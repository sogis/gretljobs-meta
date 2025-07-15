// src/analyzer.js
const fs = require('fs').promises;
const fsSync = require('fs');
const path = require('path');
const { glob } = require('glob');

class GretlJobsAnalyzer {
  constructor(options = {}) {
    this.gretlJobsDir = options.gretlJobsDir || '../gretljobs';
    this.outputFile = options.outputFile || 'GRETL_Jobs_Overview.md';
    this.debug = options.debug || false;
  }

  log(message) {
    if (this.debug) {
      console.log(`[DEBUG] ${message}`);
    }
  }

  error(message) {
    console.error(`[ERROR] ${message}`);
  }

  // Check if path exists
  async pathExists(filePath) {
    try {
      await fs.access(filePath);
      return true;
    } catch {
      return false;
    }
  }

  // Parse job.properties file
  parseJobProperties(filePath) {
    try {
      const content = fsSync.readFileSync(filePath, 'utf8');
      const properties = {};

      content.split('\n').forEach(line => {
        line = line.trim();
        if (line && !line.startsWith('#')) {
          const [key, ...valueParts] = line.split('=');
          if (key && valueParts.length > 0) {
            properties[key.trim()] = valueParts.join('=').trim();
          }
        }
      });

      return properties;
    } catch (error) {
      this.error(`Error parsing ${filePath}: ${error.message}`);
      return {};
    }
  }

  // Convert Jenkins cron to human readable format
  cronToText(cronExpression) {
    if (!cronExpression) return '-';

    const parts = cronExpression.split(' ');
    if (parts.length < 5) return cronExpression;

    // eslint-disable-next-line no-unused-vars
    const [minute, hour, day, month, dow] = parts;

    // Handle Jenkins H syntax
    let timeStr = '';

    if (hour === 'H') {
      timeStr = '~zufällig';
    } else if (hour.match(/H\((\d+)-(\d+)\)/)) {
      const match = hour.match(/H\((\d+)-(\d+)\)/);
      timeStr = `~${match[1]}-${match[2]}h`;
    } else if (hour.match(/^\d+$/)) {
      if (minute === 'H') {
        timeStr = `~${hour}:xx`;
      } else if (minute.match(/^\d+$/)) {
        timeStr = `${hour.padStart(2, '0')}:${minute.padStart(2, '0')}`;
      } else {
        timeStr = `${hour}:xx`;
      }
    } else if (hour.match(/^\*\/\d+$/)) {
      // Only handle standard interval syntax */N, not H/N
      const interval = hour.split('/')[1];
      timeStr = `alle ${interval}h`;
    } else {
      timeStr = '~variabel';
    }

    // Handle day of week
    const dayNames = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa'];
    if (dow !== '*') {
      const dayNum = parseInt(dow);
      if (dayNum >= 0 && dayNum <= 6) {
        return `${dayNames[dayNum]} ${timeStr}`;
      } else if (dayNum === 7) {
        return `${dayNames[0]} ${timeStr}`; // 7 is also Sunday
      }
    } else if (day.match(/^\d+$/)) {
      return `${day}. ${timeStr}`;
    }

    return timeStr;
  }

  // Find all job.properties files
  async findJobProperties() {
    const pattern = path.join(this.gretlJobsDir, '**/job.properties').replace(/\\/g, '/');
    this.log(`Searching for job.properties files in: ${pattern}`);

    try {
      const files = await glob(pattern);
      this.log(`Found ${files.length} job.properties files`);
      return files;
    } catch (error) {
      this.error(`Error finding job.properties files: ${error.message}`);
      return [];
    }
  }

