# Contributing to Claude Skills Library - Pandora Edition

Thank you for your interest in contributing to Pandora's Skills Library! This document provides guidelines for contributing improvements, new skills, and bug fixes.

## 🎯 Contribution Philosophy

This repository focuses on **Pandora's software delivery lifecycle (SDLC)**. Contributions should support:
- Architecture analysis and system design
- Security auditing and vulnerability detection
- Product management and feature prioritization
- Engineering best practices and automation
- Delivery workflows and team collaboration

## 🚀 How to Contribute

### 1. Fork and Branch

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/claude-skills.git
cd claude-skills

# Create a feature branch
git checkout -b feature/your-contribution-name
```

### 2. Make Your Changes

Follow the architecture guidelines in [CLAUDE.md](CLAUDE.md) when:
- Creating new skills
- Adding Python tools
- Updating documentation
- Improving existing functionality

### 3. Test Your Changes

```bash
# Test Python tools
python3 your-new-tool.py --help
python3 your-new-tool.py test-input.txt

# Verify documentation renders correctly
# Check that all links work
# Ensure examples are accurate
```

### 4. Commit and Push

```bash
# Use conventional commit format
git add .
git commit -m "feat(skills): add new architecture analysis tool"
git push origin feature/your-contribution-name
```

### 5. Submit Pull Request

- Create a PR from your fork to `rickydwilson-dcs/claude-skills:main`
- Provide clear description of changes
- Reference any related issues
- Wait for review and address feedback

## 💡 Contribution Ideas

### High Priority
- **New SDLC Skills** - Skills that accelerate software delivery
- **Tool Enhancements** - Improve existing Python analysis scripts
- **Security Improvements** - Enhance security scanning capabilities
- **Architecture Patterns** - Add new architectural analysis patterns

### Medium Priority
- **Documentation** - Improve how-to guides and examples
- **Templates** - Add ADR, PRD, or design templates
- **Framework Additions** - Enhance existing skill frameworks
- **Bug Fixes** - Fix issues in scripts or documentation

### Lower Priority
- **Marketing Skills** - Content creation tools for product launches
- **Process Improvements** - CI/CD, testing, automation
- **Translations** - Documentation in other languages

## ✅ Quality Standards

All contributions must meet these standards:

### For New Skills
- ✅ **SDLC-focused** - Supports software delivery lifecycle
- ✅ **Self-contained** - Independently deployable skill package
- ✅ **Comprehensive docs** - Complete SKILL.md with workflows
- ✅ **Actionable guidance** - Specific, not generic advice
- ✅ **Python tools** - Algorithmic analysis when possible
- ✅ **Templates included** - Ready-to-use assets
- ✅ **Zero dependencies** - Python 3.8+ standard library only

### For Python Tools
- ✅ **CLI-first** - Support `--help`, `--version`, `--output` flags
- ✅ **Multiple formats** - Text (human) and JSON (machine) output
- ✅ **Error handling** - Proper exit codes and error messages
- ✅ **UTF-8 support** - Handle international characters
- ✅ **Standard library** - No external dependencies
- ✅ **Type hints** - Use Python type annotations
- ✅ **Docstrings** - Document functions and classes

### For Documentation
- ✅ **Accuracy** - All examples must work as shown
- ✅ **SDLC examples** - Focus on architecture, security, product
- ✅ **Clear structure** - Logical organization and headings
- ✅ **Working links** - All references must be valid
- ✅ **Consistent style** - Follow existing documentation patterns

## 🏗️ Skill Architecture Pattern

New skills must follow this structure:

```
skill-name/
├── SKILL.md              # Master documentation
├── scripts/              # Python CLI tools
│   ├── tool1.py
│   └── tool2.py
├── references/           # Knowledge bases (markdown)
│   ├── patterns.md
│   └── best-practices.md
└── assets/               # Templates and examples
    ├── template1.md
    └── template2.md
```

See [templates/skill-template.md](templates/skill-template.md) for the complete template.

## 🔍 Code Review Process

1. **Automated Checks** - GitHub Actions run tests
2. **Manual Review** - Maintainers review code and docs
3. **Feedback** - Address requested changes
4. **Approval** - Maintainer approves PR
5. **Merge** - Changes merged to main branch

## 📋 Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows Python style guidelines (PEP 8)
- [ ] All Python tools have `--help` and work correctly
- [ ] Documentation is accurate and complete
- [ ] Examples use SDLC-focused scenarios
- [ ] No external dependencies added (unless justified)
- [ ] Commit messages follow conventional format
- [ ] PR description explains what and why
- [ ] All tests pass locally

## 🚫 What NOT to Contribute

Please avoid:
- **Generic advice** - Be specific and actionable
- **External dependencies** - Stick to standard library
- **Non-SDLC skills** - Focus on software delivery
- **Marketing-first content** - SDLC is primary focus
- **Duplicate functionality** - Check existing skills first
- **Unverified claims** - Don't add baseless ROI metrics

## 🤝 Getting Help

- **Questions?** Open a [GitHub Discussion](https://github.com/rickydwilson-dcs/claude-skills/discussions)
- **Found a bug?** Open a [GitHub Issue](https://github.com/rickydwilson-dcs/claude-skills/issues)
- **Need clarification?** Check [CLAUDE.md](CLAUDE.md) or ask in discussions

## 📜 Code of Conduct

- Be respectful and constructive
- Focus on what's best for Pandora's teams
- Provide helpful feedback
- Assume good intentions
- Follow GitHub's Community Guidelines

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License, with copyright retained by the original author (Alireza Rezvani) and modifications by Pandora contributors.

---

**Thank you for contributing to Pandora's Skills Library!** 🎉

Your contributions help accelerate software delivery and improve quality across Pandora's development teams.
