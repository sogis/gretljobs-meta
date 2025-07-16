#!/usr/bin/env python3
"""
Test suite for GRETL Jobs Analyzer Python version
"""

import unittest
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import patch
import sys

# Add the src directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gretl_analyzer import GretlJobsAnalyzer


class TestGretlJobsAnalyzer(unittest.TestCase):
    """Test cases for GretlJobsAnalyzer."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir=str(self.test_dir),
            output_file=str(self.test_dir / "test-output.md"),
            debug=False,
        )

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.test_dir)

    def test_constructor_with_default_options(self):
        """Test analyzer creation with default options."""
        default_analyzer = GretlJobsAnalyzer()
        self.assertEqual(str(default_analyzer.gretl_jobs_dir), "../gretljobs")
        self.assertEqual(str(default_analyzer.output_file), "GRETL_Jobs_Overview.md")
        self.assertFalse(default_analyzer.debug)

    def test_path_exists(self):
        """Test path existence checking."""
        self.assertTrue(self.analyzer.path_exists(self.test_dir))
        self.assertFalse(self.analyzer.path_exists(Path("/nonexistent/path")))

    def test_parse_job_properties(self):
        """Test job properties parsing."""
        props_file = self.test_dir / "job.properties"
        props_content = """# Comment line
triggers.cron=0 2 * * *
triggers.upstream=other_job
disabled=false
property.with.equals=value=with=equals
"""
        props_file.write_text(props_content.strip())

        result = self.analyzer.parse_job_properties(props_file)

        expected = {
            "triggers.cron": "0 2 * * *",
            "triggers.upstream": "other_job",
            "disabled": "false",
            "property.with.equals": "value=with=equals",
        }
        self.assertEqual(result, expected)

    def test_parse_job_properties_with_empty_lines_and_comments(self):
        """Test parsing with empty lines and comments."""
        props_file = self.test_dir / "job.properties"
        props_content = """
# This is a comment
key1=value1

# Another comment
key2=value2

