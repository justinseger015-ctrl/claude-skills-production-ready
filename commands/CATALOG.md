# Command Catalog

**Last Updated:** November 24, 2025
**Total Commands:** 0
**Status:** Foundation - Ready for Command Creation

---

## Overview

This catalog lists all available slash commands for the claude-skills repository. Commands are organized by category for easy discovery.

### What are Slash Commands?

Slash commands are task automation shortcuts that save developers time on repetitive workflows:

- **High-frequency** - Used multiple times per day/week
- **Standardized** - Consistent execution every time
- **Time-saving** - 50-90% reduction in manual work
- **Quality-focused** - Ensures standards compliance

### How to Use Commands

```bash
# Basic usage
/command-name

# With arguments
/command-name arg1 arg2

# Get help
/command-name --help
```

---

## Command Categories

### Code Category

Commands for code-related operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/code.review-pr` - Comprehensive code review with quality analysis
- `/code.format-check` - Validates code formatting standards
- `/code.complexity-analyze` - Analyzes code complexity metrics
- `/code.refactor-suggest` - Suggests refactoring opportunities

---

### Docs Category

Commands for documentation operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/docs.update-readme` - Updates README with latest counts
- `/docs.validate-links` - Checks for broken links
- `/docs.generate-catalog` - Creates/updates catalog files
- `/docs.spell-check` - Spell checks documentation

---

### Git Category

Commands for git workflow operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/git.create-pr` - Creates pull request with proper formatting
- `/git.create-branch` - Creates feature branch with naming conventions
- `/git.commit-conventional` - Creates conventional commit message
- `/git.sync-develop` - Syncs with develop branch

---

### Test Category

Commands for testing operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/test.run-suite` - Executes full test suite with coverage
- `/test.coverage-report` - Generates coverage report
- `/test.integration-tests` - Runs integration tests
- `/test.e2e-tests` - Runs end-to-end tests

---

### Deploy Category

Commands for deployment operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/deploy.staging` - Deploys to staging environment
- `/deploy.production` - Deploys to production (with safeguards)
- `/deploy.rollback` - Rolls back deployment
- `/deploy.health-check` - Performs health check

---

### Security Category

Commands for security operations:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/security.scan-secrets` - Scans for hardcoded secrets
- `/security.audit-dependencies` - Audits dependencies for vulnerabilities
- `/security.vulnerability-scan` - Scans for security vulnerabilities
- `/security.compliance-check` - Checks compliance requirements

---

### Architecture Category

Commands for architecture and design:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/architecture.design-review` - Expert architecture review
- `/architecture.generate-diagram` - Generates architecture diagrams
- `/architecture.dependency-analysis` - Analyzes dependencies
- `/architecture.api-design` - Reviews API design

---

### Content Category

Commands for content creation:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/content.analyze-seo` - Analyzes content for SEO
- `/content.generate-meta` - Generates meta descriptions
- `/content.keyword-research` - Performs keyword research
- `/content.readability-check` - Checks content readability

---

### Workflow Category

Commands for general workflow automation:

**Available Commands:**
- *No commands yet - coming soon!*

**Planned Commands:**
- `/workflow.daily-standup` - Generates daily standup report
- `/workflow.weekly-summary` - Creates weekly summary
- `/workflow.cleanup-branches` - Cleans up merged branches
- `/workflow.sync-all` - Syncs all repositories

---

## Command Patterns

Commands follow one of three patterns based on complexity:

### Simple Pattern (Context → Task)
- **Use For:** Straightforward, single-purpose tasks
- **Structure:** Context gathering → Task execution → Report results
- **Examples:** `/docs.update-readme`, `/git.format-code`
- **Execution Time:** < 1 minute

### Multi-Phase Pattern (Discovery → Analysis → Task)
- **Use For:** Complex analysis requiring multiple steps
- **Structure:** Discovery → Analysis → Task → Report
- **Examples:** `/code.review-pr`, `/security.audit-code`
- **Execution Time:** 1-5 minutes

