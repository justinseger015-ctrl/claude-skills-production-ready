<!--
Sync Impact Report:
- Version change: [CONSTITUTION_VERSION] → 1.0.0
- Initial constitution creation for Claude Skills Library
- Established 7 core principles based on project practices documented in CLAUDE.md and README.md
- Added Development Workflow and Standards sections
- Templates requiring updates: ✅ No updates needed (initial creation)
- Follow-up TODOs: None
-->

# Claude Skills Library Constitution

## Core Principles

### I. Skills as Products
Every skill is a deployable, self-contained package that teams can extract and use immediately.

**Rules:**
- MUST include: SKILL.md (documentation), scripts/ (Python tools), references/ (knowledge bases), assets/ (templates)
- MUST be independently usable without dependencies on other skills
- MUST save users 40%+ time while improving consistency/quality by 30%+
- MUST NOT create cross-skill dependencies that reduce portability

**Rationale:** Skills are distributed as standalone packages, not application code. Each must function independently to maintain the library's modular architecture.

### II. Documentation-Driven Development
Success depends on clear, actionable documentation that users can follow immediately.

**Rules:**
- MUST provide step-by-step workflows with specific commands and expected outputs
- MUST use progressive disclosure: YAML frontmatter with keywords → Quick Start → Core Workflows → Tools → References
- MUST keep SKILL.md under 450 lines, moving comprehensive content to references/
- MUST include 15-30 discovery keywords in YAML frontmatter
- MUST NOT use generic advice; provide specific, platform-specific frameworks

**Rationale:** Users deploy skills by following documentation. Clear, structured docs with searchable keywords ensure fast adoption and correct usage.

### III. Algorithm Over AI
Use deterministic analysis (code) versus LLM calls for tool functionality.

**Rules:**
- Python CLI tools MUST use algorithmic analysis only (no ML/LLM API calls)
- MUST support --help, --version, --output flags
- MUST provide both JSON and human-readable output formats
- MUST use standard library or minimal dependencies (update requirements.txt)
- MUST be fast, portable, and executable without API keys

**Rationale:** Algorithmic tools are faster, more predictable, and don't require API access. This keeps skills portable and cost-free to run.

### IV. Template-Heavy Design
Provide ready-to-use templates that users customize rather than creating from scratch.

**Rules:**
- MUST include user-facing templates in assets/ directory
- Templates MUST be copy-paste ready with clear placeholder markers
- MUST provide examples for all major workflows
- MUST NOT provide templates without accompanying documentation

**Rationale:** Templates accelerate adoption and ensure consistency across implementations. Users adapt proven patterns rather than inventing new approaches.

### V. Platform-Specific Expertise
Deliver specific best practices for actual tools/platforms rather than generic guidance.

**Rules:**
- MUST provide tool-specific commands, configurations, and workflows
- MUST reference actual platform APIs, UI locations, and feature names
- MUST include platform version compatibility information where relevant
- MUST NOT offer abstract advice without concrete implementation details

**Rationale:** Generic advice has limited value. Users need actionable guidance for the specific tools they use daily.

### VI. Test-Validated Quality
All Python tools must pass standardized testing before deployment.

**Rules:**
- MUST support --help flag that displays usage information
- MUST handle file input and output correctly with UTF-8 encoding
- MUST provide proper exit codes (0 = success, 1 = error)
- MUST validate using test_cli_standards.sh before merging
- SHOULD achieve 100% pass rate across all automated tests

**Rationale:** Consistent quality and interface standards ensure all tools behave predictably. Users can trust that tools follow the same patterns.

### VII. Agent-Skill Separation
Agents orchestrate workflows; skills provide tools, knowledge, and templates.

**Rules:**
- **Skills** = Tools + Knowledge + Templates (the "what")
- **Agents** = Workflow Orchestrators (the "how")
- Agents MUST use relative paths (../../skill-package/) to access skills
- Agents MUST include YAML frontmatter with metadata (name, description, skills, domain, model, tools)
- Agents MUST document minimum 4 complete workflows
- Agents MUST use cs-* prefix convention

**Rationale:** Clear separation allows skills to be used independently while agents provide intelligent orchestration for complex tasks.

## Development Workflow

### Branch Strategy
develop → staging → main (test-validated direct push for solo development)

**Rules:**
- develop: Unit tests MUST pass before pushing
- staging: Full test suite MUST pass before deploying
- main: Complete validation MUST pass before production
- Teams MUST use feature branches with PRs; solo developers MAY push directly with test validation
- ALL commits MUST follow Conventional Commits format (feat, fix, docs, chore with scopes)

### Quality Gates
- Python syntax validation: `find . -name "*.py" -exec python3 -m py_compile {} \;`
- CLI standards testing: `./test_cli_standards.sh`
- Help flag validation: Test all tools with --help
- Path validation: Verify agent relative paths resolve correctly
- Secret detection: Check for exposed credentials before commit

## Standards and References

### Documentation Standards
- Git Workflow: [documentation/WORKFLOW.md](documentation/WORKFLOW.md)
- Git Standards: [standards/git/git-workflow-standards.md](standards/git/git-workflow-standards.md)
- CLI Standards: [documentation/standards/cli-standards.md](documentation/standards/cli-standards.md)
- Quality Standards: [standards/quality/](standards/quality/)
- Security Standards: [standards/security/](standards/security/)
- Communication Standards: [standards/communication/](standards/communication/)

### Key Anti-Patterns to Avoid
- Creating dependencies between skills (keep each self-contained)
- Adding complex build systems or test frameworks (maintain simplicity)
- Generic advice (focus on specific, actionable frameworks)
- LLM calls in scripts (defeats portability and speed)
- Over-documenting file structure (skills are simple by design)
- Hardcoding absolute paths in agents (always use ../../ pattern)
- Committing directly to main without tests (use quality gates)

## Governance

### Amendment Procedure
1. Propose changes via PR with rationale
2. Version bump according to semantic versioning:
   - MAJOR: Backward incompatible principle removals or redefinitions
   - MINOR: New principle/section added or materially expanded guidance
   - PATCH: Clarifications, wording, typo fixes, non-semantic refinements
3. Update dependent templates and documentation
4. Document changes in Sync Impact Report (HTML comment at top of file)
5. Require approval before merging

### Compliance Review
- All PRs MUST verify compliance with constitution principles
- Complexity MUST be justified against Principle VII (Simplicity implied in Test-Validated Quality)
- Use [CLAUDE.md](CLAUDE.md) for runtime development guidance
- Constitution supersedes all other practices in case of conflict

### Living Document
- This constitution evolves with the project
- Version increments track significant changes
- Regular review ensures alignment with project goals
- Feedback from users informs principle refinements

**Version**: 1.0.0 | **Ratified**: 2025-11-12 | **Last Amended**: 2025-11-12
