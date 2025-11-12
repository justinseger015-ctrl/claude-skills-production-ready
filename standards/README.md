# Standards Library

This directory contains the core standards that govern all skills and agents in the claude-skills repository.

## Available Standards

### [Communication Standards](communication/communication-standards.md)
Defines how agents and skills communicate with users:
- Absolute honesty and zero fluff
- Pragmatic, actionable solutions
- Critical analysis requirements
- Prohibited response patterns

### [Quality Standards](quality/quality-standards.md)
Code quality and testing requirements:
- Testing methodology (pytest framework)
- Code review checklist
- Performance benchmarks
- Quality gates

### [Git Workflow Standards](git/git-workflow-standards.md)
Version control best practices:
- Conventional commits format
- Branch naming conventions
- PR requirements and templates
- Commit message guidelines

### [Documentation Standards](documentation/documentation-standards.md)
Documentation structure and formatting:
- Markdown conventions
- File naming patterns
- Required sections for SKILL.md
- Living documentation principles

### [Security Standards](security/security-standards.md)
Security and compliance requirements:
- Secret detection and prevention
- Dependency scanning
- Security review checklist
- Vulnerability reporting

## Usage

### For Agents
Reference standards when orchestrating workflows:

```markdown
## References
- [Communication Standards](../../standards/communication/communication-standards.md)
- [Quality Standards](../../standards/quality/quality-standards.md)
```

### For Skills
Follow standards when building new tools and documentation:
- Use quality standards for Python CLI tools
- Follow git standards for version control
- Apply documentation standards for SKILL.md files
- Implement security standards for sensitive operations

## Integration

Standards are designed to be:
- **Non-invasive**: Reference-based, not enforced by tooling
- **Living**: Updated based on community feedback
- **Practical**: Focus on actionable guidelines
- **Universal**: Apply across all domains (marketing, engineering, product, etc.)

## Contributing

To propose changes to standards:
1. Open an issue describing the proposed change
2. Reference specific use cases or pain points
3. Suggest concrete improvements
4. Follow the git workflow standards for PRs

---

**Last Updated:** November 8, 2025
**Related Documentation:** [Main CLAUDE.md](../CLAUDE.md), [Agent Development Guide](../agents/CLAUDE.md)
