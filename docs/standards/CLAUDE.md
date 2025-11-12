# Standards Library - Claude Code Guidance

**Purpose:** Enforced quality standards for all skills, agents, and documentation in the Pandora edition.

## Available Standards

All standards are located in `docs/standards/`:

| Standard | File | Purpose |
|----------|------|---------|
| **Communication** | [communication-standards.md](communication-standards.md) | Clear, actionable documentation |
| **Quality** | [quality-standards.md](quality-standards.md) | Code quality, testing, zero defects |
| **Git Workflow** | [git-workflow-standards.md](git-workflow-standards.md) | Conventional commits, branching |
| **Documentation** | [documentation-standards.md](documentation-standards.md) | Markdown quality, living docs |
| **Security** | [security-standards.md](security-standards.md) | Secret detection, input validation |
| **CLI** | [cli-standards.md](cli-standards.md) | Python tool CLI design |
| **Anthropic Validation** | [anthropic-skill-validation.md](anthropic-skill-validation.md) | Skill package requirements |

## Quick Reference

### Before Creating a New Skill

```bash
# Review these standards in order:
cat docs/standards/quality-standards.md          # Python tool requirements
cat docs/standards/cli-standards.md              # CLI design patterns
cat docs/standards/documentation-standards.md    # SKILL.md format
cat docs/standards/security-standards.md         # Security requirements
```

### Before Creating a New Agent

```bash
# Review these standards in order:
cat docs/standards/quality-standards.md          # Workflow quality
cat docs/standards/documentation-standards.md    # Agent documentation
cat docs/standards/communication-standards.md    # Clear guidance
```

### Before Committing Code

```bash
# Check compliance:
cat docs/standards/git-workflow-standards.md     # Conventional commits
cat docs/standards/security-standards.md         # No secrets check
```

## Standards Enforcement Priority

Standards are enforced in this order (highest to lowest priority):

1. **Security** - Non-negotiable. No secrets, validated input, secure dependencies.
2. **Quality** - Zero defect handoff. All tools must work, all agents tested.
3. **Git** - Conventional commits for all changes. Branch strategy followed.
4. **Documentation** - Living docs stay current. No broken links.
5. **Communication** - Clear, pragmatic, actionable guidance.
6. **CLI** - Python tools follow CLI standards (--help, JSON output, exit codes).

## Pre-Commit Checklist

**Required before every commit:**

- [ ] **Security**: No hardcoded secrets (API keys, passwords, tokens)
- [ ] **Security**: All user input validated
- [ ] **Quality**: Python tools tested with `--help` flag
- [ ] **Quality**: Agent relative paths verified (if applicable)
- [ ] **Git**: Conventional commit format (`type(scope): description`)
- [ ] **Documentation**: CLAUDE.md files updated (if structure changed)
- [ ] **CLI**: Tools support both human-readable and JSON output

## Common Violations

**Most frequent standards violations to avoid:**

1. ❌ Committing with message "updated files" → ✅ Use `feat(agents): add workflow X`
2. ❌ Hardcoding paths like `/Users/name/project/` → ✅ Use relative paths `../../skills/`
3. ❌ Creating new files unnecessarily → ✅ Edit existing files
4. ❌ Python tools without `--help` support → ✅ All tools must have `--help`
5. ❌ Vague documentation like "handles errors" → ✅ Specific: "Validates email format, returns 400 on invalid"

---

**Last Updated:** November 12, 2025
**Standards Count:** 7 comprehensive standards
**Enforcement:** Required for all commits to develop/staging/main