### Agent-Style Pattern (Role → Process → Guidelines)
- **Use For:** Specialized expertise requiring domain knowledge
- **Structure:** Role → Process → Guidelines → Deliverables
- **Examples:** `/architecture.design-review`, `/ux.usability-review`
- **Execution Time:** 3-10 minutes

---

## Browse by Pattern

### Simple Commands

*No simple commands yet - coming soon!*

### Multi-Phase Commands

*No multi-phase commands yet - coming soon!*

### Agent-Style Commands

*No agent-style commands yet - coming soon!*

---

## Browse by Use Case

### Daily Development
*Coming soon*

### Code Quality
*Coming soon*

### Documentation
*Coming soon*

### CI/CD Pipeline
*Coming soon*

### Security & Compliance
*Coming soon*

---

## Validation Status

All commands in this catalog must pass 8 validation checks:

1. ✓ Name Format - Follows `category.command-name` pattern
2. ✓ YAML Frontmatter - Valid metadata with required fields
3. ✓ Description Length - Clear, concise (≤ 150 chars)
4. ✓ Pattern Validity - Follows declared pattern structure
5. ✓ Category Validity - Recognized or valid custom category
6. ✓ Content Completeness - All required sections present
7. ✓ Markdown Structure - Proper hierarchy and formatting
8. ✓ Integration References - All references exist

**Current Status:**
- Total Commands: 0
- Passing All Checks: 0
- Validation Rate: N/A

---

## Installation

### Using Commands in Claude Code

Commands are automatically discovered when present in the `commands/` directory:

```bash
# 1. Commands are in the repository
ls commands/

# 2. Use any command
/category.command-name

# 3. Get help for a command
/category.command-name --help
```

### Using Commands Standalone

You can extract and use commands outside this repository:

```bash
# 1. Copy command file
cp commands/category/command-name.md ~/.claude/commands/

# 2. Use in any project
cd /path/to/your/project
/command-name
```

---

## Integration with Agents and Skills

### Commands + Agents

Commands can work with agents for enhanced functionality:

**Example Workflow:**
```bash
# 1. Use command for quick task
/code.review-pr 123

# 2. For deeper analysis, use agent
cs-code-reviewer --pr 123 --deep-analysis
```

**Relationship:**
- **Commands** - Quick, focused automation
- **Agents** - Comprehensive, guided workflows

### Commands + Skills

Commands leverage skills for domain expertise:

**Example:**
```bash
# Command uses skill's Python tools
/content.analyze-seo article.md
# Executes: skills/marketing-team/content-creator/scripts/seo_optimizer.py

# Or use skill directly via agent
cs-content-creator
```

**Relationship:**
- **Commands** - Automate specific tasks
- **Skills** - Provide tools, knowledge, templates

---

## Contributing Commands

### Creating a New Command

```bash
# 1. Use interactive builder (recommended)
python3 scripts/command_builder.py

# 2. Or use config file
python3 scripts/command_builder.py --config my-commands.yaml

# 3. Validate your command
python3 scripts/command_builder.py --validate commands/category/command-name.md

# 4. Test the command
/category.command-name

# 5. Submit PR
git add commands/category/command-name.md commands/CATALOG.md
git commit -m "feat(commands): add category.command-name"
git push origin feature/command-name
```

### Contribution Guidelines

**Before Creating:**
1. Check if similar command exists
2. Review [Command Development Guide](CLAUDE.md)
3. Understand [Command Standards](../docs/standards/command-standards.md)
4. Choose appropriate pattern (simple, multi-phase, agent-style)

**During Creation:**
1. Use descriptive, action-oriented name
2. Write clear, concise description
3. Provide comprehensive examples
4. Document error handling
5. Link related commands/agents/skills

**After Creation:**
1. Run all 8 validations
2. Test with various inputs
3. Update catalog (automatic with builder)
4. Create PR with conventional commit
5. Respond to reviewer feedback

---

## Command Naming Conventions

### Format

**Pattern:** `category.command-name`

**Rules:**
- Kebab-case (lowercase with hyphens)
- Category prefix (e.g., `git`, `code`, `docs`)
- Dot separator (`.`) between category and name
- Action-oriented name
- Max 40 characters

### Examples