"""
        props_file.write_text(props_content)

        result = self.analyzer.parse_job_properties(props_file)
        expected = {"key1": "value1", "key2": "value2"}
        self.assertEqual(result, expected)

    def test_parse_job_properties_nonexistent_file(self):
        """Test parsing nonexistent file."""
        nonexistent_file = self.test_dir / "nonexistent.properties"
        result = self.analyzer.parse_job_properties(nonexistent_file)
        self.assertEqual(result, {})

    def test_cron_to_text_standard_time(self):
        """Test cron to text conversion for standard times."""
        self.assertEqual(self.analyzer.cron_to_text("0 6 * * *"), "06:00")
        self.assertEqual(self.analyzer.cron_to_text("30 14 * * *"), "14:30")
        self.assertEqual(self.analyzer.cron_to_text("0 0 * * *"), "00:00")
        self.assertEqual(self.analyzer.cron_to_text("15 8 15 * *"), "15. 08:15")

    def test_cron_to_text_jenkins_h_syntax(self):
        """Test Jenkins H syntax conversion."""
        self.assertEqual(self.analyzer.cron_to_text("H H * * *"), "~zufällig")
        self.assertEqual(self.analyzer.cron_to_text("H H(1-3) * * *"), "~1-3h")
        self.assertEqual(self.analyzer.cron_to_text("0 H(6-8) * * 1"), "Mo ~6-8h")
        self.assertEqual(self.analyzer.cron_to_text("H 14 * * *"), "~14:xx")
        self.assertEqual(self.analyzer.cron_to_text("30 H * * *"), "~zufällig")

    def test_cron_to_text_intervals(self):
        """Test interval conversion."""
        self.assertEqual(self.analyzer.cron_to_text("0 */4 * * *"), "alle 4h")
        self.assertEqual(self.analyzer.cron_to_text("0 */2 * * *"), "alle 2h")
        self.assertEqual(self.analyzer.cron_to_text("*/15 * * * *"), "~variabel")

    def test_cron_to_text_days_of_week(self):
        """Test all days of week conversion."""
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 0"), "So 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 1"), "Mo 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 2"), "Di 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 3"), "Mi 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 4"), "Do 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 5"), "Fr 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 6"), "Sa 09:00")
        self.assertEqual(self.analyzer.cron_to_text("0 9 * * 7"), "So 09:00")

    def test_cron_to_text_edge_cases(self):
        """Test edge cases for cron conversion."""
        self.assertEqual(self.analyzer.cron_to_text(""), "-")
        self.assertEqual(self.analyzer.cron_to_text(None), "-")
        self.assertEqual(self.analyzer.cron_to_text("invalid"), "invalid")
        self.assertEqual(self.analyzer.cron_to_text("0 2"), "0 2")
        self.assertEqual(self.analyzer.cron_to_text("complex H/2 * * *"), "~variabel")

    def test_find_job_properties(self):
        """Test finding job.properties files."""
        # Create test job directories
        job1_dir = self.test_dir / "job1"
        job2_dir = self.test_dir / "job2"
        job1_dir.mkdir()
        job2_dir.mkdir()

        # Create job.properties files
        (job1_dir / "job.properties").write_text("triggers.cron=0 2 * * *")
        (job2_dir / "job.properties").write_text("triggers.upstream=job1")

        files = self.analyzer.find_job_properties()
        self.assertEqual(len(files), 2)
        job_names = [f.parent.name for f in files]
        self.assertIn("job1", job_names)
        self.assertIn("job2", job_names)

    def test_find_job_properties_no_files(self):
        """Test handling directory without job.properties files."""
        files = self.analyzer.find_job_properties()
        self.assertEqual(len(files), 0)

    def test_extract_cte_names(self):
        """Test CTE name extraction."""
        sql_content = """
        WITH temp_table AS (
            SELECT * FROM source_table
        ),
        another_cte AS (
            SELECT * FROM temp_table
        )
        SELECT * FROM another_cte
        """

        cte_names = self.analyzer.extract_cte_names(sql_content)
        expected = {"temp_table", "another_cte"}
        self.assertEqual(cte_names, expected)

    def test_extract_cte_names_with_comments(self):
        """Test CTE extraction with comments."""
        sql_content = """
        -- This is a comment with WITH in it
        WITH /* comment */ test_cte AS (
            SELECT * FROM real_table
        )
        SELECT * FROM test_cte
        """

        cte_names = self.analyzer.extract_cte_names(sql_content)
        self.assertEqual(cte_names, {"test_cte"})

    def test_analyze_sql_files_improved_parsing(self):
        """Test improved SQL file analysis that avoids 'AS' problem."""
        job_dir = self.test_dir / "test_job"
        job_dir.mkdir()

        # SQL with potential 'AS' problem
        sql_content = """
        WITH temp_cte AS (
            SELECT * FROM source_table
        )
        INSERT INTO target_table
        SELECT t.*, s.data
        FROM temp_cte t
        JOIN another_source AS s ON t.id = s.id
        WHERE s.status = 'active'
        """

        (job_dir / "main.sql").write_text(sql_content)

        result = self.analyzer.analyze_sql_files(job_dir)

        # Should find source tables but not CTEs or keywords
        self.assertIn("source_table", result["sourceTables"])
        self.assertIn("another_source", result["sourceTables"])
        self.assertNotIn("temp_cte", result["sourceTables"])
        self.assertNotIn("AS", result["sourceTables"])
        self.assertNotIn("s", result["sourceTables"])

        # Should find target table
        self.assertIn("target_table", result["targetTables"])

        # Results should be sorted
        self.assertEqual(result["sourceTables"], sorted(result["sourceTables"]))
        self.assertEqual(result["targetTables"], sorted(result["targetTables"]))

    def test_analyze_sql_files_ignores_searchindex(self):
        """Test that searchindex files are ignored."""
        job_dir = self.test_dir / "test_job"
        job_dir.mkdir()

        # Create regular SQL file
        (job_dir / "main.sql").write_text("SELECT * FROM test_table")

        # Create searchindex file (should be ignored)
        (job_dir / "searchindex_something.sql").write_text(
            "SELECT * FROM ignored_table"
        )

        result = self.analyzer.analyze_sql_files(job_dir)

        self.assertIn("test_table", result["sourceTables"])
        self.assertNotIn("ignored_table", result["sourceTables"])

    def test_analyze_jobs(self):
        """Test job analysis - now analyzes ALL jobs, not just triggered ones."""
        # Create test jobs
        cron_job_dir = self.test_dir / "cron_job"
        upstream_job_dir = self.test_dir / "upstream_job"
        manual_job_dir = self.test_dir / "manual_job"

        cron_job_dir.mkdir()
        upstream_job_dir.mkdir()
        manual_job_dir.mkdir()

        # Create job.properties files
        cron_props = "triggers.cron=0 2 * * *\nstatus=active"
        upstream_props = "triggers.upstream=cron_job\ndisabled=true"
        manual_props = "description=Manual job\nstatus=active"

        (cron_job_dir / "job.properties").write_text(cron_props)
        (upstream_job_dir / "job.properties").write_text(upstream_props)
        (manual_job_dir / "job.properties").write_text(manual_props)

        # Create SQL files
        sql1 = "INSERT INTO target1 SELECT * FROM source1"
        sql2 = "INSERT INTO target2 SELECT * FROM source2"
        sql3 = "INSERT INTO target3 SELECT * FROM source3"

        (cron_job_dir / "main.sql").write_text(sql1)
        (upstream_job_dir / "main.sql").write_text(sql2)
        (manual_job_dir / "main.sql").write_text(sql3)

        jobs = self.analyzer.analyze_jobs()

        # Should find ALL jobs now, not just triggered ones
        self.assertEqual(len(jobs), 3)

        # Check cron job
        cron_job = next(j for j in jobs if j["name"] == "cron_job")
        self.assertEqual(cron_job["triggerType"], "cron")
        self.assertEqual(cron_job["cronSchedule"], "0 2 * * *")
        self.assertEqual(cron_job["status"], "Aktiv")

        # Check upstream job
        upstream_job = next(j for j in jobs if j["name"] == "upstream_job")
        self.assertEqual(upstream_job["triggerType"], "upstream")
        self.assertEqual(upstream_job["upstream"], "cron_job")
        self.assertEqual(upstream_job["status"], "Inaktiv")

        # Check manual job (NEW)
        manual_job = next(j for j in jobs if j["name"] == "manual_job")
        self.assertEqual(manual_job["triggerType"], "manual")
        self.assertEqual(manual_job["triggerValue"], "Manuell")
        self.assertEqual(manual_job["status"], "Aktiv")
        self.assertIsNone(manual_job["cronSchedule"])
        self.assertIsNone(manual_job["upstream"])

    def test_get_amtsstelle_from_schema(self):
        """Test Amtsstelle mapping from schema."""
        self.assertEqual(
            self.analyzer.get_amtsstelle_from_schema("agi_av"), "Amt für Geoinformation"
        )
        self.assertEqual(
            self.analyzer.get_amtsstelle_from_schema("afu_gewaesser"), "Amt für Umwelt"
        )
        self.assertEqual(
            self.analyzer.get_amtsstelle_from_schema("arp_npl"), "Amt für Raumplanung"
        )
        self.assertEqual(
            self.analyzer.get_amtsstelle_from_schema("ada_denkmalpflege"),
            "Amt für Denkmalpflege und Archäologie",
        )
        self.assertEqual(
            self.analyzer.get_amtsstelle_from_schema("unknown_schema"), None
        )

    def test_analyze_schemas(self):
        """Test schema analysis."""
        jobs = [
            {
                "name": "job1",
                "sourceTables": ["agi_av.table1", "agi_av.table2"],
                "targetTables": ["afu_gewaesser.result"],
            },
            {
                "name": "job2",
                "sourceTables": ["agi_av.table1"],
                "targetTables": ["arp_npl.output"],
            },
        ]

        schemas = self.analyzer.analyze_schemas(jobs)

        self.assertIn("agi_av", schemas)
        self.assertIn("afu_gewaesser", schemas)
        self.assertIn("arp_npl", schemas)

        # Check agi_av schema
        agi_schema = schemas["agi_av"]
        self.assertEqual(agi_schema["description"], "Amt für Geoinformation")
        self.assertEqual(set(agi_schema["jobs"]), {"job1", "job2"})
        self.assertEqual(len(agi_schema["tables"]), 2)

    def test_cron_sort_key(self):
        """Test cron sort key generation."""
        # Test various cron expressions
        self.assertEqual(self.analyzer.cron_sort_key("0 2 * * *"), "02_00_7_99")
        self.assertEqual(self.analyzer.cron_sort_key("30 14 * * *"), "14_30_7_99")
        self.assertEqual(self.analyzer.cron_sort_key("H H * * *"), "99_99_7_99")
        self.assertEqual(self.analyzer.cron_sort_key("0 */4 * * *"), "50_00_7_99")
        self.assertEqual(self.analyzer.cron_sort_key("0 9 * * 1"), "09_00_1_99")
        self.assertEqual(self.analyzer.cron_sort_key(""), "zzz")
        self.assertEqual(self.analyzer.cron_sort_key("invalid"), "invalid")

    def test_generate_markdown_improved(self):
        """Test improved markdown generation with all job types."""
        jobs = [
            {
                "name": "cron_job",
                "path": "/test/path1",
                "triggerType": "cron",
                "triggerValue": "0 2 * * *",
                "cronSchedule": "0 2 * * *",
                "upstream": None,
                "status": "Aktiv",
                "sourceTables": ["source1", "source2"],
                "targetTables": ["target1"],
                "sortKey": "1",
            },
            {
                "name": "upstream_job",
                "path": "/test/path2",
                "triggerType": "upstream",
                "triggerValue": "cron_job",
                "cronSchedule": None,
                "upstream": "cron_job",
                "status": "Aktiv",
                "sourceTables": ["source3"],
                "targetTables": ["target2"],
                "sortKey": "2",
            },
            {
                "name": "manual_job",
                "path": "/test/path3",
                "triggerType": "manual",
                "triggerValue": "Manuell",
                "cronSchedule": None,
                "upstream": None,
                "status": "Aktiv",
                "sourceTables": ["source4"],
                "targetTables": ["target3"],
                "sortKey": "3",
            },
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        # Check all sections are present
        self.assertIn("# GRETL Jobs Übersicht", markdown)
        self.assertIn("## Zeitgesteuerte Jobs (Cron)", markdown)
        self.assertIn("## Upstream-gesteuerte Jobs", markdown)
        self.assertIn("## Manuelle Jobs", markdown)

        # Check cron job formatting
        self.assertIn("`0 2 * * *`", markdown)  # Code formatting
        self.assertIn("02:00", markdown)  # Description

        # Check that tables are NOT in overview sections
        overview_part = markdown.split("## Detailierte Job-Informationen")[0]
        self.assertNotIn("source1", overview_part)

        # Check that tables ARE in detailed section
        detailed_section = markdown.split("## Detailierte Job-Informationen")[1]
        self.assertIn("source1", detailed_section)
        self.assertIn("target1", detailed_section)

    def test_generate_markdown_with_manual_jobs(self):
        """Test markdown generation with manual jobs."""
        jobs = [
            {
                "name": "manual_job",
                "path": "/test/path",
                "triggerType": "manual",
                "triggerValue": "Manuell",
                "cronSchedule": None,
                "upstream": None,
                "status": "Aktiv",
                "sourceTables": [],
                "targetTables": [],
                "sortKey": "3",
            }
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        self.assertIn("## Manuelle Jobs", markdown)
        self.assertIn("manual_job", markdown)
        # Should not show table information in overview
        overview_part = markdown.split("## Detailierte Job-Informationen")[0]
        self.assertNotIn("**Quell-Tabellen**", overview_part)

    @patch("sys.exit")
    def test_run_with_nonexistent_directory(self, mock_exit):
        """Test run method with nonexistent directory."""
        analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir="/definitely/nonexistent/path",
            output_file=str(self.test_dir / "output.md"),
        )

        with patch("builtins.print"):
            analyzer.run()


if __name__ == "__main__":
    unittest.main()

    @patch("builtins.print")
    def test_run_with_no_jobs(self, mock_print):
        """Test run method with no jobs found."""
        self.analyzer.run()

        # Should print warning about no jobs (updated message)
        mock_print.assert_any_call("⚠️  No jobs found")

    @patch("builtins.print")
    def test_run_success(self, mock_print):
        """Test successful run."""
        # Create test job
        job_dir = self.test_dir / "test_job"
        job_dir.mkdir()
        (job_dir / "job.properties").write_text("triggers.cron=0 2 * * *")

        self.analyzer.run()

        # Should print success message
        mock_print.assert_any_call("📄 Script completed successfully!")

        # Should create output file
        self.assertTrue(self.analyzer.output_file.exists())

    def test_analyze_jobs_sorting(self):
        """Test that jobs are sorted correctly by type and name."""
        # Create test jobs in reverse alphabetical order
        z_cron_dir = self.test_dir / "z_cron_job"
        a_upstream_dir = self.test_dir / "a_upstream_job"
        m_manual_dir = self.test_dir / "m_manual_job"

        z_cron_dir.mkdir()
        a_upstream_dir.mkdir()
        m_manual_dir.mkdir()

        (z_cron_dir / "job.properties").write_text("triggers.cron=0 2 * * *")
        (a_upstream_dir / "job.properties").write_text("triggers.upstream=z_cron_job")
        (m_manual_dir / "job.properties").write_text("description=Manual job")

        jobs = self.analyzer.analyze_jobs()

        # Should be sorted by sortKey (cron=1, upstream=2, manual=3) then by name
        self.assertEqual(jobs[0]["triggerType"], "cron")
        self.assertEqual(jobs[1]["triggerType"], "upstream")
        self.assertEqual(jobs[2]["triggerType"], "manual")

        # Check sort keys
        self.assertEqual(jobs[0]["sortKey"], "1")
        self.assertEqual(jobs[1]["sortKey"], "2")
        self.assertEqual(jobs[2]["sortKey"], "3")

    def test_cron_schedule_sorting_in_markdown(self):
        """Test that cron jobs are sorted by schedule in markdown output."""
        jobs = [
            {
                "name": "late_job",
                "triggerType": "cron",
                "cronSchedule": "0 23 * * *",
                "status": "Aktiv",
                "sourceTables": [],
                "targetTables": [],
                "path": "/test",
                "triggerValue": "0 23 * * *",
                "upstream": None,
                "sortKey": "1",
            },
            {
                "name": "early_job",
                "triggerType": "cron",
                "cronSchedule": "0 1 * * *",
                "status": "Aktiv",
                "sourceTables": [],
                "targetTables": [],
                "path": "/test",
                "triggerValue": "0 1 * * *",
                "upstream": None,
                "sortKey": "1",
            },
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        # Check that early_job appears before late_job in the markdown
        early_pos = markdown.find("early_job")
        late_pos = markdown.find("late_job")
        self.assertLess(early_pos, late_pos)

    @patch("sys.exit")
    def test_run_with_write_error(self, mock_exit):
        """Test run method with write error."""
        # Create test job
        job_dir = self.test_dir / "test_job"
        job_dir.mkdir()
        (job_dir / "job.properties").write_text("triggers.cron=0 2 * * *")

        # Set output to readonly directory
        analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir=str(self.test_dir), output_file="/readonly/path/output.md"
        )

        with patch("builtins.print"):
            analyzer.run()

        mock_exit.assert_called_with(1)
