#!/bin/bash

# GRETL Jobs Analyse Script
# Generiert Markdown-Dokumentation für Jenkins-gesteuerte GRETL-Jobs
# Analysiert triggers.cron und triggers.upstream

OUTPUT_FILE="GRETL_Jobs_Overview.md"
TEMP_DIR=$(mktemp -d)

# Pfad zu GRETL-Jobs bestimmen
CURRENT_DIR=$(pwd)
if [[ "$CURRENT_DIR" == *"/gretljobs-meta" ]]; then
    GRETL_JOBS_DIR="../gretljobs"
else
    GRETL_JOBS_DIR="."
fi

echo "=== GRETL Jobs Dokumentation Generator ==="
echo "Aktuelles Verzeichnis: $CURRENT_DIR"
echo "Suche GRETL-Jobs in: $GRETL_JOBS_DIR"
echo "Analysiere Jobs mit 'triggers.cron' und 'triggers.upstream' Properties..."
echo "Ignoriere searchindex_*.sql Dateien in der Analyse..."
echo

# Prüfe ob GRETL-Jobs Verzeichnis existiert
if [[ ! -d "$GRETL_JOBS_DIR" ]]; then
    echo "FEHLER: GRETL-Jobs Verzeichnis '$GRETL_JOBS_DIR' nicht gefunden!" >&2
    echo "Stelle sicher, dass das Script aus dem korrekten Verzeichnis läuft." >&2
    exit 1
fi

# Funktion um Jenkins-Cron-Ausdruck in lesbaren Text zu konvertieren
cron_to_text() {
    local cron="$1"

    if [[ -z "$cron" ]]; then
        echo "-"
        return
    fi

    local minute=$(echo "$cron" | cut -d' ' -f1)
    local hour=$(echo "$cron" | cut -d' ' -f2)
    local day=$(echo "$cron" | cut -d' ' -f3)
    local month=$(echo "$cron" | cut -d' ' -f4)
    local dow=$(echo "$cron" | cut -d' ' -f5)

    # Jenkins H-Syntax behandeln
    local time_str=""

    if [[ "$hour" == "H" ]]; then
        time_str="~zufällig"
    elif [[ "$hour" == *"H("*"-"*")"* ]]; then
        local start=$(echo "$hour" | sed 's/.*H(\([0-9]*\)-.*/\1/')
        local end=$(echo "$hour" | sed 's/.*-\([0-9]*\)).*/\1/')
        time_str="~${start}-${end}h"
    elif [[ "$hour" =~ ^[0-9]+$ ]]; then
        if [[ "$minute" == "H" ]]; then
            time_str="~${hour}:xx"
        elif [[ "$minute" =~ ^[0-9]+$ ]]; then
            time_str=$(printf "%02d:%02d" "$hour" "$minute")
        else
            time_str="${hour}:xx"
        fi
    elif [[ "$hour" == *"/"* ]]; then
        local interval=$(echo "$hour" | cut -d'/' -f2)
        time_str="alle ${interval}h"
    else
        time_str="~variabel"
    fi

    # Wochentag/Periode
    case "$dow" in
        0|7) echo "So $time_str" ;;
        1) echo "Mo $time_str" ;;
        2) echo "Di $time_str" ;;
        3) echo "Mi $time_str" ;;
        4) echo "Do $time_str" ;;
        5) echo "Fr $time_str" ;;
        6) echo "Sa $time_str" ;;
        *)
            if [[ "$day" =~ ^[0-9]+$ ]]; then
                echo "${day}. $time_str"
            else
                echo "$time_str"
            fi
            ;;
    esac
}

# Markdown-Header erstellen
cat > "$OUTPUT_FILE" << 'EOF'
# GRETL Jobs Übersicht

EOF

