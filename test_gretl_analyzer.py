#!/usr/bin/env python3
"""
Test suite for GRETL Jobs Analyzer Python version
"""

import unittest
import tempfile
import shutil
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import sys

# Add the src directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from gretl_analyzer import GretlJobsAnalyzer


class TestGretlJobsAnalyzer(unittest.TestCase):
    """Test cases for GretlJobsAnalyzer."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir=str(self.test_dir),
            output_file=str(self.test_dir / 'test-output.md'),
            debug=False
        )

    def tearDown(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.test_dir)

    def test_constructor_with_default_options(self):
        """Test analyzer creation with default options."""
        default_analyzer = GretlJobsAnalyzer()
        self.assertEqual(str(default_analyzer.gretl_jobs_dir), '../gretljobs')
        self.assertEqual(str(default_analyzer.output_file), 'GRETL_Jobs_Overview.md')
        self.assertFalse(default_analyzer.debug)

    def test_path_exists(self):
        """Test path existence checking."""
        self.assertTrue(self.analyzer.path_exists(self.test_dir))
        self.assertFalse(self.analyzer.path_exists(Path('/nonexistent/path')))

    def test_parse_job_properties(self):
        """Test job properties parsing."""
        props_file = self.test_dir / 'job.properties'
        props_content = """# Comment line
triggers.cron=0 2 * * *
triggers.upstream=other_job
disabled=false
property.with.equals=value=with=equals
"""
        props_file.write_text(props_content.strip())

        result = self.analyzer.parse_job_properties(props_file)

        expected = {
            'triggers.cron': '0 2 * * *',
            'triggers.upstream': 'other_job',
            'disabled': 'false',
            'property.with.equals': 'value=with=equals'
        }
        self.assertEqual(result, expected)

    def test_parse_job_properties_with_empty_lines_and_comments(self):
        """Test parsing with empty lines and comments."""
        props_file = self.test_dir / 'job.properties'
        props_content = """
# This is a comment
key1=value1

# Another comment
key2=value2

