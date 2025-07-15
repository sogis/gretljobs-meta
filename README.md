> [!TIP]
> Siehe [Zusammenfassung](./GRETL_Jobs_Overview.md), täglich um 4:00 UTC automatisch aktualisiert



# GRETL Jobs Analyzer - sogis
[![GRETL Jobs Analysis (Node.js)](https://github.com/sogis/gretljobs-meta/actions/workflows/gretl-analysis-nodejs.yml/badge.svg)](https://github.com/sogis/gretljobs-meta/actions/workflows/gretl-analysis-nodejs.yml)

Ein Node.js-basierter Analyzer für GRETL Jenkins Jobs der **sogis** (Solothurn), der automatisch Dokumentation aus `job.properties` Dateien generiert.

Dieser Analyzer analysiert zeitgesteuerte und upstream-gestartete GRETL-Jobs aus dem [sogis/gretljobs](https://github.com/sogis/gretljobs) Repository.

## 🚀 Features

- **Jenkins H-Syntax Support**: Analysiert komplexe Jenkins Cron-Ausdrücke (`H H(1-3) * * *`)
- **Upstream Dependencies**: Erkennt Job-Abhängigkeiten via `triggers.upstream`
- **SQL Analysis**: Automatische Erkennung von Quell- und Ziel-Tabellen
- **CTE-Ignorierung**: Filtert Common Table Expressions aus der Tabellen-Analyse
- **sogis Schema Support**: Optimiert für sogis-Datenbank-Schemas (agi_, afu_, arp_, ada_)
- **Markdown Output**: Generiert strukturierte Dokumentation
- **GitHub Actions Integration**: Vollständige CI/CD Pipeline
- **Umfassende Tests**: >90% Test-Coverage

## 📦 Installation

```bash
# Repository klonen
git clone https://github.com/sogis/gretljobs-meta.git
cd gretljobs-meta

# Dependencies installieren
npm install

# Erste Analyse ausführen (benötigt ../gretljobs)
npm run analyze
```

## 🔧 Verwendung

### Lokal ausführen
```bash
# Standard-Analyse (../gretljobs → GRETL_Jobs_Overview.md)
npm start

# Mit Debug-Ausgabe
DEBUG=true npm start

# Custom Pfade
GRETL_JOBS_DIR=/path/to/gretljobs OUTPUT_FILE=custom.md npm start

# Watch Mode (automatisch bei Änderungen)
npm run watch
```

### In sogis-Umgebung
```bash
# Wenn gretljobs-meta und gretljobs nebeneinander liegen:
/sogis/
├── gretljobs-meta/     # Dieses Repository
└── gretljobs/          # GRETL Jobs Repository

cd gretljobs-meta
npm run analyze
```

## 📁 sogis Repository-Struktur

```
sogis/gretljobs/
├── agi_av_gb_abgleich/
│   ├── job.properties          # triggers.cron=H H(1-3) * * *
│   ├── av_gb_abgleich.sql      # SQL mit agi_ Schema-Tabellen
│   └── build.gradle
├── afu_gewaesser_import/
│   ├── job.properties          # triggers.upstream=agi_av_gb_abgleich
│   └── gewaesser_import.sql    # SQL mit afu_ Schema-Tabellen
└── ...
```

## 🏗️ sogis-spezifische Features

### Schema-Erkennung
Automatische Erkennung der sogis-Datenbank-Schemas:
- **agi_**: Amt für Geoinformation
- **afu_**: Amt für Umwelt
- **arp_**: Amt für Raumplanung
- **ada_**: Amt für Denkmalpflege und Archäologie
- **avt_**: Amt für Verkehr und Tiefbau

### Job-Naming Conventions
Erkennt sogis Job-Namenskonventionen:
```
{amt}_{fachbereich}_{funktion}[_pub]
```

### Jenkins H-Syntax
Vollständige Unterstützung für Jenkins Hash-basierte Scheduling:
```properties
triggers.cron=H H(1-3) * * *     # Zufällig zwischen 1-3 Uhr
triggers.cron=H H(18-20) * * 1   # Montags zwischen 18-20 Uhr
triggers.cron=H */4 * * *         # Alle 4 Stunden
```

## 📊 Beispiel-Ausgabe

```markdown
# GRETL Jobs Übersicht

| Job Name | Trigger | Schedule | Lesbar | Pfad | Status |
|----------|---------|----------|--------|------|---------|
| agi_av_gb_abgleich | Cron | `H H(1-3) * * *` | ~1-3h | `./agi_av_gb_abgleich/` | Aktiv |
| afu_gewaesser_import | Upstream | agi_av_gb_abgleich | - | `./afu_gewaesser_import/` | Aktiv |

## Tabellenzugriffe pro Job

### agi_av_gb_abgleich
- **Pfad**: `./agi_av_gb_abgleich/`
- **Schedule**: `H H(1-3) * * *` (~1-3h)
- **Quell-Tabellen**:
  - `agi_av.liegenschaften` (READ)
  - `agi_gb.grundstuecke` (READ)
- **Ziel-Tabellen**:
  - `agi_av_gb_abgleich.differenzen` (INSERT/UPDATE)

## Häufig verwendete Tabellen

| Anzahl | Tabellenname | Schema |
|--------|-------------|--------|
| 15 | gemeindegrenzen | agi_hoheitsgrenzen |
| 12 | nutzungsplanung | arp_npl |
| 8 | gewaesser | afu_gewaesser |
```

## 🔄 GitHub Actions Integration

Die GitHub Action läuft automatisch:

### Triggers
- **Täglich um 4:00 UTC**
- **Bei Push in main branch**
- **Manuell über GitHub UI**
- **Webhook vom gretljobs Repository**

### Outputs
- **Aktualisierte Dokumentation** in `GRETL_Jobs_Overview.md`
- **Artefakt-Download** für 30 Tage
- **Automatische Commits** bei Änderungen

## 🧪 Tests

```bash
# Alle Tests ausführen
npm test

# Tests mit Coverage-Report
npm run test:coverage

# Tests im Watch-Mode
npm run test:watch

# Linting
npm run lint
```

**Test-Coverage**: >90% für alle Metriken

## ⚙️ Konfiguration

### Umgebungsvariablen
```bash
GRETL_JOBS_DIR=../gretljobs        # Pfad zum gretljobs Repository
OUTPUT_FILE=GRETL_Jobs_Overview.md # Ausgabedatei
DEBUG=true                         # Debug-Modus aktivieren
```

### GitHub Secrets (für private Repos)
```yaml
GRETL_JOBS_TOKEN: ghp_xxxxx       # Personal Access Token
```

## 🐛 Troubleshooting

### Häufige Probleme

**"No jobs found"**
```bash
# Pfad-Struktur prüfen
ls -la ../gretljobs/*/job.properties

# Debug-Modus aktivieren
DEBUG=true npm start
```

**"Repository not found"**
```bash
# Prüfen ob gretljobs Repository existiert
git clone https://github.com/sogis/gretljobs.git ../gretljobs
```

## 📞 Support

- **Issues**: https://github.com/sogis/gretljobs-meta/issues
- **Kontakt**: christian.baumann@bd.so.ch
- **Dokumentation**: Siehe README im sogis/gretljobs Repository

## 📄 Lizenz

MIT License

---

