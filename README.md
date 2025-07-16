[![GRETL Jobs Analysis (Node.js)](https://github.com/sogis/gretljobs-meta/actions/workflows/gretl-analysis-nodejs.yml/badge.svg)](https://github.com/sogis/gretljobs-meta/actions/workflows/gretl-analysis-nodejs.yml)

> [!TIP]
> Siehe [Zusammenfassung](./nodejs_version/GRETL_Jobs_Overview.md), täglich um 4:00 UTC automatisch aktualisiert

# GRETL Jobs Analyzer - sogis

Ein Python-basierter Analyzer für GRETL Jenkins Jobs, der automatisch Dokumentation aus `job.properties` Dateien generiert.

## 🚀 Features

- **Jenkins H-Syntax Support**: Analysiert komplexe Jenkins Cron-Ausdrücke (`H H(1-3) * * *`)
- **Upstream Dependencies**: Erkennt Job-Abhängigkeiten via `triggers.upstream`
- **SQL Analysis**: Automatische Erkennung von Quell- und Ziel-Tabellen
- **CTE-Ignorierung**: Filtert Common Table Expressions aus der Tabellen-Analyse
- **Schema Support**: Optimiert für Datenbank-Schemas (agi_, afu_, arp_, ada_)
- **Markdown Output**: Generiert strukturierte Dokumentation
- **Cross-Platform**: Läuft auf Windows, macOS und Linux
- **Type Hints**: Vollständig typisiert für bessere Code-Qualität

## 📋 Anforderungen

- Python 3.7 oder höher
- Keine externen Dependencies (nur Python Standard Library)

## 📦 Installation

### Option 1: Direkte Verwendung
```bash
# Repository klonen
git clone <your-repo-url>
cd gretl-analyzer-python

# Script ausführbar machen (Linux/macOS)
chmod +x gretl_analyzer.py

# Erste Analyse ausführen
python gretl_analyzer.py --gretl-jobs-dir ../gretljobs
```

### Option 2: Als Python Package
```bash
# Erstelle setup.py für Installation
pip install -e .

# Dann verwendbar als:
gretl-analyzer --help
```

## 🔧 Verwendung

### Kommandozeile

```bash
# Standard-Analyse (../gretljobs → GRETL_Jobs_Overview.md)
python gretl_analyzer.py

# Mit Debug-Ausgabe
python gretl_analyzer.py --debug

# Custom Pfade
python gretl_analyzer.py --gretl-jobs-dir /path/to/gretljobs --output-file custom.md

# Hilfe anzeigen
python gretl_analyzer.py --help
```

### Umgebungsvariablen
```bash
# Pfade über Umgebungsvariablen setzen
export GRETL_JOBS_DIR=/path/to/gretljobs
export OUTPUT_FILE=custom_output.md
export DEBUG=true

python gretl_analyzer.py
```

### Als Python Modul verwenden

```python
from gretl_analyzer import GretlJobsAnalyzer

# Analyzer erstellen
analyzer = GretlJobsAnalyzer(
    gretl_jobs_dir='../gretljobs',
    output_file='GRETL_Jobs_Overview.md',
    debug=True
)

# Analyse ausführen
analyzer.run()

# Oder einzelne Methoden verwenden
jobs = analyzer.analyze_jobs()
markdown = analyzer.generate_markdown(jobs)
```

## 📁 Repository-Struktur

```
gretl-analyzer-python/
├── gretl_analyzer.py          # Haupt-Analyzer Klasse
├── test_gretl_analyzer.py     # Unit Tests
├── requirements.txt           # Python Dependencies (leer, da nur stdlib)
├── setup.py                   # Python Package Setup
├── README.md                  # Diese Datei
└── examples/
    ├── example_job.properties  # Beispiel job.properties
    └── sample_output.md        # Beispiel-Ausgabe
```

### Erwartete GRETL Jobs Struktur
```
gretljobs/
├── job1_name/
│   ├── job.properties          # triggers.cron=H H(1-3) * * *
│   ├── main_query.sql          # SQL mit Schema-Tabellen
│   └── build.gradle
├── job2_name/
│   ├── job.properties          # triggers.upstream=job1_name
│   └── transform.sql
└── ...
```

## ⚙️ Konfiguration

### Kommandozeilenoptionen

| Option | Umgebungsvariable | Standard | Beschreibung |
|--------|-------------------|----------|--------------|
| `--gretl-jobs-dir` | `GRETL_JOBS_DIR` | `../gretljobs` | Pfad zum GRETL Jobs Verzeichnis |
| `--output-file` | `OUTPUT_FILE` | `GRETL_Jobs_Overview.md` | Ausgabe Markdown-Datei |
| `--debug` | `DEBUG=true` | `false` | Debug-Modus aktivieren |

### job.properties Format

Das Script erkennt folgende Properties:

```properties
# Zeitgesteuerte Jobs
triggers.cron=H H(1-3) * * *
triggers.cron=0 2 * * *
triggers.cron=*/15 * * * *

# Upstream-abhängige Jobs
triggers.upstream=other_job_name

# Job Status
disabled=true
enabled=false
```

### Unterstützte Jenkins Cron-Syntax

| Ausdruck | Beschreibung | Ausgabe |
|----------|--------------|---------|
| `0 6 * * *` | Täglich um 6:00 | `06:00` |
| `H H * * *` | Zufällige Zeit | `~zufällig` |
| `H H(1-3) * * *` | Zufällig zwischen 1-3 Uhr | `~1-3h` |
| `0 */4 * * *` | Alle 4 Stunden | `alle 4h` |
| `0 9 * * 1` | Montags um 9:00 | `Mo 09:00` |

## 📊 Ausgabe-Format

Das Script generiert eine strukturierte Markdown-Datei mit:

### 1. Übersichtstabellen
- **Zeitgesteuerte Jobs**: Cron-Schedule, Status, Tabellen
- **Upstream Jobs**: Abhängigkeiten, Status, Tabellen
- **Schema-Übersicht**: Verwendete Datenbank-Schemas

### 2. Detailierte Job-Informationen
Für jeden Job:
- Status (Aktiv/Inaktiv)
- Trigger-Typ und -Wert
- Pfad zum Job
- Quell-Tabellen (aus SQL-Analyse)
- Ziel-Tabellen (aus SQL-Analyse)

### Beispiel-Ausgabe
```markdown
# GRETL Jobs Übersicht

**Automatisch generiert am:** 15.07.2025 10:30
**Anzahl Jobs:** 45

## Zeitgesteuerte Jobs (Cron)

| Job | Status | Schedule | Quell-Tabellen | Ziel-Tabellen |
|-----|--------|----------|----------------|---------------|
| agi_av_gb_abgleich | Aktiv | ~1-3h | agi_av.grundbuch, agi_av.liegenschaften | agi_av.abgleich_result |
```

## 🧪 Tests

```bash
# Alle Tests ausführen
python -m unittest test_gretl_analyzer.py

# Tests mit verbose Ausgabe
python -m unittest -v test_gretl_analyzer.py

# Einzelne Testklasse
python -m unittest test_gretl_analyzer.TestGretlJobsAnalyzer

# Mit Coverage (wenn installiert)
pip install coverage
coverage run -m unittest test_gretl_analyzer.py
coverage report
coverage html
```

### Test-Abdeckung
- ✅ Job Properties Parsing
- ✅ Cron Expression Parsing
- ✅ SQL File Analysis
- ✅ CTE Detection
- ✅ Schema Analysis
- ✅ Markdown Generation
- ✅ Error Handling

## 🔄 Migration von JavaScript

### Hauptunterschiede zur JavaScript-Version

| Aspekt | JavaScript/Node.js | Python |
|--------|-------------------|---------|
| **Dependencies** | glob, jest, eslint | Nur Python stdlib |
| **File Operations** | fs.promises | pathlib, open() |
| **Regex** | String.match() | re.findall(), re.match() |
| **Testing** | Jest | unittest |
| **CLI** | process.env | argparse |
| **Async** | async/await | Synchron |

### Funktionale Äquivalenz
✅ Alle Features der JavaScript-Version portiert
✅ Gleiche Ausgabe-Formate
✅ Identische Cron-Parsing-Logik
✅ Gleiche SQL-Analyse-Features

## 🐛 Troubleshooting

### Häufige Probleme

**"No jobs with triggers found"**
```bash
# Verzeichnis-Struktur prüfen
ls -la ../gretljobs/*/job.properties

# Debug-Modus aktivieren
python gretl_analyzer.py --debug
```

**"GRETL Jobs directory not found"**
```bash
# Pfad explizit setzen
python gretl_analyzer.py --gretl-jobs-dir /absolute/path/to/gretljobs

# Oder relativ vom aktuellen Verzeichnis
python gretl_analyzer.py --gretl-jobs-dir ./gretljobs
```

**"Permission denied" (Linux/macOS)**
```bash
# Script ausführbar machen
chmod +x gretl_analyzer.py

# Oder direkt über Python aufrufen
python gretl_analyzer.py
```

### Debug-Ausgabe
```bash
python gretl_analyzer.py --debug
```
Zeigt detaillierte Informationen über:
- Gefundene job.properties Dateien
- Erkannte CTEs in SQL-Dateien
- Geparste Cron-Expressions
- Extrahierte Tabellen-Namen

## 🔧 Entwicklung

### Code-Stil
- **PEP 8** konforme Formatierung
- **Type Hints** für alle Funktionen
- **Docstrings** im Google-Stil
- **Logging** statt print() für Debug-Ausgaben

### Erweiterungen hinzufügen

```python
class GretlJobsAnalyzer:
    def custom_analysis(self, jobs: List[Dict]) -> Dict:
        """Füge eigene Analyse-Logik hinzu."""
        # Implementierung hier
        pass

    def generate_custom_output(self, jobs: List[Dict]) -> str:
        """Generiere alternatives Ausgabe-Format."""
        # z.B. JSON, HTML, XML
        pass
```

### GitHub Actions Integration

```yaml
name: GRETL Jobs Analysis (Python)

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Run Analysis
      run: |
        python gretl_analyzer.py --gretl-jobs-dir ../gretljobs

    - name: Run Tests
      run: |
        python -m unittest test_gretl_analyzer.py
```

## 📞 Support

- **Issues**: https://github.com/sogis/gretljobs-meta/issues
- **Kontakt**: christian.baumann@bd.so.ch
- **Dokumentation**: Siehe README im sogis/gretljobs Repository

## 📄 Lizenz

MIT License


## 🔗 Siehe auch

- [GRETL Documentation](https://github.com/sogis/gretl)
- [Jenkins Cron Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/#cron-syntax)
- [Python pathlib](https://docs.python.org/3/library/pathlib.html)
- [Python argparse](https://docs.python.org/3/library/argparse.html)