  // Analyze SQL files for table access
  async analyzeSqlFiles(jobDir) {
    const pattern = path.join(jobDir, '**/*.sql').replace(/\\/g, '/');

    try {
      const sqlFiles = await glob(pattern);
      const filteredFiles = sqlFiles.filter(file => !path.basename(file).startsWith('searchindex_'));

      const sourceTables = new Set();
      const targetTables = new Set();

      for (const sqlFile of filteredFiles) {
        try {
          const content = await fs.readFile(sqlFile, 'utf8');

          // Extract CTE names to ignore them later
          const cteNames = this.extractCteNames(content);

          // Find FROM tables (source) - improved regex
          const fromMatches = content.match(/FROM\s+([a-zA-Z_][a-zA-Z0-9_.]*)/gi);
          if (fromMatches) {
            fromMatches.forEach(match => {
              const table = match.replace(/FROM\s+/i, '').trim();
              if (!cteNames.has(table.toLowerCase())) {
                sourceTables.add(table);
              }
            });
          }

          // Find JOIN tables (also source) - new addition
          const joinMatches = content.match(/JOIN\s+([a-zA-Z_][a-zA-Z0-9_.]*)/gi);
          if (joinMatches) {
            joinMatches.forEach(match => {
              const table = match.replace(/JOIN\s+/i, '').trim();
              if (!cteNames.has(table.toLowerCase())) {
                sourceTables.add(table);
              }
            });
          }

          // Find INSERT/UPDATE/CREATE tables (target)
          const targetMatches = content.match(/(INSERT\s+INTO|UPDATE|CREATE\s+TABLE)\s+([a-zA-Z_][a-zA-Z0-9_.]*)/gi);
          if (targetMatches) {
            targetMatches.forEach(match => {
              const table = match.replace(/(INSERT\s+INTO|UPDATE|CREATE\s+TABLE)\s+/i, '').trim();
              // CTEs are never targets, so no need to check
              targetTables.add(table);
            });
          }
        } catch (error) {
          this.error(`Error reading SQL file ${sqlFile}: ${error.message}`);
        }
      }

      return {
        sourceTables: Array.from(sourceTables),
        targetTables: Array.from(targetTables)
      };
    } catch (error) {
      this.error(`Error analyzing SQL files in ${jobDir}: ${error.message}`);
      return { sourceTables: [], targetTables: [] };
    }
  }

