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

  describe('parseJobProperties', () => {
    it('should parse job properties correctly', async () => {
      const propsFile = path.join(testDir, 'job.properties');
      await fs.writeFile(propsFile, `
# Comment line
triggers.cron=0 2 * * *
triggers.upstream=other_job
disabled=false
      `.trim());

      const result = analyzer.parseJobProperties(propsFile);

      expect(result).toEqual({
        'triggers.cron': '0 2 * * *',
        'triggers.upstream': 'other_job',
        'disabled': 'false'
      });
    });

    it('should handle empty or malformed files', () => {
      const result = analyzer.parseJobProperties('/nonexistent/file.properties');
      expect(result).toEqual({});
    });
  });

  describe('cronToText', () => {
    it('should convert standard cron expressions', () => {
      expect(analyzer.cronToText('0 2 * * *')).toBe('02:00');
      expect(analyzer.cronToText('30 14 * * *')).toBe('14:30');
      expect(analyzer.cronToText('0 6 * * 1')).toBe('Mo 06:00');
      expect(analyzer.cronToText('0 0 1 * *')).toBe('1. 00:00');
    });

    it('should handle Jenkins H syntax', () => {
      expect(analyzer.cronToText('H H * * *')).toBe('~zufällig');
      expect(analyzer.cronToText('H H(1-3) * * *')).toBe('~1-3h');
      expect(analyzer.cronToText('0 H(6-8) * * 1')).toBe('Mo ~6-8h');
      expect(analyzer.cronToText('H 14 * * *')).toBe('~14:xx');
    });

    it('should handle intervals', () => {
      expect(analyzer.cronToText('0 */4 * * *')).toBe('alle 4h');
      expect(analyzer.cronToText('0 */2 * * *')).toBe('alle 2h');
    });

    it('should handle empty or invalid input', () => {
      expect(analyzer.cronToText('')).toBe('-');
      expect(analyzer.cronToText(null)).toBe('-');
      expect(analyzer.cronToText(undefined)).toBe('-');
    });
  });

  describe('analyzeSqlFiles', () => {
    it('should analyze SQL files correctly', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.mkdir(jobDir, { recursive: true });

      const sqlContent = `
        SELECT * FROM source_table1 st1
        JOIN source_table2 st2 ON st1.id = st2.id;

        INSERT INTO target_table1 (col1, col2)
        VALUES ('test', 'value');

        UPDATE target_table2
        SET status = 'processed';
      `;

      await fs.writeFile(path.join(jobDir, 'query.sql'), sqlContent);

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toContain('source_table1');
      expect(result.sourceTables).toContain('source_table2');
      expect(result.targetTables).toContain('target_table1');
      expect(result.targetTables).toContain('target_table2');
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
  });

  describe('analyzeJobs', () => {
    it('should find and analyze jobs correctly', async () => {
      // Create test job structure
      const job1Dir = path.join(testDir, 'job1');
      const job2Dir = path.join(testDir, 'job2');

      await fs.mkdir(job1Dir, { recursive: true });
      await fs.mkdir(job2Dir, { recursive: true });

      // Job 1: Cron job
      await fs.writeFile(path.join(job1Dir, 'job.properties'), 'triggers.cron=0 2 * * *');
      await fs.writeFile(path.join(job1Dir, 'query.sql'), 'SELECT * FROM test_table;');

      // Job 2: Upstream job
      await fs.writeFile(path.join(job2Dir, 'job.properties'), 'triggers.upstream=job1');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(2);
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[0].cronSchedule).toBe('0 2 * * *');
      expect(jobs[1].triggerType).toBe('upstream');
      expect(jobs[1].upstream).toBe('job1');
    });

    it('should skip jobs without triggers', async () => {
      const jobDir = path.join(testDir, 'job-without-triggers');
      await fs.mkdir(jobDir, { recursive: true });
      await fs.writeFile(path.join(jobDir, 'job.properties'), 'some.other.property=value');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(0);
    });
  });

  describe('generateMarkdown', () => {
    it('should generate valid markdown', () => {
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
    });
  });

  describe('integration test', () => {
    it('should run complete analysis', async () => {
      // Create realistic test structure
      const job1Dir = path.join(testDir, 'daily_import');
      const job2Dir = path.join(testDir, 'weekly_report');

      await fs.mkdir(job1Dir, { recursive: true });
      await fs.mkdir(job2Dir, { recursive: true });

      // Daily import job
      await fs.writeFile(path.join(job1Dir, 'job.properties'), `
triggers.cron=H H(1-3) * * *
description=Daily data import
      `.trim());

      await fs.writeFile(path.join(job1Dir, 'import.sql'), `
        SELECT * FROM source_system.raw_data
        WHERE updated_date >= CURRENT_DATE - 1;

        INSERT INTO staging.daily_import (data, import_date)
        SELECT processed_data, CURRENT_DATE
        FROM source_system.raw_data;
      `);

      // Weekly report job
      await fs.writeFile(path.join(job2Dir, 'job.properties'), `
triggers.upstream=daily_import
description=Weekly aggregation report
      `.trim());

      await fs.writeFile(path.join(job2Dir, 'report.sql'), `
        SELECT
          DATE_TRUNC('week', import_date) as week,
          COUNT(*) as record_count
        FROM staging.daily_import
        GROUP BY week;

        CREATE TABLE reports.weekly_summary AS
        SELECT * FROM staging.aggregated_data;
      `);

      // Run analysis
      const jobs = await analyzer.analyzeJobs();
      const markdown = analyzer.generateMarkdown(jobs);

      // Verify results
      expect(jobs).toHaveLength(2);
      expect(jobs[0].name).toBe('daily_import');
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[1].name).toBe('weekly_report');
      expect(jobs[1].triggerType).toBe('upstream');

      expect(markdown).toContain('daily_import');
      expect(markdown).toContain('weekly_report');
      expect(markdown).toContain('~1-3h');
      expect(markdown).toContain('source_system.raw_data');
      expect(markdown).toContain('staging.daily_import');
    });
  });
});