**Good Names:**
```
✓ git.create-pr          - Clear action, proper category
✓ code.review-pr         - Specific and descriptive
✓ docs.update-readme     - Exact purpose stated
✓ test.run-suite         - Simple and clear
```

**Bad Names:**
```
✗ createPR               - Not kebab-case, no category
✗ git-create-pr          - Wrong separator (use dot)
✗ pr                     - Too vague, no category
✗ git.create-pull-request-with-template  - Too long
```

---

## Frequently Asked Questions

### Q: How are commands different from agents?

**A:** Commands are quick automation shortcuts (seconds-minutes), while agents are comprehensive workflow orchestrators (minutes-hours). Use commands for repetitive tasks, agents for complex workflows.

### Q: Can I create custom command categories?

**A:** Yes! Use standard categories when possible, but custom categories are supported if they're kebab-case, 3-20 characters, and represent a clear grouping.

### Q: What model should I use for commands?

**A:** Default to `sonnet` for most commands. Use `haiku` for simple, fast tasks (< 10 seconds). Use `opus` for complex reasoning or strategic decisions.

### Q: How do I make commands interactive?

**A:** Set `interactive: true` in frontmatter and document the interaction points. Use for commands that need user confirmation or additional input during execution.

### Q: Can commands modify files?

**A:** Yes, but mark them as `dangerous: true` in frontmatter. These commands should ask for user confirmation before making changes.

### Q: How do I test commands before submitting?

**A:** 1) Validate with `command_builder.py --validate`, 2) Test basic usage, 3) Test with various inputs, 4) Test error cases, 5) Verify output format and location.

---

## Roadmap

### Phase 1: Foundation (Current)
- [x] Command template created
- [x] Command standards documented
- [x] Development guide written
- [x] Catalog structure established
- [ ] Command builder tool implemented

### Phase 2: Core Commands (Q1 2026)
- [ ] Git workflow commands (5)
- [ ] Documentation commands (5)
- [ ] Code quality commands (5)
- [ ] Testing commands (3)

### Phase 3: Expansion (Q2 2026)
- [ ] Deployment commands (4)
- [ ] Security commands (4)
- [ ] Architecture commands (3)
- [ ] Content commands (3)

### Phase 4: Integration (Q2 2026)
- [ ] Agent integration commands
- [ ] Skill automation commands
- [ ] Workflow orchestration commands
- [ ] Website deployment

---

## Support

### Documentation
- **[Command Development Guide](CLAUDE.md)** - How to create commands
- **[Command Standards](../docs/standards/command-standards.md)** - Validation rules
- **[Command Template](../templates/command-template.md)** - Starting template
- **[Config Example](../templates/command-config.yaml)** - Batch creation

### Related Resources
- **[Agent Catalog](../agents/README.md)** - Available agents
- **[Skills Catalog](../docs/SKILLS_CATALOG.md)** - Available skills
- **[Main Documentation](../CLAUDE.md)** - Repository overview

### Getting Help

**Issues:**
- Check [FAQ](#frequently-asked-questions)
- Search existing issues
- Create new issue with details

**Questions:**
- Review documentation first
- Check related resources
- Ask in discussions

---

## Statistics

### By Category

| Category | Count | Planned |
|----------|-------|---------|
| Code | 0 | 4 |
| Docs | 0 | 4 |
| Git | 0 | 4 |
| Test | 0 | 3 |
| Deploy | 0 | 4 |
| Security | 0 | 4 |
| Architecture | 0 | 3 |
| Content | 0 | 3 |
| Workflow | 0 | 4 |
| **Total** | **0** | **33** |

### By Pattern

| Pattern | Count | Planned |
|---------|-------|---------|
| Simple | 0 | 15 |
| Multi-Phase | 0 | 12 |
| Agent-Style | 0 | 6 |
| **Total** | **0** | **33** |

### Validation Status

| Status | Count | Percentage |
|--------|-------|------------|
| All Passing | 0 | N/A |
| Partial | 0 | N/A |
| Failing | 0 | N/A |
| **Total** | **0** | **0%** |

---

**Last Updated:** November 24, 2025
**Next Update:** As commands are added
**Maintained By:** Claude Skills Team
**Status:** Ready for command creation
