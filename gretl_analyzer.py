#!/usr/bin/env python3
"""
GRETL Jobs Analyzer - Python Version
Converts the JavaScript GRETL Jobs Analyzer to Python

Analyzes GRETL Jenkins Jobs and generates documentation from job.properties files.
"""

import os
import sys
import re
import glob
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
import logging


class GretlJobsAnalyzer:
    """GRETL Jobs Analyzer for analyzing Jenkins jobs and generating documentation."""

    def __init__(self, gretl_jobs_dir: str = '../gretljobs',
                 output_file: str = 'GRETL_Jobs_Overview.md',
                 debug: bool = False):
        """
        Initialize the analyzer.

        Args:
            gretl_jobs_dir: Path to the GRETL jobs directory
            output_file: Path to the output markdown file
            debug: Enable debug logging
        """
        self.gretl_jobs_dir = Path(gretl_jobs_dir)
        self.output_file = Path(output_file)
        self.debug = debug

        # Setup logging
        level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=level, format='[%(levelname)s] %(message)s')
        self.logger = logging.getLogger(__name__)

    def log(self, message: str) -> None:
        """Log debug message if debug mode is enabled."""
        if self.debug:
            self.logger.debug(message)

    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(message)

    def path_exists(self, file_path: Path) -> bool:
        """Check if path exists."""
        return file_path.exists()

    def parse_job_properties(self, file_path: Path) -> Dict[str, str]:
        """
        Parse job.properties file.

        Args:
            file_path: Path to the job.properties file

        Returns:
            Dictionary of properties
        """
        try:
            properties = {}
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, *value_parts = line.split('=')
                            if key and value_parts:
                                properties[key.strip()] = '='.join(value_parts).strip()
            return properties
        except Exception as e:
            self.error(f"Error parsing {file_path}: {e}")
            return {}

    def cron_to_text(self, cron_expression: str) -> str:
        """
        Convert Jenkins cron expression to human readable format.

        Args:
            cron_expression: Jenkins cron expression

        Returns:
            Human readable time string
        """
        if not cron_expression:
            return '-'

        parts = cron_expression.split(' ')
        if len(parts) < 5:
            return cron_expression

        minute, hour, day, month, dow = parts[:5]

        # Handle Jenkins H syntax
        time_str = ''

        if hour == 'H':
            time_str = '~zufällig'
        elif re.match(r'H\((\d+)-(\d+)\)', hour):
            match = re.match(r'H\((\d+)-(\d+)\)', hour)
            time_str = f"~{match.group(1)}-{match.group(2)}h"
        elif re.match(r'^\d+$', hour):
            if minute == 'H':
                time_str = f"~{hour}:xx"
            elif re.match(r'^\d+$', minute):
                time_str = f"{hour.zfill(2)}:{minute.zfill(2)}"
            else:
                time_str = f"{hour}:xx"
        elif re.match(r'^\*/\d+$', hour):
            # Only handle standard interval syntax */N, not H/N
            interval = hour.split('/')[1]
            time_str = f"alle {interval}h"
        else:
            time_str = '~variabel'

        # Handle day of week
        day_names = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa']
        if dow != '*':
            try:
                day_num = int(dow)
                if 0 <= day_num <= 6:
                    return f"{day_names[day_num]} {time_str}"
                elif day_num == 7:
                    return f"{day_names[0]} {time_str}"  # 7 is also Sunday
            except ValueError:
                pass
        elif re.match(r'^\d+$', day):
            return f"{day}. {time_str}"

        return time_str

    def find_job_properties(self) -> List[Path]:
        """
        Find all job.properties files.

        Returns:
            List of paths to job.properties files
        """
        pattern = str(self.gretl_jobs_dir / '**/job.properties')
        self.log(f"Searching for job.properties files in: {pattern}")

        try:
            files = [Path(f) for f in glob.glob(pattern, recursive=True)]
            self.log(f"Found {len(files)} job.properties files")
            return files
        except Exception as e:
            self.error(f"Error finding job.properties files: {e}")
            return []

    def extract_cte_names(self, sql_content: str) -> Set[str]:
        """
        Extract CTE (Common Table Expression) names from SQL content.

        Args:
            sql_content: SQL content

        Returns:
            Set of CTE names (lowercase)
        """
        cte_names = set()

        # Remove comments and strings to avoid false matches
        clean_sql = sql_content
        clean_sql = re.sub(r'--[^\n]*', '', clean_sql)  # Remove single-line comments
        clean_sql = re.sub(r'/\*[\s\S]*?\*/', '', clean_sql)  # Remove multi-line comments
        clean_sql = re.sub(r"'[^']*'", "''", clean_sql)  # Remove string literals
        clean_sql = re.sub(r'"[^"]*"', '""', clean_sql)  # Remove quoted identifiers

        # Match WITH clauses: WITH cte_name AS (...), another_cte AS (...)
        with_matches = re.findall(r'WITH\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+AS\s*\(', clean_sql, re.IGNORECASE)
        for match in with_matches:
            cte_names.add(match.lower())

        # Match additional CTEs in the same WITH clause: , cte_name AS (...)
        additional_cte_matches = re.findall(r',\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+AS\s*\(', clean_sql, re.IGNORECASE)
        for match in additional_cte_matches:
            cte_names.add(match.lower())

        self.log(f"Found CTEs: {', '.join(cte_names)}")
        return cte_names

    def analyze_sql_files(self, job_dir: Path) -> Dict[str, List[str]]:
        """
        Analyze SQL files for table access.

        Args:
            job_dir: Job directory path

        Returns:
            Dictionary with 'sourceTables' and 'targetTables' lists
        """
        pattern = str(job_dir / '**/*.sql')

        try:
            sql_files = [Path(f) for f in glob.glob(pattern, recursive=True)]
            # Filter out searchindex files
            filtered_files = [f for f in sql_files if not f.name.startswith('searchindex_')]

            source_tables = set()
            target_tables = set()

            for sql_file in filtered_files:
                try:
                    with open(sql_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Extract CTE names to ignore them later
                    cte_names = self.extract_cte_names(content)

                    # Find FROM tables (source)
                    from_matches = re.findall(r'FROM\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content, re.IGNORECASE)
                    for match in from_matches:
                        table = match.strip()
                        if table.lower() not in cte_names:
                            source_tables.add(table)

                    # Find JOIN tables (also source)
                    join_matches = re.findall(r'JOIN\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content, re.IGNORECASE)
                    for match in join_matches:
                        table = match.strip()
                        if table.lower() not in cte_names:
                            source_tables.add(table)

                    # Find INSERT/UPDATE/CREATE tables (target)
                    target_matches = re.findall(r'(INSERT\s+INTO|UPDATE|CREATE\s+TABLE)\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content, re.IGNORECASE)
                    for match in target_matches:
                        table = match[1].strip()
                        target_tables.add(table)

                except Exception as e:
                    self.error(f"Error reading SQL file {sql_file}: {e}")

            return {
                'sourceTables': list(source_tables),
                'targetTables': list(target_tables)
            }
        except Exception as e:
            self.error(f"Error analyzing SQL files in {job_dir}: {e}")
            return {'sourceTables': [], 'targetTables': []}

    def analyze_jobs(self) -> List[Dict]:
        """
        Analyze all jobs.

        Returns:
            List of job dictionaries
        """
        job_files = self.find_job_properties()
        jobs = []

        for file_path in job_files:
            job_dir = file_path.parent
            job_name = job_dir.name

            self.log(f"Processing job: {job_name}")

            properties = self.parse_job_properties(file_path)
            cron_schedule = properties.get('triggers.cron')
            upstream = properties.get('triggers.upstream')

            if cron_schedule or upstream:
                status = 'Inaktiv' if (properties.get('disabled') == 'true' or
                                     properties.get('enabled') == 'false') else 'Aktiv'

                trigger_type = 'cron' if cron_schedule else 'upstream'
                trigger_value = cron_schedule or upstream

                # Analyze SQL files
                sql_analysis = self.analyze_sql_files(job_dir)

                jobs.append({
                    'name': job_name,
                    'path': str(job_dir),
                    'triggerType': trigger_type,
                    'triggerValue': trigger_value,
                    'cronSchedule': cron_schedule,
                    'upstream': upstream,
                    'status': status,
                    'sourceTables': sql_analysis['sourceTables'],
                    'targetTables': sql_analysis['targetTables'],
                    'sortKey': '1' if trigger_type == 'cron' else '2'
                })

        # Sort jobs: cron jobs first, then by name
        jobs.sort(key=lambda x: (x['sortKey'], x['name'].lower()))
        return jobs

    def get_amtsstelle_from_schema(self, schema: str) -> Optional[str]:
        """
        Get Amtsstelle description from schema name (sogis specific).

        Args:
            schema: Schema name

        Returns:
            Amtsstelle description or None
        """
        schema_mappings = {
            'agi': 'Amt für Geoinformation',
            'afu': 'Amt für Umwelt',
            'arp': 'Amt für Raumplanung',
            'ada': 'Amt für Denkmalpflege und Archäologie',
            'avt': 'Amt für Verkehr und Tiefbau',
            'awjf': 'Amt für Wald, Jagd und Fischerei',
            'alw': 'Amt für Landwirtschaft',
            'so': 'Kanton Solothurn'
        }

        prefix = schema.split('_')[0].lower()
        return schema_mappings.get(prefix)

    def generate_markdown(self, jobs: List[Dict]) -> str:
        """
        Generate markdown documentation.

        Args:
            jobs: List of job dictionaries

        Returns:
            Markdown content string
        """
        from datetime import datetime

        lines = [
            "# GRETL Jobs Übersicht",
            "",
            f"**Automatisch generiert am:** {datetime.now().strftime('%d.%m.%Y %H:%M')}",
            f"**Anzahl Jobs:** {len(jobs)}",
            "",
            "## Inhaltsverzeichnis",
            "",
            "- [Zeitgesteuerte Jobs (Cron)](#zeitgesteuerte-jobs-cron)",
            "- [Upstream-gesteuerte Jobs](#upstream-gesteuerte-jobs)",
            "- [Schema-Übersicht](#schema-übersicht)",
            "",
            "---",
            ""
        ]

        # Group jobs by trigger type
        cron_jobs = [job for job in jobs if job['triggerType'] == 'cron']
        upstream_jobs = [job for job in jobs if job['triggerType'] == 'upstream']

        # Zeitgesteuerte Jobs
        lines.extend([
            "## Zeitgesteuerte Jobs (Cron)",
            "",
            f"**Anzahl:** {len(cron_jobs)}",
            ""
        ])

        if cron_jobs:
            lines.extend([
                "| Job | Status | Schedule | Quell-Tabellen | Ziel-Tabellen |",
                "|-----|--------|----------|----------------|---------------|"
            ])

            for job in cron_jobs:
                schedule = self.cron_to_text(job['cronSchedule'])
                source_tables = ', '.join(job['sourceTables'][:3])
                if len(job['sourceTables']) > 3:
                    source_tables += f" (+{len(job['sourceTables']) - 3} weitere)"
                target_tables = ', '.join(job['targetTables'][:3])
                if len(job['targetTables']) > 3:
                    target_tables += f" (+{len(job['targetTables']) - 3} weitere)"

                lines.append(f"| {job['name']} | {job['status']} | {schedule} | {source_tables} | {target_tables} |")
        else:
            lines.append("*Keine zeitgesteuerten Jobs gefunden.*")

        lines.extend(["", "---", ""])

        # Upstream Jobs
        lines.extend([
            "## Upstream-gesteuerte Jobs",
            "",
            f"**Anzahl:** {len(upstream_jobs)}",
            ""
        ])

        if upstream_jobs:
            lines.extend([
                "| Job | Status | Upstream | Quell-Tabellen | Ziel-Tabellen |",
                "|-----|--------|----------|----------------|---------------|"
            ])

            for job in upstream_jobs:
                source_tables = ', '.join(job['sourceTables'][:3])
                if len(job['sourceTables']) > 3:
                    source_tables += f" (+{len(job['sourceTables']) - 3} weitere)"
                target_tables = ', '.join(job['targetTables'][:3])
                if len(job['targetTables']) > 3:
                    target_tables += f" (+{len(job['targetTables']) - 3} weitere)"

                lines.append(f"| {job['name']} | {job['status']} | {job['upstream']} | {source_tables} | {target_tables} |")
        else:
            lines.append("*Keine upstream-gesteuerten Jobs gefunden.*")

        lines.extend(["", "---", ""])

        # Schema-Übersicht
        schemas = self.analyze_schemas(jobs)
        lines.extend([
            "## Schema-Übersicht",
            "",
            f"**Anzahl Schemas:** {len(schemas)}",
            "",
            "| Schema | Beschreibung | Anzahl Jobs | Anzahl Tabellen |",
            "|--------|--------------|-------------|-----------------|"
        ])

        for schema, info in sorted(schemas.items()):
            lines.append(f"| {schema} | {info['description']} | {len(info['jobs'])} | {len(info['tables'])} |")

        lines.extend(["", "---", ""])

        # Detailierte Job-Informationen
        lines.extend([
            "## Detailierte Job-Informationen",
            ""
        ])

        for job in jobs:
            lines.extend([
                f"### {job['name']}",
                "",
                f"**Status:** {job['status']}",
                f"**Trigger:** {job['triggerType']}",
                f"**Pfad:** `{job['path']}`"
            ])

            if job['cronSchedule']:
                lines.append(f"**Schedule:** {job['cronSchedule']} ({self.cron_to_text(job['cronSchedule'])})")

            if job['upstream']:
                lines.append(f"**Upstream:** {job['upstream']}")

            if job['sourceTables']:
                lines.extend([
                    "",
                    "**Quell-Tabellen:**"
                ])
                for table in job['sourceTables']:
                    lines.append(f"- {table}")

            if job['targetTables']:
                lines.extend([
                    "",
                    "**Ziel-Tabellen:**"
                ])
                for table in job['targetTables']:
                    lines.append(f"- {table}")

            lines.extend(["", "---", ""])

        return '\n'.join(lines)

    def analyze_schemas(self, jobs: List[Dict]) -> Dict[str, Dict]:
        """
        Analyze schemas used by jobs.

        Args:
            jobs: List of job dictionaries

        Returns:
            Dictionary of schema information
        """
        schemas = {}

        for job in jobs:
            all_tables = job['sourceTables'] + job['targetTables']
            for table in all_tables:
                if '.' in table:
                    schema = table.split('.')[0]

                    if schema not in schemas:
                        schemas[schema] = {
                            'description': self.get_amtsstelle_from_schema(schema) or schema,
                            'jobs': set(),
                            'tables': set()
                        }

                    schemas[schema]['jobs'].add(job['name'])
                    schemas[schema]['tables'].add(table)

        # Convert sets to lists for JSON serialization
        for schema in schemas:
            schemas[schema]['jobs'] = list(schemas[schema]['jobs'])
            schemas[schema]['tables'] = list(schemas[schema]['tables'])

        return schemas

    def run(self) -> None:
        """Main analysis function."""
        print('=== GRETL Jobs Dokumentation Generator (Python) ===')
        print(f'Analysiere Jobs in: {self.gretl_jobs_dir}')
        print(f'Ausgabedatei: {self.output_file}')

        # Check if GRETL jobs directory exists
        if not self.path_exists(self.gretl_jobs_dir):
            self.error(f"GRETL Jobs directory not found: {self.gretl_jobs_dir}")
            sys.exit(1)

        try:
            # Analyze jobs
            jobs = self.analyze_jobs()

            if len(jobs) == 0:
                print('⚠️  No jobs with triggers found')
                return

            # Generate documentation
            markdown = self.generate_markdown(jobs)

            # Write to file
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)

            print(f'✅ Documentation created: {self.output_file}')
            print(f'📊 Analyzed {len(jobs)} jobs')
            print(f'📄 Script completed successfully!')

        except Exception as e:
            self.error(f"Analysis failed: {e}")
            sys.exit(1)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description='Analyze GRETL Jenkins jobs and generate documentation')
    parser.add_argument('--gretl-jobs-dir', default=os.environ.get('GRETL_JOBS_DIR', '../gretljobs'),
                        help='Path to GRETL jobs directory (default: ../gretljobs)')
    parser.add_argument('--output-file', default=os.environ.get('OUTPUT_FILE', 'GRETL_Jobs_Overview.md'),
                        help='Output markdown file (default: GRETL_Jobs_Overview.md)')
    parser.add_argument('--debug', action='store_true', default=os.environ.get('DEBUG', '').lower() == 'true',
                        help='Enable debug output')

    args = parser.parse_args()

    analyzer = GretlJobsAnalyzer(
        gretl_jobs_dir=args.gretl_jobs_dir,
        output_file=args.output_file,
        debug=args.debug
    )

    analyzer.run()


if __name__ == '__main__':
    main()