describe('GretlJobsAnalyzer', () => {
  let analyzer;
  let testDir;

  beforeEach(async () => {
    testDir = await fs.mkdtemp(path.join(__dirname, 'test-'));
    analyzer = new GretlJobsAnalyzer({
      gretlJobsDir: testDir,
      outputFile: path.join(testDir, 'test-output.md'),
      debug: false
    });
  });

  afterEach(async () => {
    await fs.remove(testDir);
  });

  describe('parseJobProperties', () => {
    it('should parse job properties correctly', async () => {
      const propsFile = path.join(testDir, 'job.properties');
      await fs.writeFile(propsFile, `
# Comment line
triggers.cron=0 2 * * *
triggers.upstream=other_job
disabled=false
      `.trim());

      const result = analyzer.parseJobProperties(propsFile);

      expect(result).toEqual({
        'triggers.cron': '0 2 * * *',
        'triggers.upstream': 'other_job',
        'disabled': 'false'
      });
    });

    it('should handle empty or malformed files', () => {
      const result = analyzer.parseJobProperties('/nonexistent/file.properties');
      expect(result).toEqual({});
    });
  });

  describe('cronToText', () => {
    it('should convert standard cron expressions', () => {
      expect(analyzer.cronToText('0 2 * * *')).toBe('02:00');
      expect(analyzer.cronToText('30 14 * * *')).toBe('14:30');
      expect(analyzer.cronToText('0 6 * * 1')).toBe('Mo 06:00');
      expect(analyzer.cronToText('0 0 1 * *')).toBe('1. 00:00');
    });

    it('should handle Jenkins H syntax', () => {
      expect(analyzer.cronToText('H H * * *')).toBe('~zufällig');
      expect(analyzer.cronToText('H H(1-3) * * *')).toBe('~1-3h');
      expect(analyzer.cronToText('0 H(6-8) * * 1')).toBe('Mo ~6-8h');
      expect(analyzer.cronToText('H 14 * * *')).toBe('~14:xx');
    });

    it('should handle intervals', () => {
      expect(analyzer.cronToText('0 */4 * * *')).toBe('alle 4h');
      expect(analyzer.cronToText('0 */2 * * *')).toBe('alle 2h');
    });

    it('should handle empty or invalid input', () => {
      expect(analyzer.cronToText('')).toBe('-');
      expect(analyzer.cronToText(null)).toBe('-');
      expect(analyzer.cronToText(undefined)).toBe('-');
    });
  });

  describe('analyzeSqlFiles', () => {
    it('should analyze SQL files correctly', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.ensureDir(jobDir);

      const sqlContent = `
        SELECT * FROM source_table1 st1
        JOIN source_table2 st2 ON st1.id = st2.id;

        INSERT INTO target_table1 (col1, col2)
        VALUES ('test', 'value');

        UPDATE target_table2
        SET status = 'processed';
      `;

      await fs.writeFile(path.join(jobDir, 'query.sql'), sqlContent);

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toContain('source_table1');
      expect(result.sourceTables).toContain('source_table2');
      expect(result.targetTables).toContain('target_table1');
      expect(result.targetTables).toContain('target_table2');
    });

    it('should ignore searchindex SQL files', async () => {
      const jobDir = path.join(testDir, 'test-job');
      await fs.ensureDir(jobDir);

      await fs.writeFile(path.join(jobDir, 'searchindex_create.sql'), 'CREATE TABLE searchindex_table (id INT);');
      await fs.writeFile(path.join(jobDir, 'normal.sql'), 'SELECT * FROM normal_table;');

      const result = await analyzer.analyzeSqlFiles(jobDir);

      expect(result.sourceTables).toContain('normal_table');
      expect(result.sourceTables).not.toContain('searchindex_table');
      expect(result.targetTables).not.toContain('searchindex_table');
    });
  });

  describe('analyzeJobs', () => {
    it('should find and analyze jobs correctly', async () => {
      // Create test job structure
      const job1Dir = path.join(testDir, 'job1');
      const job2Dir = path.join(testDir, 'job2');

      await fs.ensureDir(job1Dir);
      await fs.ensureDir(job2Dir);

      // Job 1: Cron job
      await fs.writeFile(path.join(job1Dir, 'job.properties'), 'triggers.cron=0 2 * * *');
      await fs.writeFile(path.join(job1Dir, 'query.sql'), 'SELECT * FROM test_table;');

      // Job 2: Upstream job
      await fs.writeFile(path.join(job2Dir, 'job.properties'), 'triggers.upstream=job1');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(2);
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[0].cronSchedule).toBe('0 2 * * *');
      expect(jobs[1].triggerType).toBe('upstream');
      expect(jobs[1].upstream).toBe('job1');
    });

    it('should skip jobs without triggers', async () => {
      const jobDir = path.join(testDir, 'job-without-triggers');
      await fs.ensureDir(jobDir);
      await fs.writeFile(path.join(jobDir, 'job.properties'), 'some.other.property=value');

      const jobs = await analyzer.analyzeJobs();

      expect(jobs).toHaveLength(0);
    });
  });

  describe('generateMarkdown', () => {
    it('should generate valid markdown', () => {
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
    });
  });

  describe('integration test', () => {
    it('should run complete analysis', async () => {
      // Create realistic test structure
      const job1Dir = path.join(testDir, 'daily_import');
      const job2Dir = path.join(testDir, 'weekly_report');

      await fs.ensureDir(job1Dir);
      await fs.ensureDir(job2Dir);

      // Daily import job
      await fs.writeFile(path.join(job1Dir, 'job.properties'), `
triggers.cron=H H(1-3) * * *
description=Daily data import
      `.trim());

      await fs.writeFile(path.join(job1Dir, 'import.sql'), `
        SELECT * FROM source_system.raw_data
        WHERE updated_date >= CURRENT_DATE - 1;

        INSERT INTO staging.daily_import (data, import_date)
        SELECT processed_data, CURRENT_DATE
        FROM source_system.raw_data;
      `);

      // Weekly report job
      await fs.writeFile(path.join(job2Dir, 'job.properties'), `
triggers.upstream=daily_import
description=Weekly aggregation report
      `.trim());

      await fs.writeFile(path.join(job2Dir, 'report.sql'), `
        SELECT
          DATE_TRUNC('week', import_date) as week,
          COUNT(*) as record_count
        FROM staging.daily_import
        GROUP BY week;

        CREATE TABLE reports.weekly_summary AS
        SELECT * FROM staging.aggregated_data;
      `);

      // Run analysis
      const jobs = await analyzer.analyzeJobs();
      const markdown = analyzer.generateMarkdown(jobs);

      // Verify results
      expect(jobs).toHaveLength(2);
      expect(jobs[0].name).toBe('daily_import');
      expect(jobs[0].triggerType).toBe('cron');
      expect(jobs[1].name).toBe('weekly_report');
      expect(jobs[1].triggerType).toBe('upstream');

      expect(markdown).toContain('daily_import');
      expect(markdown).toContain('weekly_report');
      expect(markdown).toContain('~1-3h');
      expect(markdown).toContain('source_system.raw_data');
      expect(markdown).toContain('staging.daily_import');
    });
  });
});
