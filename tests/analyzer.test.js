// tests/analyzer.test.js
const GretlJobsAnalyzer = require('../src/analyzer');
const fs = require('fs').promises;
const fsSync = require('fs');
const path = require('path');
const os = require('os');

describe('GretlJobsAnalyzer', () => {
  let analyzer;
  let testDir;

  beforeEach(async () => {
    testDir = await fs.mkdtemp(path.join(os.tmpdir(), 'gretl-test-'));
    analyzer = new GretlJobsAnalyzer({
      gretlJobsDir: testDir,
      outputFile: path.join(testDir, 'test-output.md'),
      debug: false
    });
  });

  afterEach(async () => {
    await fs.rm(testDir, { recursive: true, force: true });
  });

  describe('constructor and basic methods', () => {
    it('should create analyzer with default options', () => {
      const defaultAnalyzer = new GretlJobsAnalyzer();
      expect(defaultAnalyzer.gretlJobsDir).toBe('../gretljobs');
      expect(defaultAnalyzer.outputFile).toBe('GRETL_Jobs_Overview.md');
      expect(defaultAnalyzer.debug).toBe(false);
    });

    it('should log debug messages when debug is enabled', () => {
      const debugAnalyzer = new GretlJobsAnalyzer({ debug: true });
      const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

      debugAnalyzer.log('test message');
      expect(consoleSpy).toHaveBeenCalledWith('[DEBUG] test message');

      consoleSpy.mockRestore();
    });

    it('should not log when debug is disabled', () => {
      const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

      analyzer.log('test message');
      expect(consoleSpy).not.toHaveBeenCalled();

      consoleSpy.mockRestore();
    });

    it('should log error messages', () => {
      const consoleSpy = jest.spyOn(console, 'error').mockImplementation();

      analyzer.error('test error');
      expect(consoleSpy).toHaveBeenCalledWith('[ERROR] test error');

      consoleSpy.mockRestore();
    });
  });

  describe('pathExists', () => {
    it('should return true for existing path', async () => {
      const result = await analyzer.pathExists(testDir);
      expect(result).toBe(true);
    });

    it('should return false for non-existing path', async () => {
      const result = await analyzer.pathExists('/nonexistent/path');
      expect(result).toBe(false);
    });
  });

  describe('parseJobProperties', () => {
    it('should parse job properties correctly', async () => {
      const propsFile = path.join(testDir, 'job.properties');
      await fs.writeFile(propsFile, `
# Comment line
triggers.cron=0 2 * * *
triggers.upstream=other_job
disabled=false
property.with.equals=value=with=equals
      `.trim());

      const result = analyzer.parseJobProperties(propsFile);

      expect(result).toEqual({
        'triggers.cron': '0 2 * * *',
        'triggers.upstream': 'other_job',
        'disabled': 'false',
        'property.with.equals': 'value=with=equals'
      });
    });

    it('should handle empty lines and comments', async () => {
      const propsFile = path.join(testDir, 'job.properties');
      await fs.writeFile(propsFile, `
# This is a comment
# Another comment

triggers.cron=0 2 * * *

# Empty line above
triggers.upstream=other_job
      `.trim());

      const result = analyzer.parseJobProperties(propsFile);

      expect(result).toEqual({
        'triggers.cron': '0 2 * * *',
        'triggers.upstream': 'other_job'
      });
    });

    it('should handle malformed lines gracefully', async () => {
      const propsFile = path.join(testDir, 'job.properties');
      await fs.writeFile(propsFile, `
triggers.cron=0 2 * * *
malformed_line_without_equals
=value_without_key
key_without_value=
triggers.upstream=other_job
      `.trim());

      const result = analyzer.parseJobProperties(propsFile);

      expect(result).toEqual({
        'triggers.cron': '0 2 * * *',
        'key_without_value': '',
        'triggers.upstream': 'other_job'
      });
    });

    it('should handle empty or malformed files gracefully', () => {
      const originalError = console.error;
      console.error = jest.fn();

      const result = analyzer.parseJobProperties('/nonexistent/file.properties');
      expect(result).toEqual({});

      console.error = originalError;
    });
  });

  describe('cronToText', () => {
    it('should convert standard cron expressions', () => {
      expect(analyzer.cronToText('0 2 * * *')).toBe('02:00');
      expect(analyzer.cronToText('30 14 * * *')).toBe('14:30');
      expect(analyzer.cronToText('0 6 * * 1')).toBe('Mo 06:00');
      expect(analyzer.cronToText('0 0 1 * *')).toBe('1. 00:00');
      expect(analyzer.cronToText('15 8 15 * *')).toBe('15. 08:15');
    });

    it('should handle Jenkins H syntax', () => {
      expect(analyzer.cronToText('H H * * *')).toBe('~zufällig');
      expect(analyzer.cronToText('H H(1-3) * * *')).toBe('~1-3h');
      expect(analyzer.cronToText('0 H(6-8) * * 1')).toBe('Mo ~6-8h');
      expect(analyzer.cronToText('H 14 * * *')).toBe('~14:xx');
      expect(analyzer.cronToText('30 H * * *')).toBe('~zufällig');
    });

    it('should handle intervals', () => {
      expect(analyzer.cronToText('0 */4 * * *')).toBe('alle 4h');
      expect(analyzer.cronToText('0 */2 * * *')).toBe('alle 2h');
      expect(analyzer.cronToText('*/15 * * * *')).toBe('~variabel');
    });

    it('should handle all days of week', () => {
      expect(analyzer.cronToText('0 9 * * 0')).toBe('So 09:00');
      expect(analyzer.cronToText('0 9 * * 1')).toBe('Mo 09:00');
      expect(analyzer.cronToText('0 9 * * 2')).toBe('Di 09:00');
      expect(analyzer.cronToText('0 9 * * 3')).toBe('Mi 09:00');
      expect(analyzer.cronToText('0 9 * * 4')).toBe('Do 09:00');
      expect(analyzer.cronToText('0 9 * * 5')).toBe('Fr 09:00');
      expect(analyzer.cronToText('0 9 * * 6')).toBe('Sa 09:00');
      expect(analyzer.cronToText('0 9 * * 7')).toBe('So 09:00');
    });

    it('should handle edge cases', () => {
      expect(analyzer.cronToText('')).toBe('-');
      expect(analyzer.cronToText(null)).toBe('-');
      expect(analyzer.cronToText(undefined)).toBe('-');
      expect(analyzer.cronToText('invalid')).toBe('invalid');
      expect(analyzer.cronToText('0 2')).toBe('0 2');
      expect(analyzer.cronToText('complex H/2 * * *')).toBe('~variabel');
    });
  });

  describe('findJobProperties', () => {
    it('should find job.properties files', async () => {
      const job1Dir = path.join(testDir, 'job1');
      const job2Dir = path.join(testDir, 'job2');

      await fs.mkdir(job1Dir, { recursive: true });
      await fs.mkdir(job2Dir, { recursive: true });

      await fs.writeFile(path.join(job1Dir, 'job.properties'), 'triggers.cron=0 2 * * *');
      await fs.writeFile(path.join(job2Dir, 'job.properties'), 'triggers.upstream=job1');

      const files = await analyzer.findJobProperties();
      expect(files).toHaveLength(2);
      expect(files.some(f => f.includes('job1'))).toBe(true);
      expect(files.some(f => f.includes('job2'))).toBe(true);
    });

    it('should handle directory without job.properties files', async () => {
      const files = await analyzer.findJobProperties();
      expect(files).toHaveLength(0);
    });

    it('should handle glob errors gracefully', async () => {
      const analyzerWithBadPath = new GretlJobsAnalyzer({
        gretlJobsDir: '/definitely/nonexistent/path'
      });

      const originalError = console.error;
      console.error = jest.fn();

      const files = await analyzerWithBadPath.findJobProperties();
      expect(files).toHaveLength(0);

      console.error = originalError;
    });
  });

  describe('analyzeSqlFiles', () => {
    it('should analyze SQL files correctly', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.mkdir(jobDir, { recursive: true });

      const sqlContent = `
        SELECT * FROM source_table1 st1
        JOIN source_table2 st2 ON st1.id = st2.id
        LEFT JOIN source_table3 st3 ON st2.id = st3.id
        INNER JOIN source_table4 st4 ON st3.id = st4.id;

        INSERT INTO target_table1 (col1, col2)
        VALUES ('test', 'value');

        UPDATE target_table2
        SET status = 'processed';

        CREATE TABLE target_table3 (id INT);
      `;

      await fs.writeFile(path.join(jobDir, 'query.sql'), sqlContent);

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toContain('source_table1');
      expect(result.sourceTables).toContain('source_table2');
      expect(result.sourceTables).toContain('source_table3');
      expect(result.sourceTables).toContain('source_table4');
      expect(result.targetTables).toContain('target_table1');
      expect(result.targetTables).toContain('target_table2');
      expect(result.targetTables).toContain('target_table3');
    });

    it('should ignore CTE names in SQL analysis', async () => {
      const jobDir = path.join(testDir, 'test-job-with-cte');
      await fs.mkdir(jobDir, { recursive: true });

      const sqlContent = `
        WITH filtered_data AS (
          SELECT * FROM real_source_table
          WHERE status = 'active'
        ),
        aggregated_data AS (
          SELECT category, COUNT(*) as count
          FROM filtered_data
          GROUP BY category
        )
        SELECT
          ad.category,
          ad.count,
          rst.details
        FROM aggregated_data ad
        JOIN real_source_table rst ON ad.category = rst.category
        LEFT JOIN another_real_table art ON rst.id = art.ref_id;

        INSERT INTO target_table (category, count, details)
        SELECT category, count, details FROM aggregated_data;
      `;

      await fs.writeFile(path.join(jobDir, 'cte_query.sql'), sqlContent);

      const result = await analyzer.analyzeSqlFiles(jobDir);

      // Should include real tables
      expect(result.sourceTables).toContain('real_source_table');
      expect(result.sourceTables).toContain('another_real_table');
      expect(result.targetTables).toContain('target_table');

      // Should NOT include CTE names
      expect(result.sourceTables).not.toContain('filtered_data');
      expect(result.sourceTables).not.toContain('aggregated_data');
    });

    it('should handle complex CTEs with comments', async () => {
      const jobDir = path.join(testDir, 'test-job-complex-cte');
      await fs.mkdir(jobDir, { recursive: true });

      const sqlContent = `
        -- This is a complex query with CTEs
        WITH
        /* Multi-line comment
           with CTE description */
        sales_data AS (
          SELECT * FROM sales_table -- Real table
          WHERE year = 2024
        ),
        -- Another CTE
        monthly_summary AS (
          SELECT
            month,
            SUM(amount) as total
          FROM sales_data
          GROUP BY month
        )
        /* Final query */
        SELECT
          ms.month,
          ms.total,
          pt.product_name
        FROM monthly_summary ms
        JOIN product_table pt ON ms.product_id = pt.id;
      `;

      await fs.writeFile(path.join(jobDir, 'complex_cte.sql'), sqlContent);

      const result = await analyzer.analyzeSqlFiles(jobDir);

      // Should include real tables
      expect(result.sourceTables).toContain('sales_table');
      expect(result.sourceTables).toContain('product_table');

      // Should NOT include CTE names
      expect(result.sourceTables).not.toContain('sales_data');
      expect(result.sourceTables).not.toContain('monthly_summary');
    });

    it('should ignore searchindex SQL files', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.mkdir(jobDir, { recursive: true });

      await fs.writeFile(path.join(jobDir, 'searchindex_create.sql'), 'CREATE TABLE searchindex_table (id INT);');
      await fs.writeFile(path.join(jobDir, 'normal.sql'), 'SELECT * FROM normal_table;');

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toContain('normal_table');
      expect(result.sourceTables).not.toContain('searchindex_table');
      expect(result.targetTables).not.toContain('searchindex_table');
    });

    it('should handle directories without SQL files', async () => {
      const jobDir = path.join(testDir, 'empty-job');
      await fs.mkdir(jobDir, { recursive: true });

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toHaveLength(0);
      expect(result.targetTables).toHaveLength(0);
    });

    it('should handle SQL file read errors', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.mkdir(jobDir, { recursive: true });

      // Create file but then make it unreadable
      const sqlFile = path.join(jobDir, 'query.sql');
      await fs.writeFile(sqlFile, 'SELECT * FROM test_table;');
      await fs.chmod(sqlFile, 0o000);

      const originalError = console.error;
      console.error = jest.fn();

      const result = await analyzer.analyzeSqlFiles(jobDir);

      // Should handle error gracefully
      expect(result.sourceTables).toHaveLength(0);
      expect(result.targetTables).toHaveLength(0);

      // Restore permissions for cleanup
      await fs.chmod(sqlFile, 0o644);
      console.error = originalError;
    });

    it('should handle glob pattern errors', async () => {
      const originalError = console.error;
      console.error = jest.fn();

      const result = await analyzer.analyzeSqlFiles('/nonexistent/path');

      expect(result.sourceTables).toHaveLength(0);
      expect(result.targetTables).toHaveLength(0);

      console.error = originalError;
    });
  });

  describe('extractCteNames', () => {
    it('should extract CTE names correctly', () => {
      const sqlContent = `
        WITH filtered_data AS (
          SELECT * FROM source_table
        ),
        summary_data AS (
          SELECT category, COUNT(*) FROM filtered_data GROUP BY category
        )
        SELECT * FROM summary_data;
      `;

      const cteNames = analyzer.extractCteNames(sqlContent);

      expect(cteNames.has('filtered_data')).toBe(true);
      expect(cteNames.has('summary_data')).toBe(true);
      expect(cteNames.size).toBe(2);
    });

    it('should handle CTEs with comments and strings', () => {
      const sqlContent = `
        -- Comment with 'fake_cte' in string
        WITH /* comment */ real_cte AS (
          SELECT 'WITH fake_string AS' FROM table1
        ),
        another_cte AS ( -- another comment
          SELECT "WITH quoted_fake" FROM table2
        )
        SELECT * FROM real_cte JOIN another_cte;
      `;

      const cteNames = analyzer.extractCteNames(sqlContent);

      expect(cteNames.has('real_cte')).toBe(true);
      expect(cteNames.has('another_cte')).toBe(true);
      expect(cteNames.has('fake_string')).toBe(false);
      expect(cteNames.has('quoted_fake')).toBe(false);
      expect(cteNames.size).toBe(2);
    });

    it('should handle empty or no CTEs', () => {
      const sqlContent = `
        SELECT * FROM regular_table
        WHERE column = 'value';
      `;

      const cteNames = analyzer.extractCteNames(sqlContent);

      expect(cteNames.size).toBe(0);
    });
  });

  describe('analyzeJobs', () => {
    it('should find and analyze jobs correctly', async () => {
      const job1Dir = path.join(testDir, 'job1');
      const job2Dir = path.join(testDir, 'job2');

      await fs.mkdir(job1Dir, { recursive: true });
      await fs.mkdir(job2Dir, { recursive: true });

      await fs.writeFile(path.join(job1Dir, 'job.properties'), 'triggers.cron=0 2 * * *');
      await fs.writeFile(path.join(job1Dir, 'query.sql'), 'SELECT * FROM test_table;');

      await fs.writeFile(path.join(job2Dir, 'job.properties'), 'triggers.upstream=job1');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(2);
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[0].cronSchedule).toBe('0 2 * * *');
      expect(jobs[1].triggerType).toBe('upstream');
      expect(jobs[1].upstream).toBe('job1');
    });

    it('should handle disabled jobs', async () => {
      const jobDir = path.join(testDir, 'disabled-job');
      await fs.mkdir(jobDir, { recursive: true });

      await fs.writeFile(path.join(jobDir, 'job.properties'), `
triggers.cron=0 2 * * *
disabled=true
      `.trim());

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(1);
      expect(jobs[0].status).toBe('Inaktiv');
    });

    it('should handle jobs with enabled=false', async () => {
      const jobDir = path.join(testDir, 'enabled-false-job');
      await fs.mkdir(jobDir, { recursive: true });

      await fs.writeFile(path.join(jobDir, 'job.properties'), `
triggers.cron=0 2 * * *
enabled=false
      `.trim());

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(1);
      expect(jobs[0].status).toBe('Inaktiv');
    });

    it('should skip jobs without triggers', async () => {
      const jobDir = path.join(testDir, 'job-without-triggers');
      await fs.mkdir(jobDir, { recursive: true });
      await fs.writeFile(path.join(jobDir, 'job.properties'), 'some.other.property=value');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(0);
    });

    it('should sort jobs correctly', async () => {
      const job1Dir = path.join(testDir, 'zzz-job');
      const job2Dir = path.join(testDir, 'aaa-job');
      const job3Dir = path.join(testDir, 'upstream-job');

      await fs.mkdir(job1Dir, { recursive: true });
      await fs.mkdir(job2Dir, { recursive: true });
      await fs.mkdir(job3Dir, { recursive: true });

      await fs.writeFile(path.join(job1Dir, 'job.properties'), 'triggers.cron=0 23 * * *');
      await fs.writeFile(path.join(job2Dir, 'job.properties'), 'triggers.cron=0 1 * * *');
      await fs.writeFile(path.join(job3Dir, 'job.properties'), 'triggers.upstream=aaa-job');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(3);
      expect(jobs[0].name).toBe('aaa-job'); // Cron jobs first, sorted by schedule
      expect(jobs[1].name).toBe('zzz-job');
      expect(jobs[2].name).toBe('upstream-job'); // Upstream jobs last
    });
  });

  describe('generateMarkdown', () => {
    it('should generate valid markdown for cron jobs', () => {
      const jobs = [
        {
          name: 'test-job',
          path: '/test/path',
          triggerType: 'cron',
          cronSchedule: '0 2 * * *',
          status: 'Aktiv',
          sourceTables: ['source_table'],
          targetTables: ['target_table'],
          sortKey: '1_0 2 * * *_test-job'
        }
      ];

      const markdown = analyzer.generateMarkdown(jobs);

      expect(markdown).toContain('# GRETL Jobs Übersicht');
      expect(markdown).toContain('| test-job | Cron |');
      expect(markdown).toContain('### test-job');
      expect(markdown).toContain('source_table');
      expect(markdown).toContain('target_table');
      expect(markdown).toContain('02:00');
    });

    it('should generate valid markdown for upstream jobs', () => {
      const jobs = [
        {
          name: 'upstream-job',
          path: '/test/path',
          triggerType: 'upstream',
          upstream: 'parent-job',
          status: 'Aktiv',
          sourceTables: [],
          targetTables: [],
          sortKey: '2_upstream_upstream-job'
        }
      ];

      const markdown = analyzer.generateMarkdown(jobs);

      expect(markdown).toContain('| upstream-job | Upstream | parent-job |');
      expect(markdown).toContain('### upstream-job');
      expect(markdown).toContain('**Upstream-Trigger**: parent-job');
    });

    it('should generate table frequency analysis', () => {
      const jobs = [
        {
          name: 'job1',
          path: '/path1',
          triggerType: 'cron',
          cronSchedule: '0 2 * * *',
          status: 'Aktiv',
          sourceTables: ['common.table', 'schema1.table1'],
          targetTables: ['common.table'],
          sortKey: '1'
        },
        {
          name: 'job2',
          path: '/path2',
          triggerType: 'cron',
          cronSchedule: '0 3 * * *',
          status: 'Aktiv',
          sourceTables: ['common.table'],
          targetTables: ['schema2.table2'],
          sortKey: '2'
        }
      ];

      const markdown = analyzer.generateMarkdown(jobs);

      expect(markdown).toContain('## Häufig verwendete Tabellen');
      expect(markdown).toContain('| 3 | table | common |'); // common.table used 3 times
    });

    it('should handle jobs without tables', () => {
      const jobs = [
        {
          name: 'empty-job',
          path: '/test/path',
          triggerType: 'cron',
          cronSchedule: '0 2 * * *',
          status: 'Aktiv',
          sourceTables: [],
          targetTables: [],
          sortKey: '1'
        }
      ];

      const markdown = analyzer.generateMarkdown(jobs);

      expect(markdown).toContain('### empty-job');
      expect(markdown).not.toContain('**Quell-Tabellen**');
      expect(markdown).not.toContain('**Ziel-Tabellen**');
    });
  });

  describe('run method', () => {
    it('should exit with error if directory does not exist', async () => {
      const analyzerWithBadPath = new GretlJobsAnalyzer({
        gretlJobsDir: '/definitely/nonexistent/path',
        outputFile: path.join(testDir, 'output.md')
      });

      const originalExit = process.exit;
      const originalError = console.error;
      process.exit = jest.fn();
      console.error = jest.fn();

      await analyzerWithBadPath.run();

      expect(process.exit).toHaveBeenCalledWith(1);

      process.exit = originalExit;
      console.error = originalError;
    });

    it('should complete successfully with no jobs', async () => {
      const consoleSpy = jest.spyOn(console, 'log').mockImplementation();

      await analyzer.run();

      expect(consoleSpy).toHaveBeenCalledWith('⚠️  No jobs with triggers found');

      consoleSpy.mockRestore();
    });

    it('should handle analysis errors gracefully', async () => {
      const analyzerWithError = new GretlJobsAnalyzer({
        gretlJobsDir: testDir,
        outputFile: '/readonly/path/output.md' // This should cause write error
      });

      // Create a job to trigger analysis
      const jobDir = path.join(testDir, 'test-job');
      await fs.mkdir(jobDir, { recursive: true });
      await fs.writeFile(path.join(jobDir, 'job.properties'), 'triggers.cron=0 2 * * *');

      const originalExit = process.exit;
      const originalError = console.error;
      process.exit = jest.fn();
      console.error = jest.fn();

      await analyzerWithError.run();

      expect(process.exit).toHaveBeenCalledWith(1);

      process.exit = originalExit;
      console.error = originalError;
    });
  });

  describe('sogis-specific features', () => {
    it('should recognize sogis schema patterns', () => {
      expect(analyzer.getAmtsstelleFromSchema('agi_av')).toBe('Amt für Geoinformation');
      expect(analyzer.getAmtsstelleFromSchema('afu_gewaesser')).toBe('Amt für Umwelt');
      expect(analyzer.getAmtsstelleFromSchema('arp_npl')).toBe('Amt für Raumplanung');
      expect(analyzer.getAmtsstelleFromSchema('ada_archaeologie')).toBe('Amt für Denkmalpflege und Archäologie');
      expect(analyzer.getAmtsstelleFromSchema('avt_verkehr')).toBe('Amt für Verkehr und Tiefbau');
    });

    it('should handle unknown schemas', () => {
      expect(analyzer.getAmtsstelleFromSchema('unknown_schema')).toBe('');
      expect(analyzer.getAmtsstelleFromSchema('xyz')).toBe('');
    });

    it('should add schema info to table names', () => {
      expect(analyzer.getSchemaInfo('agi_av.liegenschaften')).toBe(' - Amt für Geoinformation');
      expect(analyzer.getSchemaInfo('afu_gewaesser.fliessgewaesser')).toBe(' - Amt für Umwelt');
      expect(analyzer.getSchemaInfo('simple_table')).toBe('');
    });

    it('should analyze schemas correctly', () => {
      const jobs = [
        {
          name: 'agi_job',
          sourceTables: ['agi_av.liegenschaften', 'agi_gb.grundstuecke'],
          targetTables: ['agi_export.data']
        },
        {
          name: 'afu_job',
          sourceTables: ['afu_gewaesser.fliessgewaesser'],
          targetTables: ['afu_export.summary']
        }
      ];

      const schemas = analyzer.analyzeSchemas(jobs);

      expect(schemas['agi_av']).toBeDefined();
      expect(schemas['agi_av'].description).toBe('Amt für Geoinformation');
      expect(schemas['agi_av'].jobs).toContain('agi_job');

      expect(schemas['afu_gewaesser']).toBeDefined();
      expect(schemas['afu_gewaesser'].description).toBe('Amt für Umwelt');
      expect(schemas['afu_gewaesser'].jobs).toContain('afu_job');
    });

    it('should generate sogis-specific markdown', () => {
      const jobs = [
        {
          name: 'agi_av_gb_abgleich',
          path: './agi_av_gb_abgleich',
          triggerType: 'cron',
          cronSchedule: 'H H(1-3) * * *',
          status: 'Aktiv',
          sourceTables: ['agi_av.liegenschaften', 'agi_gb.grundstuecke'],
          targetTables: ['agi_av_gb_abgleich.differenzen'],
          sortKey: '1'
        }
      ];

      const markdown = analyzer.generateMarkdown(jobs);

      expect(markdown).toContain('# GRETL Jobs Übersicht - sogis');
      expect(markdown).toContain('Jenkins-Instanz: [Jenkins sogis]');
      expect(markdown).toContain('## Analyse nach Amtsstellen (sogis)');
      expect(markdown).toContain('Amt für Geoinformation');
      expect(markdown).toContain('| Amtsstelle |');
      expect(markdown).toContain('info@sogis.so.ch');
      expect(markdown).toContain('sogis - Solothurner Geoinformations GmbH');
    });
  });

  describe('integration test', () => {
    it('should run complete analysis', async () => {
      // Create realistic sogis test structure
      const agiJobDir = path.join(testDir, 'agi_av_gb_abgleich');
      const afuJobDir = path.join(testDir, 'afu_gewaesser_import');

      await fs.mkdir(agiJobDir, { recursive: true });
      await fs.mkdir(afuJobDir, { recursive: true });

      // AGI job with typical sogis structure
      await fs.writeFile(path.join(agiJobDir, 'job.properties'), `
triggers.cron=H H(1-3) * * *
description=AV-GB Abgleich für sogis
      `.trim());

      await fs.writeFile(path.join(agiJobDir, 'av_gb_abgleich.sql'), `
        WITH filtered_av AS (
          SELECT * FROM agi_av.liegenschaften
          WHERE status = 'rechtskraeftig'
        )
        SELECT
          av.egrid,
          gb.nummer,
          CASE
            WHEN av.flaeche != gb.flaeche THEN 'Flächendifferenz'
            ELSE 'OK'
          END as status
        FROM filtered_av av
        JOIN agi_gb.grundstuecke gb ON av.egrid = gb.egrid
        WHERE av.flaeche != gb.flaeche;

        INSERT INTO agi_av_gb_abgleich.differenzen (egrid, typ, beschreibung)
        SELECT egrid, 'Fläche', 'Differenz zwischen AV und GB'
        FROM agi_av.liegenschaften av
        JOIN agi_gb.grundstuecke gb ON av.egrid = gb.egrid
        WHERE av.flaeche != gb.flaeche;
      `);

      // AFU job depending on AGI job
      await fs.writeFile(path.join(afuJobDir, 'job.properties'), `
triggers.upstream=agi_av_gb_abgleich
description=Gewässer Import nach AV-GB Abgleich
      `.trim());

      await fs.writeFile(path.join(afuJobDir, 'gewaesser_import.sql'), `
        SELECT
          g.objectid,
          g.gewaessername,
          ST_Intersects(g.geometrie, l.geometrie) as schneidet_liegenschaft
        FROM afu_gewaesser.fliessgewaesser g
        JOIN agi_av.liegenschaften l ON ST_Intersects(g.geometrie, l.geometrie)
        WHERE g.typ = 'Bach';

        CREATE TABLE afu_gewaesser_av.schnittpunkte AS
        SELECT * FROM afu_gewaesser.analysierte_daten;
      `);

      // Run analysis
      const jobs = await analyzer.analyzeJobs();
      const markdown = analyzer.generateMarkdown(jobs);

      // Verify sogis-specific results
      expect(jobs).toHaveLength(2);
      expect(jobs[0].name).toBe('agi_av_gb_abgleich');
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[1].name).toBe('afu_gewaesser_import');
      expect(jobs[1].triggerType).toBe('upstream');

      // Verify sogis-specific content
      expect(markdown).toContain('sogis');
      expect(markdown).toContain('~1-3h');
      expect(markdown).toContain('agi_av.liegenschaften');
      expect(markdown).toContain('afu_gewaesser.fliessgewaesser');
      expect(markdown).toContain('Amt für Geoinformation');
      expect(markdown).toContain('Amt für Umwelt');

      // Verify CTE filtering worked
      expect(markdown).not.toContain('filtered_av');

      // Verify schema analysis
      expect(markdown).toContain('## Analyse nach Amtsstellen (sogis)');
    });
  });
});