  // Extract CTE (Common Table Expression) names from SQL content
  extractCteNames(sqlContent) {
    const cteNames = new Set();

    // Remove comments and strings to avoid false matches
    const cleanSql = sqlContent
      .replace(/--[^\n]*/g, '') // Remove single-line comments
      .replace(/\/\*[\s\S]*?\*\//g, '') // Remove multi-line comments
      .replace(/'[^']*'/g, "''") // Remove string literals
      .replace(/"[^"]*"/g, '""'); // Remove quoted identifiers

    // Match WITH clauses: WITH cte_name AS (...), another_cte AS (...)
    const withMatches = cleanSql.match(/WITH\s+([^()]+?)(?:\s+AS\s*\()/gi);
    if (withMatches) {
      withMatches.forEach(match => {
        // Extract CTE name from "WITH cte_name AS ("
        const cteMatch = match.match(/WITH\s+([a-zA-Z_][a-zA-Z0-9_]*)/i);
        if (cteMatch) {
          cteNames.add(cteMatch[1].toLowerCase());
        }
      });
    }

    // Match additional CTEs in the same WITH clause: , cte_name AS (...)
    const additionalCteMatches = cleanSql.match(/,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+AS\s*\(/gi);
    if (additionalCteMatches) {
      additionalCteMatches.forEach(match => {
        const cteMatch = match.match(/,\s*([a-zA-Z_][a-zA-Z0-9_]*)\s+AS/i);
        if (cteMatch) {
          cteNames.add(cteMatch[1].toLowerCase());
        }
      });
    }

    this.log(`Found CTEs: ${Array.from(cteNames).join(', ')}`);
    return cteNames;
  }

  // Analyze all jobs
  async analyzeJobs() {
    const jobFiles = await this.findJobProperties();
    const jobs = [];

    for (const filePath of jobFiles) {
      const jobDir = path.dirname(filePath);
      const jobName = path.basename(jobDir);

      this.log(`Processing job: ${jobName}`);

      const properties = this.parseJobProperties(filePath);
      const cronSchedule = properties['triggers.cron'];
      const upstream = properties['triggers.upstream'];

      if (cronSchedule || upstream) {
        const status = properties['disabled'] === 'true' || properties['enabled'] === 'false' ? 'Inaktiv' : 'Aktiv';

        const triggerType = cronSchedule ? 'cron' : 'upstream';
        const triggerValue = cronSchedule || upstream;

        // Analyze SQL files
        const sqlAnalysis = await this.analyzeSqlFiles(jobDir);

        jobs.push({
          name: jobName,
          path: jobDir,
          triggerType,
          triggerValue,
          cronSchedule,
          upstream,
          status,
          sourceTables: sqlAnalysis.sourceTables,
          targetTables: sqlAnalysis.targetTables,
          sortKey: triggerType === 'cron' ? `1_${cronSchedule}_${jobName}` : `2_upstream_${jobName}`
        });
      }
    }

    // Sort jobs
    jobs.sort((a, b) => a.sortKey.localeCompare(b.sortKey));

    this.log(`Found ${jobs.length} jobs with triggers`);
    return jobs;
  }

  // Generate markdown documentation
  generateMarkdown(jobs) {
    const timestamp = new Date().toISOString().slice(0, 19).replace('T', ' ');
    const repoName = path.basename(path.resolve(this.gretlJobsDir));

    let markdown = `# GRETL Jobs Übersicht - sogis

*Generiert am: ${timestamp} UTC, *
*Repository: ${repoName}*

## Zeitgesteuerte Jobs (sortiert nach Schedule)

| Job Name | Trigger | Schedule | Lesbar | Pfad | Status |
|----------|---------|----------|--------|------|---------|
`;

    // Generate job table
    jobs.forEach(job => {
      if (job.triggerType === 'cron') {
        const readable = this.cronToText(job.cronSchedule);
        markdown += `| ${job.name} | Cron | \`${job.cronSchedule}\` | ${readable} | \`${job.path}/\` | ${job.status} |\n`;
      } else {
        markdown += `| ${job.name} | Upstream | ${job.upstream} | - | \`${job.path}/\` | ${job.status} |\n`;
      }
    });

    // Generate detailed job analysis
    markdown += `\n## Tabellenzugriffe pro Job\n\n`;

    jobs.forEach(job => {
      markdown += `### ${job.name}\n`;
      markdown += `- **Pfad**: \`${job.path}/\`\n`;

      if (job.triggerType === 'cron') {
        const readable = this.cronToText(job.cronSchedule);
        markdown += `- **Schedule**: \`${job.cronSchedule}\` (${readable})\n`;
      } else {
        markdown += `- **Upstream-Trigger**: ${job.upstream}\n`;
      }

      if (job.sourceTables.length > 0) {
        markdown += `- **Quell-Tabellen**: \n`;
        job.sourceTables.forEach(table => {
          const schemaInfo = this.getSchemaInfo(table);
          markdown += `  - \`${table}\` (READ)${schemaInfo}\n`;
        });
      }

      if (job.targetTables.length > 0) {
        markdown += `- **Ziel-Tabellen**: \n`;
        job.targetTables.forEach(table => {
          const schemaInfo = this.getSchemaInfo(table);
          markdown += `  - \`${table}\` (INSERT/UPDATE)${schemaInfo}\n`;
        });
      }

      markdown += `\n`;
    });

    // Generate schema-specific analysis
    const schemaAnalysis = this.analyzeSchemas(jobs);
    if (Object.keys(schemaAnalysis).length > 0) {
      markdown += `## Analyse nach Amtsstellen (sogis)\n\n`;

      Object.entries(schemaAnalysis).forEach(([schema, info]) => {
        markdown += `### ${info.description} (${schema})\n`;
        markdown += `- **Jobs**: ${info.jobs.length}\n`;
        markdown += `- **Tabellen**: ${info.tables.length}\n`;
        markdown += `- **Job-Namen**: ${info.jobs.join(', ')}\n\n`;
      });
    }

    // Generate table frequency analysis
    const tableFrequency = new Map();
    jobs.forEach(job => {
      [...job.sourceTables, ...job.targetTables].forEach(table => {
        tableFrequency.set(table, (tableFrequency.get(table) || 0) + 1);
      });
    });

    const sortedTables = Array.from(tableFrequency.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 15); // Show top 15 for sogis

    if (sortedTables.length > 0) {
      markdown += `## Häufig verwendete Tabellen\n\n`;
      markdown += `| Anzahl | Tabellenname | Schema | Amtsstelle |\n`;
      markdown += `|--------|-------------|--------|------------|\n`;

      sortedTables.forEach(([table, count]) => {
        const parts = table.split('.');
        const schema = parts.length > 1 ? parts[0] : '';
        const tableName = parts.length > 1 ? parts[1] : table;
        const amtsstelle = this.getAmtsstelleFromSchema(schema);
        markdown += `| ${count} | ${tableName} | ${schema} | ${amtsstelle} |\n`;
      });
    }

    // Footer

    markdown += `### Kontakt\n`;
    markdown += `- **Repository**: https://github.com/sogis/gretljobs-meta\n`;
    markdown += `- **GRETL Jobs**: https://github.com/sogis/gretljobs\n`;
    markdown += `- **Support**: christian.baumann@bd.so.ch\n\n`;

    markdown += `---\n`;
    markdown += `*Diese Dokumentation wurde automatisch generiert am ${timestamp}*\n`;

    return markdown;
  }

  // Get schema information for sogis
  getSchemaInfo(tableName) {
    if (!tableName.includes('.')) return '';

    const schema = tableName.split('.')[0];
    const amtsstelle = this.getAmtsstelleFromSchema(schema);

    return amtsstelle ? ` - ${amtsstelle}` : '';
  }

  // Get Amtsstelle from schema prefix
  getAmtsstelleFromSchema(schema) {
    const amtsstellen = {
      'agi': 'Amt für Geoinformation',
      'afu': 'Amt für Umwelt',
      'arp': 'Amt für Raumplanung',
      'ada': 'Amt für Denkmalpflege und Archäologie',
      'avt': 'Amt für Verkehr und Tiefbau',
      'awjf': 'Amt für Wald, Jagd und Fischerei',
      'alw': 'Amt für Landwirtschaft',
      'so': 'Kanton Solothurn',
      'sogis': 'sogis'
    };

    const prefix = schema.split('_')[0];
    return amtsstellen[prefix] || '';
  }

  // Analyze jobs and tables by schema
  analyzeSchemas(jobs) {
    const schemas = {};

    jobs.forEach(job => {
      const allTables = [...job.sourceTables, ...job.targetTables];

      allTables.forEach(table => {
        if (table.includes('.')) {
          const schema = table.split('.')[0];
          const prefix = schema.split('_')[0];

          if (!schemas[schema]) {
            schemas[schema] = {
              description: this.getAmtsstelleFromSchema(schema) || schema,
              jobs: new Set(),
              tables: new Set()
            };
          }

          schemas[schema].jobs.add(job.name);
          schemas[schema].tables.add(table);
        }
      });
    });

    // Convert Sets to Arrays
    Object.keys(schemas).forEach(schema => {
      schemas[schema].jobs = Array.from(schemas[schema].jobs);
      schemas[schema].tables = Array.from(schemas[schema].tables);
    });

    return schemas;
  }

  // Main analysis function
  async run() {
    console.log('=== GRETL Jobs Dokumentation Generator (Node.js) ===');
    console.log(`Analysiere Jobs in: ${this.gretlJobsDir}`);
    console.log(`Ausgabedatei: ${this.outputFile}`);

    // Check if GRETL jobs directory exists
    if (!await this.pathExists(this.gretlJobsDir)) {
      this.error(`GRETL Jobs directory not found: ${this.gretlJobsDir}`);
      process.exit(1);
    }

    try {
      // Analyze jobs
      const jobs = await this.analyzeJobs();

      if (jobs.length === 0) {
        console.log('⚠️  No jobs with triggers found');
        return;
      }

      // Generate documentation
      const markdown = this.generateMarkdown(jobs);

      // Write to file
      await fs.writeFile(this.outputFile, markdown, 'utf8');

      console.log(`✅ Documentation created: ${this.outputFile}`);
      console.log(`📊 Analyzed ${jobs.length} jobs`);
      console.log(`📄 Script completed successfully!`);

    } catch (error) {
      this.error(`Analysis failed: ${error.message}`);
      process.exit(1);
    }
  }
}

// CLI usage
if (require.main === module) {
  const analyzer = new GretlJobsAnalyzer({
    gretlJobsDir: process.env.GRETL_JOBS_DIR || '../gretljobs',
    outputFile: process.env.OUTPUT_FILE || 'GRETL_Jobs_Overview.md',
    debug: process.env.DEBUG === 'true'
  });

  analyzer.run();
}

module.exports = GretlJobsAnalyzer;