echo "*Generiert am: $(date)*" >> "$OUTPUT_FILE"
echo "*Repository: $(basename "$GRETL_JOBS_DIR")*" >> "$OUTPUT_FILE"
echo "*Jenkins-Instanz: [Jenkins-URL]*" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Job-Informationen sammeln
echo "Sammle Job-Informationen..."
job_info=$(mktemp)

for props in $(find "$GRETL_JOBS_DIR" -name "job.properties" -type f | sort); do
    dir=$(dirname "$props")
    job_name=$(basename "$dir")

    echo "DEBUG: Verarbeite Job '$job_name' in '$dir'" >&2

    # Schedule-Informationen extrahieren - bereinigt
    cron_schedule=""
    upstream=""

    cron_line=$(grep "triggers.cron" "$props" 2>/dev/null | head -1)
    if [[ -n "$cron_line" ]]; then
        cron_schedule=$(echo "$cron_line" | cut -d'=' -f2- | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
    fi

    upstream_line=$(grep "triggers.upstream" "$props" 2>/dev/null | head -1)
    if [[ -n "$upstream_line" ]]; then
        upstream=$(echo "$upstream_line" | cut -d'=' -f2- | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
    fi

    echo "DEBUG: Cron='$cron_schedule' Upstream='$upstream'" >&2

    if [[ -n "$cron_schedule" ]] || [[ -n "$upstream" ]]; then
        # Status ermitteln
        status="Aktiv"
        if grep -q "disabled.*true\|enabled.*false" "$props" 2>/dev/null; then
            status="Inaktiv"
        fi

        # Trigger-Typ bestimmen
        if [[ -n "$cron_schedule" ]]; then
            trigger_type="cron"
            trigger_value="$cron_schedule"
            sort_key="1_${cron_schedule}_${job_name}"
        elif [[ -n "$upstream" ]]; then
            trigger_type="upstream"
            trigger_value="$upstream"
            sort_key="2_upstream_${job_name}"
        else
            continue
        fi

        echo "DEBUG: Schreibe Job-Info: $job_name | $trigger_type | $trigger_value" >&2
        echo "$sort_key|$job_name|$trigger_type|$trigger_value|$dir|$status" >> "$job_info"
    else
        echo "DEBUG: Job '$job_name' hat keine Trigger, überspringe" >&2
    fi
done

echo "DEBUG: Job-Sammlung abgeschlossen" >&2

# Prüfe ob Jobs gefunden wurden
if [[ ! -s "$job_info" ]]; then
    echo "WARNUNG: Keine Jobs mit triggers.cron oder triggers.upstream gefunden!" >&2
    echo "Prüfe ob job.properties Dateien existieren und korrekte Trigger haben." >&2
fi

# Tabellen-Header für Jobs
cat >> "$OUTPUT_FILE" << 'EOF'
## Zeitgesteuerte Jobs (sortiert nach Schedule)

| Job Name | Trigger | Schedule | Lesbar | Pfad | Status |
|----------|---------|----------|--------|------|---------|
EOF

# Jobs sortieren und in Tabelle schreiben
sort -t'|' -k1,1 "$job_info" | while IFS='|' read -r sort_key job_name trigger_type trigger_value dir status; do
    echo "DEBUG: Verarbeite Tabelleneintrag: $job_name | $trigger_type | $trigger_value" >&2

    if [[ "$trigger_type" == "cron" ]]; then
        readable_schedule=$(cron_to_text "$trigger_value")
        echo "| $job_name | Cron | \`$trigger_value\` | $readable_schedule | \`$dir/\` | $status |" >> "$OUTPUT_FILE"
    elif [[ "$trigger_type" == "upstream" ]]; then
        echo "| $job_name | Upstream | $trigger_value | - | \`$dir/\` | $status |" >> "$OUTPUT_FILE"
    fi
done

echo "DEBUG: Tabellenerstellung abgeschlossen" >&2

# Tabellenzugriffe-Sektion
echo "" >> "$OUTPUT_FILE"
echo "## Tabellenzugriffe pro Job" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Für jeden Job detaillierte Analyse
sort -t'|' -k1,1 "$job_info" | while IFS='|' read -r sort_key job_name trigger_type trigger_value dir status; do
    echo "### $job_name" >> "$OUTPUT_FILE"
    echo "- **Pfad**: \`$dir/\`" >> "$OUTPUT_FILE"

    if [[ "$trigger_type" == "cron" ]]; then
        readable_schedule=$(cron_to_text "$trigger_value")
        echo "- **Schedule**: \`$trigger_value\` ($readable_schedule)" >> "$OUTPUT_FILE"
    elif [[ "$trigger_type" == "upstream" ]]; then
        echo "- **Upstream-Trigger**: $trigger_value" >> "$OUTPUT_FILE"
    fi

    # Quell-Tabellen analysieren
    source_tables=$(mktemp)
    find "$dir" -name "*.sql" -type f ! -name "searchindex_*.sql" -exec grep -ihE "FROM[[:space:]]+[[:alnum:]_.]+" {} \; 2>/dev/null | \
        sed -E 's/.*FROM[[:space:]]+([[:alnum:]_.]+).*/\1/i' | \
        sort -u | head -10 > "$source_tables"

    if [[ -s "$source_tables" ]]; then
        echo "- **Quell-Tabellen**: " >> "$OUTPUT_FILE"
        while read -r table; do
            [[ -n "$table" ]] && echo "  - \`$table\` (READ)" >> "$OUTPUT_FILE"
        done < "$source_tables"
    fi

    # Ziel-Tabellen analysieren
    target_tables=$(mktemp)
    find "$dir" -name "*.sql" -type f ! -name "searchindex_*.sql" -exec grep -ihE "(INSERT INTO|UPDATE|CREATE TABLE)[[:space:]]+[[:alnum:]_.]+" {} \; 2>/dev/null | \
        sed -E 's/.*(INSERT INTO|UPDATE|CREATE TABLE)[[:space:]]+([[:alnum:]_.]+).*/\2/i' | \
        sort -u | head -10 > "$target_tables"

    if [[ -s "$target_tables" ]]; then
        echo "- **Ziel-Tabellen**: " >> "$OUTPUT_FILE"
        while read -r table; do
            [[ -n "$table" ]] && echo "  - \`$table\` (INSERT/UPDATE)" >> "$OUTPUT_FILE"
        done < "$target_tables"
    fi

    echo "" >> "$OUTPUT_FILE"

    rm -f "$source_tables" "$target_tables"
done

# Häufig verwendete Tabellen
echo "" >> "$OUTPUT_FILE"
echo "## Häufig verwendete Tabellen" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "| Anzahl | Tabellenname | Schema |" >> "$OUTPUT_FILE"
echo "|--------|-------------|--------|" >> "$OUTPUT_FILE"

find "$GRETL_JOBS_DIR" -name "*.sql" -type f ! -name "searchindex_*.sql" -exec grep -ihE "(FROM|INSERT INTO|UPDATE)[[:space:]]+[[:alnum:]_.]+" {} \; 2>/dev/null | \
    sed -E 's/.*(FROM|INSERT INTO|UPDATE)[[:space:]]+([[:alnum:]_.]+).*/\2/i' | \
    sort | uniq -c | sort -nr | head -10 | while read -r count table; do
    if [[ -n "$table" ]]; then
        schema=$(echo "$table" | cut -d'.' -f1)
        table_name=$(echo "$table" | cut -d'.' -f2)
        echo "| $count | $table_name | $schema |" >> "$OUTPUT_FILE"
    fi
done

# Footer
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "*Diese Dokumentation wurde automatisch generiert am $(date)*" >> "$OUTPUT_FILE"

# Cleanup
rm -rf "$TEMP_DIR"
rm -f "$job_info" 2>/dev/null

echo "✅ Dokumentation erstellt: $OUTPUT_FILE"
echo "📄 Script completed successfully!"