"""
        props_file.write_text(props_content)

        result = self.analyzer.parse_job_properties(props_file)
        expected = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(result, expected)

    def test_parse_job_properties_nonexistent_file(self):
        """Test parsing nonexistent file."""
        nonexistent_file = self.test_dir / 'nonexistent.properties'
        result = self.analyzer.parse_job_properties(nonexistent_file)
        self.assertEqual(result, {})

    def test_cron_to_text_standard_time(self):
        """Test cron to text conversion for standard times."""
        self.assertEqual(self.analyzer.cron_to_text('0 6 * * *'), '06:00')
        self.assertEqual(self.analyzer.cron_to_text('30 14 * * *'), '14:30')
        self.assertEqual(self.analyzer.cron_to_text('0 0 * * *'), '00:00')
        self.assertEqual(self.analyzer.cron_to_text('15 8 15 * *'), '15. 08:15')

    def test_cron_to_text_jenkins_h_syntax(self):
        """Test Jenkins H syntax conversion."""
        self.assertEqual(self.analyzer.cron_to_text('H H * * *'), '~zufällig')
        self.assertEqual(self.analyzer.cron_to_text('H H(1-3) * * *'), '~1-3h')
        self.assertEqual(self.analyzer.cron_to_text('0 H(6-8) * * 1'), 'Mo ~6-8h')
        self.assertEqual(self.analyzer.cron_to_text('H 14 * * *'), '~14:xx')
        self.assertEqual(self.analyzer.cron_to_text('30 H * * *'), '~zufällig')

    def test_cron_to_text_intervals(self):
        """Test interval conversion."""
        self.assertEqual(self.analyzer.cron_to_text('0 */4 * * *'), 'alle 4h')
        self.assertEqual(self.analyzer.cron_to_text('0 */2 * * *'), 'alle 2h')
        self.assertEqual(self.analyzer.cron_to_text('*/15 * * * *'), '~variabel')

    def test_cron_to_text_days_of_week(self):
        """Test all days of week conversion."""
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 0'), 'So 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 1'), 'Mo 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 2'), 'Di 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 3'), 'Mi 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 4'), 'Do 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 5'), 'Fr 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 6'), 'Sa 09:00')
        self.assertEqual(self.analyzer.cron_to_text('0 9 * * 7'), 'So 09:00')

    def test_cron_to_text_edge_cases(self):
        """Test edge cases for cron conversion."""
        self.assertEqual(self.analyzer.cron_to_text(''), '-')
        self.assertEqual(self.analyzer.cron_to_text(None), '-')
        self.assertEqual(self.analyzer.cron_to_text('invalid'), 'invalid')
        self.assertEqual(self.analyzer.cron_to_text('0 2'), '0 2')
        self.assertEqual(self.analyzer.cron_to_text('complex H/2 * * *'), '~variabel')

    def test_find_job_properties(self):
        """Test finding job.properties files."""
        # Create test job directories
        job1_dir = self.test_dir / 'job1'
        job2_dir = self.test_dir / 'job2'
        job1_dir.mkdir()
        job2_dir.mkdir()

        # Create job.properties files
        (job1_dir / 'job.properties').write_text('triggers.cron=0 2 * * *')
        (job2_dir / 'job.properties').write_text('triggers.upstream=job1')

        files = self.analyzer.find_job_properties()
        self.assertEqual(len(files), 2)
        job_names = [f.parent.name for f in files]
        self.assertIn('job1', job_names)
        self.assertIn('job2', job_names)

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
        expected = {'temp_table', 'another_cte'}
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
        self.assertEqual(cte_names, {'test_cte'})

    def test_analyze_sql_files(self):
        """Test SQL file analysis."""
        # Create test job directory with SQL files
        job_dir = self.test_dir / 'test_job'
        job_dir.mkdir()

        sql_content = """
        WITH temp_cte AS (
            SELECT * FROM source_table
        )
        INSERT INTO target_table
        SELECT t.*, s.data
        FROM temp_cte t
        JOIN another_source s ON t.id = s.id
        """

        (job_dir / 'main.sql').write_text(sql_content)

        result = self.analyzer.analyze_sql_files(job_dir)

        # Should find source tables but not CTEs
        self.assertIn('source_table', result['sourceTables'])
        self.assertIn('another_source', result['sourceTables'])
        self.assertNotIn('temp_cte', result['sourceTables'])

        # Should find target table
        self.assertIn('target_table', result['targetTables'])

    def test_analyze_sql_files_ignores_searchindex(self):
        """Test that searchindex files are ignored."""
        job_dir = self.test_dir / 'test_job'
        job_dir.mkdir()

        # Create regular SQL file
        (job_dir / 'main.sql').write_text('SELECT * FROM test_table')

        # Create searchindex file (should be ignored)
        (job_dir / 'searchindex_something.sql').write_text('SELECT * FROM ignored_table')

        result = self.analyzer.analyze_sql_files(job_dir)

        self.assertIn('test_table', result['sourceTables'])
        self.assertNotIn('ignored_table', result['sourceTables'])

    def test_analyze_jobs(self):
        """Test job analysis."""
        # Create test jobs
        job1_dir = self.test_dir / 'cron_job'
        job2_dir = self.test_dir / 'upstream_job'
        job1_dir.mkdir()
        job2_dir.mkdir()

        # Create job.properties files
        (job1_dir / 'job.properties').write_text('triggers.cron=0 2 * * *\nstatus=active')
        (job2_dir / 'job.properties').write_text('triggers.upstream=cron_job\ndisabled=true')

        # Create SQL files
        (job1_dir / 'main.sql').write_text('INSERT INTO target1 SELECT * FROM source1')
        (job2_dir / 'main.sql').write_text('INSERT INTO target2 SELECT * FROM source2')

        jobs = self.analyzer.analyze_jobs()

        self.assertEqual(len(jobs), 2)

        # Check cron job
        cron_job = next(j for j in jobs if j['name'] == 'cron_job')
        self.assertEqual(cron_job['triggerType'], 'cron')
        self.assertEqual(cron_job['cronSchedule'], '0 2 * * *')
        self.assertEqual(cron_job['status'], 'Aktiv')

        # Check upstream job
        upstream_job = next(j for j in jobs if j['name'] == 'upstream_job')
        self.assertEqual(upstream_job['triggerType'], 'upstream')
        self.assertEqual(upstream_job['upstream'], 'cron_job')
        self.assertEqual(upstream_job['status'], 'Inaktiv')

    def test_get_amtsstelle_from_schema(self):
        """Test Amtsstelle mapping from schema."""
        self.assertEqual(self.analyzer.get_amtsstelle_from_schema('agi_av'), 'Amt für Geoinformation')
        self.assertEqual(self.analyzer.get_amtsstelle_from_schema('afu_gewaesser'), 'Amt für Umwelt')
        self.assertEqual(self.analyzer.get_amtsstelle_from_schema('arp_npl'), 'Amt für Raumplanung')
        self.assertEqual(self.analyzer.get_amtsstelle_from_schema('ada_denkmalpflege'), 'Amt für Denkmalpflege und Archäologie')
        self.assertEqual(self.analyzer.get_amtsstelle_from_schema('unknown_schema'), None)

    def test_analyze_schemas(self):
        """Test schema analysis."""
        jobs = [
            {
                'name': 'job1',
                'sourceTables': ['agi_av.table1', 'agi_av.table2'],
                'targetTables': ['afu_gewaesser.result']
            },
            {
                'name': 'job2',
                'sourceTables': ['agi_av.table1'],
                'targetTables': ['arp_npl.output']
            }
        ]

        schemas = self.analyzer.analyze_schemas(jobs)

        self.assertIn('agi_av', schemas)
        self.assertIn('afu_gewaesser', schemas)
        self.assertIn('arp_npl', schemas)

        # Check agi_av schema
        agi_schema = schemas['agi_av']
        self.assertEqual(agi_schema['description'], 'Amt für Geoinformation')
        self.assertEqual(set(agi_schema['jobs']), {'job1', 'job2'})
        self.assertEqual(len(agi_schema['tables']), 2)

    def test_generate_markdown(self):
        """Test markdown generation."""
        jobs = [
            {
                'name': 'test_job',
                'path': '/test/path',
                'triggerType': 'cron',
                'triggerValue': '0 2 * * *',
                'cronSchedule': '0 2 * * *',
                'upstream': None,
                'status': 'Aktiv',
                'sourceTables': ['source1', 'source2'],
                'targetTables': ['target1'],
                'sortKey': '1'
            }
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        self.assertIn('# GRETL Jobs Übersicht', markdown)
        self.assertIn('test_job', markdown)
        self.assertIn('02:00', markdown)
        self.assertIn('source1', markdown)
        self.assertIn('target1', markdown)

    def test_generate_markdown_with_upstream_job(self):
        """Test markdown generation with upstream job."""
        jobs = [
            {
                'name': 'upstream_job',
                'path': '/test/path',
                'triggerType': 'upstream',
                'triggerValue': 'parent_job',
                'cronSchedule': None,
                'upstream': 'parent_job',
                'status': 'Aktiv',
                'sourceTables': ['source1'],
                'targetTables': ['target1'],
                'sortKey': '2'
            }
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        self.assertIn('## Upstream-gesteuerte Jobs', markdown)
        self.assertIn('parent_job', markdown)

    def test_generate_markdown_with_no_tables(self):
        """Test markdown generation with jobs without tables."""
        jobs = [
            {
                'name': 'empty_job',
                'path': '/test/path',
                'triggerType': 'cron',
                'triggerValue': '0 2 * * *',
                'cronSchedule': '0 2 * * *',
                'upstream': None,
                'status': 'Aktiv',
                'sourceTables': [],
                'targetTables': [],
                'sortKey': '1'
            }
        ]

        markdown = self.analyzer.generate_markdown(jobs)

        self.assertIn('empty_job', markdown)
        # Should not show table information if no tables
        self.assertNotIn('**Quell-Tabellen**', markdown)
        self.assertNotIn('**Ziel-Tabellen**', markdown)

    @patch('sys.exit')
    def test_run_with_nonexistent_directory(self, mock_exit):
        """Test run method with nonexistent directory."""
        analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir='/definitely/nonexistent/path',
            output_file=str(self.test_dir / 'output.md')
        )

        with patch('builtins.print'):
            analyzer.run()

        mock_exit.assert_called_with(1)

    @patch('builtins.print')
    def test_run_with_no_jobs(self, mock_print):
        """Test run method with no jobs found."""
        self.analyzer.run()

        # Should print warning about no jobs
        mock_print.assert_any_call('⚠️  No jobs with triggers found')

    @patch('builtins.print')
    def test_run_success(self, mock_print):
        """Test successful run."""
        # Create test job
        job_dir = self.test_dir / 'test_job'
        job_dir.mkdir()
        (job_dir / 'job.properties').write_text('triggers.cron=0 2 * * *')

        self.analyzer.run()

        # Should print success message
        mock_print.assert_any_call('📄 Script completed successfully!')

        # Should create output file
        self.assertTrue(self.analyzer.output_file.exists())

    @patch('sys.exit')
    def test_run_with_write_error(self, mock_exit):
        """Test run method with write error."""
        # Create test job
        job_dir = self.test_dir / 'test_job'
        job_dir.mkdir()
        (job_dir / 'job.properties').write_text('triggers.cron=0 2 * * *')

        # Set output to readonly directory
        analyzer = GretlJobsAnalyzer(
            gretl_jobs_dir=str(self.test_dir),
            output_file='/readonly/path/output.md'
        )

        with patch('builtins.print'):
            analyzer.run()

        mock_exit.assert_called_with(1)


if __name__ == '__main__':
    unittest.main()
