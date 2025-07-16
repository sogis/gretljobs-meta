#!/usr/bin/env python3
"""
GRETL Jobs Analyzer - Python Version
Analyzes GRETL Jenkins Jobs and generates documentation from job.properties files.
"""

import os
import sys
import re
import glob
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional
import logging


class GretlJobsAnalyzer:
    """GRETL Jobs Analyzer for analyzing Jenkins jobs and generating documentation."""

    def __init__(
        self,
        gretl_jobs_dir: str = "../gretljobs",
        output_file: str = "GRETL_Jobs_Overview.md",
        debug: bool = False,
    ):
        """Initialize the analyzer."""
        self.gretl_jobs_dir = Path(gretl_jobs_dir)
        self.output_file = Path(output_file)
        self.debug = debug

        # Setup logging
        level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")
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
        """Parse job.properties file."""
        try:
            properties = {}
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        if "=" in line:
                            key, *value_parts = line.split("=")
                            if key and value_parts:
                                properties[key.strip()] = "=".join(value_parts).strip()
            return properties
        except Exception as e:
            self.error(f"Error parsing {file_path}: {e}")
            return {}

    def cron_to_text(self, cron_expression: str) -> str:
        """Convert Jenkins cron expression to human readable format."""
        if not cron_expression:
            return "-"

        parts = cron_expression.split(" ")
        if len(parts) < 5:
            return cron_expression

        minute, hour, day, month, dow = parts[:5]

        # Handle Jenkins H syntax
        time_str = ""

        if hour == "H":
            time_str = "~zufällig"
        elif re.match(r"H\((\d+)-(\d+)\)", hour):
            match = re.match(r"H\((\d+)-(\d+)\)", hour)
            time_str = f"~{match.group(1)}-{match.group(2)}h"
        elif re.match(r"^\d+$", hour):
            if minute == "H":
                time_str = f"~{hour}:xx"
            elif re.match(r"^\d+$", minute):
                time_str = f"{hour.zfill(2)}:{minute.zfill(2)}"
            else:
                time_str = f"{hour}:xx"
        elif re.match(r"^\*/\d+$", hour):
            interval = hour.split("/")[1]
            time_str = f"alle {interval}h"
        else:
            time_str = "~variabel"

        # Handle day of week
        day_names = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]
        if dow != "*":
            try:
                day_num = int(dow)
                if 0 <= day_num <= 6:
                    return f"{day_names[day_num]} {time_str}"
                elif day_num == 7:
                    return f"{day_names[0]} {time_str}"
            except ValueError:
                pass
        elif re.match(r"^\d+$", day):
            return f"{day}. {time_str}"

        return time_str

    def find_job_properties(self) -> List[Path]:
        """Find all job.properties files."""
        pattern = str(self.gretl_jobs_dir / "**/job.properties")
        self.log(f"Searching for job.properties files in: {pattern}")

        try:
            files = [Path(f) for f in glob.glob(pattern, recursive=True)]
            self.log(f"Found {len(files)} job.properties files")
            return files
        except Exception as e:
            self.error(f"Error finding job.properties files: {e}")
            return []

    def extract_cte_names(self, sql_content: str) -> Set[str]:
        """Extract CTE names from SQL content."""
        cte_names = set()

        # Remove comments and strings
        clean_sql = sql_content
        clean_sql = re.sub(r"--[^\n]*", "", clean_sql)
        clean_sql = re.sub(r"/\*[\s\S]*?\*/", "", clean_sql)
        clean_sql = re.sub(r"'[^']*'", "''", clean_sql)
        clean_sql = re.sub(r'"[^"]*"', '""', clean_sql)

        # Match WITH clauses
        with_matches = re.findall(
            r"WITH\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+AS\s*\(", clean_sql, re.IGNORECASE
        )
        for match in with_matches:
            cte_names.add(match.lower())

        additional_cte_matches = re.findall(
            r",\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+AS\s*\(", clean_sql, re.IGNORECASE
        )
        for match in additional_cte_matches:
            cte_names.add(match.lower())

        self.log(f"Found CTEs: {', '.join(cte_names)}")
        return cte_names

    def analyze_sql_files(self, job_dir: Path) -> Dict[str, List[str]]:
        """Analyze SQL files for table access."""
        pattern = str(job_dir / "**/*.sql")

        try:
            sql_files = [Path(f) for f in glob.glob(pattern, recursive=True)]
            filtered_files = [
                f for f in sql_files if not f.name.startswith("searchindex_")
            ]

            source_tables = set()
            target_tables = set()

            for sql_file in filtered_files:
                try:
                    with open(sql_file, "r", encoding="utf-8") as f:
                        content = f.read()

                    cte_names = self.extract_cte_names(content)

                    # Find FROM tables
                    from_matches = re.findall(
                        r"FROM\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s*"
                        r"(?:AS\s+[a-zA-Z_][a-zA-Z0-9_]*)?",
                        content,
                        re.IGNORECASE,
                    )
                    for match in from_matches:
                        table = match.strip()
                        excluded_keywords = [
                            "AS",
                            "SELECT",
                            "WITH",
                            "WHERE",
                            "ORDER",
                            "GROUP",
                            "HAVING",
                        ]
                        if (
                            table.upper() not in excluded_keywords
                            and table.lower() not in cte_names
                        ):
                            source_tables.add(table)

                    # Find JOIN tables
                    join_matches = re.findall(
                        r"JOIN\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s*"
                        r"(?:AS\s+[a-zA-Z_][a-zA-Z0-9_]*)?",
                        content,
                        re.IGNORECASE,
                    )
                    for match in join_matches:
                        table = match.strip()
                        excluded_keywords = [
                            "AS",
                            "SELECT",
                            "WITH",
                            "WHERE",
                            "ORDER",
                            "GROUP",
                            "HAVING",
                        ]
                        if (
                            table.upper() not in excluded_keywords
                            and table.lower() not in cte_names
                        ):
                            source_tables.add(table)

                    # Find INSERT/UPDATE/CREATE tables
                    target_matches = re.findall(
                        r"(?:INSERT\s+INTO|UPDATE|CREATE\s+TABLE)\s+"
                        r"([a-zA-Z_][a-zA-Z0-9_.]*)",
                        content,
                        re.IGNORECASE,
                    )
                    for match in target_matches:
                        table = match.strip()
                        excluded_keywords = [
                            "AS",
                            "SELECT",
                            "WITH",
                            "WHERE",
                            "ORDER",
                            "GROUP",
                            "HAVING",
                        ]
                        if table.upper() not in excluded_keywords:
                            target_tables.add(table)

                except Exception as e:
                    self.error(f"Error reading SQL file {sql_file}: {e}")

            return {
                "sourceTables": sorted(list(source_tables)),
                "targetTables": sorted(list(target_tables)),
            }
        except Exception as e:
            self.error(f"Error analyzing SQL files in {job_dir}: {e}")
            return {"sourceTables": [], "targetTables": []}

    def analyze_jobs(self) -> List[Dict]:
        """Analyze all jobs."""
        job_files = self.find_job_properties()
        jobs = []

        for file_path in job_files:
            job_dir = file_path.parent
            job_name = job_dir.name

            self.log(f"Processing job: {job_name}")

            properties = self.parse_job_properties(file_path)
            cron_schedule = properties.get("triggers.cron")
            upstream = properties.get("triggers.upstream")

            status = (
                "Inaktiv"
                if (
                    properties.get("disabled") == "true"
                    or properties.get("enabled") == "false"
                )
                else "Aktiv"
            )

            if cron_schedule:
                trigger_type = "cron"
                trigger_value = cron_schedule
            elif upstream:
                trigger_type = "upstream"
                trigger_value = upstream
            else:
                trigger_type = "manual"
                trigger_value = "Manuell"

            sql_analysis = self.analyze_sql_files(job_dir)

            jobs.append(
                {
                    "name": job_name,
                    "path": str(job_dir),
                    "triggerType": trigger_type,
                    "triggerValue": trigger_value,
                    "cronSchedule": cron_schedule,
                    "upstream": upstream,
                    "status": status,
                    "sourceTables": sql_analysis["sourceTables"],
                    "targetTables": sql_analysis["targetTables"],
                    "sortKey": (
                        "1"
                        if trigger_type == "cron"
                        else ("2" if trigger_type == "upstream" else "3")
                    ),
                }
            )

        jobs.sort(key=lambda x: (x["sortKey"], x["name"].lower()))
        return jobs

    def get_amtsstelle_from_schema(self, schema: str) -> Optional[str]:
        """Get Amtsstelle description from schema name."""
        schema_mappings = {
            "agi": "Amt für Geoinformation",
            "afu": "Amt für Umwelt",
            "arp": "Amt für Raumplanung",
            "ada": "Amt für Denkmalpflege und Archäologie",
            "avt": "Amt für Verkehr und Tiefbau",
            "awjf": "Amt für Wald, Jagd und Fischerei",
            "alw": "Amt für Landwirtschaft",
            "so": "Kanton Solothurn",
        }

        prefix = schema.split("_")[0].lower()
        return schema_mappings.get(prefix)

    def cron_sort_key(self, cron_expression: str) -> str:
        """Generate sort key for cron expressions."""
        if not cron_expression:
            return "zzz"

        parts = cron_expression.split(" ")
        if len(parts) < 5:
            return cron_expression

        minute, hour, day, month, dow = parts[:5]

        hour_key = (
            "99"
            if hour == "H" or hour.startswith("H(")
            else hour.zfill(2) if hour.isdigit() else "50"
        )
        minute_key = (
            "99" if minute == "H" else minute.zfill(2) if minute.isdigit() else "50"
        )
        dow_key = "7" if dow == "*" else dow
        day_key = "99" if day == "*" else day.zfill(2)

        return f"{hour_key}_{minute_key}_{dow_key}_{day_key}"

    def generate_markdown(self, jobs: List[Dict]) -> str:
        """Generate markdown documentation."""
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
            "- [Manuelle Jobs](#manuelle-jobs)",
            "- [Schema-Übersicht](#schema-übersicht)",
            "",
            "---",
            "",
        ]

        cron_jobs = [job for job in jobs if job["triggerType"] == "cron"]
        upstream_jobs = [job for job in jobs if job["triggerType"] == "upstream"]
        manual_jobs = [job for job in jobs if job["triggerType"] == "manual"]

        cron_jobs.sort(key=lambda x: self.cron_sort_key(x["cronSchedule"]))

        # Zeitgesteuerte Jobs
        lines.extend(
            ["## Zeitgesteuerte Jobs (Cron)", "", f"**Anzahl:** {len(cron_jobs)}", ""]
        )

        if cron_jobs:
            lines.extend(
                [
                    "| Job | Status | Cron Schedule | Beschreibung |",
                    "|-----|--------|---------------|--------------|",
                ]
            )

            for job in cron_jobs:
                schedule_desc = self.cron_to_text(job["cronSchedule"])
                job_line = (
                    f"| {job['name']} | {job['status']} | "
                    f"`{job['cronSchedule']}` | {schedule_desc} |"
                )
                lines.append(job_line)
        else:
            lines.append("*Keine zeitgesteuerten Jobs gefunden.*")

        lines.extend(["", "---", ""])

        # Upstream Jobs
        lines.extend(
            ["## Upstream-gesteuerte Jobs", "", f"**Anzahl:** {len(upstream_jobs)}", ""]
        )

        if upstream_jobs:
            lines.extend(
                ["| Job | Status | Upstream Job |", "|-----|--------|--------------|"]
            )

            for job in upstream_jobs:
                job_line = f"| {job['name']} | {job['status']} | {job['upstream']} |"
                lines.append(job_line)
        else:
            lines.append("*Keine upstream-gesteuerten Jobs gefunden.*")

        lines.extend(["", "---", ""])

        # Manual Jobs
        lines.extend(["## Manuelle Jobs", "", f"**Anzahl:** {len(manual_jobs)}", ""])

        if manual_jobs:
            lines.extend(["| Job | Status |", "|-----|--------|"])

            for job in manual_jobs:
                job_line = f"| {job['name']} | {job['status']} |"
                lines.append(job_line)
        else:
            lines.append("*Keine manuellen Jobs gefunden.*")

        lines.extend(["", "---", ""])

        # Schema-Übersicht
        schemas = self.analyze_schemas(jobs)
        lines.extend(
            [
                "## Schema-Übersicht",
                "",
                f"**Anzahl Schemas:** {len(schemas)}",
                "",
                "| Schema | Beschreibung | Anzahl Jobs | Anzahl Tabellen |",
                "|--------|--------------|-------------|-----------------|",
            ]
        )

        for schema, info in sorted(schemas.items()):
            schema_line = (
                f"| {schema} | {info['description']} | "
                f"{len(info['jobs'])} | {len(info['tables'])} |"
            )
            lines.append(schema_line)

        lines.extend(["", "---", ""])

        # Detailierte Job-Informationen
        lines.extend(["## Detailierte Job-Informationen", ""])

        for job in jobs:
            lines.extend(
                [
                    f"### {job['name']}",
                    "",
                    f"**Status:** {job['status']}",
                    f"**Trigger:** {job['triggerType']}",
                    f"**Pfad:** `{job['path']}`",
                ]
            )

            if job["cronSchedule"]:
                schedule_line = (
                    f"**Schedule:** `{job['cronSchedule']}` "
                    f"({self.cron_to_text(job['cronSchedule'])})"
                )
                lines.append(schedule_line)

            if job["upstream"]:
                lines.append(f"**Upstream:** {job['upstream']}")

            if job["sourceTables"]:
                lines.extend(["", "**Quell-Tabellen:**"])
                for table in job["sourceTables"]:
                    lines.append(f"- {table}")

            if job["targetTables"]:
                lines.extend(["", "**Ziel-Tabellen:**"])
                for table in job["targetTables"]:
                    lines.append(f"- {table}")

            lines.extend(["", "---", ""])

        return "\n".join(lines)

    def analyze_schemas(self, jobs: List[Dict]) -> Dict[str, Dict]:
        """Analyze schemas used by jobs."""
        schemas = {}

        for job in jobs:
            all_tables = job["sourceTables"] + job["targetTables"]
            for table in all_tables:
                if "." in table:
                    schema = table.split(".")[0]

                    if schema not in schemas:
                        schemas[schema] = {
                            "description": self.get_amtsstelle_from_schema(schema)
                            or schema,
                            "jobs": set(),
                            "tables": set(),
                        }

                    schemas[schema]["jobs"].add(job["name"])
                    schemas[schema]["tables"].add(table)

        for schema in schemas:
            schemas[schema]["jobs"] = list(schemas[schema]["jobs"])
            schemas[schema]["tables"] = list(schemas[schema]["tables"])

        return schemas

    def run(self) -> None:
        """Main analysis function."""
        print("=== GRETL Jobs Dokumentation Generator (Python) ===")
        print(f"Analysiere Jobs in: {self.gretl_jobs_dir}")
        print(f"Ausgabedatei: {self.output_file}")

        if not self.path_exists(self.gretl_jobs_dir):
            self.error(f"GRETL Jobs directory not found: {self.gretl_jobs_dir}")
            sys.exit(1)

        try:
            jobs = self.analyze_jobs()

            if len(jobs) == 0:
                print("⚠️  No jobs found")
                return

            markdown = self.generate_markdown(jobs)

            with open(self.output_file, "w", encoding="utf-8") as f:
                f.write(markdown)

            print(f"✅ Documentation created: {self.output_file}")
            print(f"📊 Analyzed {len(jobs)} jobs")
            print(f"📄 Script completed successfully!")

        except Exception as e:
            self.error(f"Analysis failed: {e}")
            sys.exit(1)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze GRETL Jenkins jobs and generate documentation"
    )
    parser.add_argument(
        "--gretl-jobs-dir",
        default=os.environ.get("GRETL_JOBS_DIR", "../gretljobs"),
        help="Path to GRETL jobs directory (default: ../gretljobs)",
    )
    parser.add_argument(
        "--output-file",
        default=os.environ.get("OUTPUT_FILE", "GRETL_Jobs_Overview.md"),
        help="Output markdown file (default: GRETL_Jobs_Overview.md)",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=os.environ.get("DEBUG", "").lower() == "true",
        help="Enable debug output",
    )

    args = parser.parse_args()

    analyzer = GretlJobsAnalyzer(
        gretl_jobs_dir=args.gretl_jobs_dir,
        output_file=args.output_file,
        debug=args.debug,
    )

    analyzer.run()


if __name__ == "__main__":
    main()
