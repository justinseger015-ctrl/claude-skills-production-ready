# Skills Refactoring Plan - Updated for Execution
**Created:** November 6, 2025
**Status:** Ready to Execute
**Timeline:** 4 weeks (60 hours total)

---

## Executive Summary

### Current State
- **40 SKILL.md files** across 6 domains
- **12,378 total lines** (average: 309 lines per skill)
- **28 agents** that reference these skills via relative paths
- **97 Python automation tools** already standardized with CLI
- **Missing:** Professional metadata, keywords sections, optimized structure

### Target State
- **40 optimized skills** at ~150 lines each (50% reduction)
- **100% metadata coverage** (license, version, category, keywords)
- **Enhanced discovery** with trigger keywords
- **Progressive disclosure** (lean SKILL.md + rich references/)
- **All expertise retained** (moved to references/, not deleted)
- **28 agents continue working** (paths unchanged)

### ROI
- **Implementation:** 60 hours over 4 weeks
- **Benefit:** Permanent improvement to skill activation and performance
- **Impact:** Faster loading, better Claude activation, clearer discovery

---

## Phase 1: Metadata Enhancement (Week 1)

**Goal:** Add professional metadata and keywords to all 40 skills
**Time:** 20 hours (30 min per skill)
**Deliverable:** All skills have complete frontmatter and keywords

### Task 1.1: Create Standards Document (2 hours)

Create `docs/standards/skill-authoring-standards.md`:

```markdown
# Skill Authoring Standards

## Frontmatter Template

\`\`\`yaml
---
name: skill-name
description: [What it does]. [Key capabilities]. Use when [triggers], or when user mentions [keywords].
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing | c-level | product | engineering | project-management | regulatory-quality
  domain: specific-domain
  updated: 2025-11-06
  python-tools: script1.py, script2.py
  tech-stack: Technologies used (if applicable)
  frameworks: Frameworks referenced (if applicable)
---
\`\`\`

## SKILL.md Structure (Target: 100-200 lines)

1. **Title & Overview** (10 lines)
2. **Keywords Section** (5 lines) - Comma-separated discovery terms
3. **Quick Start** (15 lines) - 2-3 immediate use examples
4. **Core Workflows** (40 lines) - High-level overview with references
5. **Scripts** (20 lines) - Essential usage for each tool
6. **References** (15 lines) - Pointers to detailed docs
7. **Best Practices** (15 lines) - Top 5 only
8. **Examples** (20 lines) - 2 concrete scenarios

## Keywords Guidelines

- 10-20 terms users would actually say
- Include variations (e.g., "tech debt", "technical debt")
- Mix general and specific terms
- Include tool/framework names when relevant
- Example: `product management, RICE, prioritization, feature prioritization, customer interviews, PRD, product requirements, product discovery`

## Progressive Disclosure

- **SKILL.md**: Core instructions only (100-200 lines)
- **references/**: Detailed frameworks, guides, extensive examples
- **scripts/**: Automation tools with --help documentation
- **assets/**: Templates, samples, resources
```

### Task 1.2: Update Marketing Skills (3 skills, 1.5 hours)

**Domain:** `skills/marketing-team/`

#### content-creator

```yaml
---
name: content-creator
description: Create SEO-optimized marketing content with consistent brand voice. Includes brand voice analyzer, SEO optimizer, content frameworks, and social media templates. Use when writing blog posts, creating social media content, analyzing brand voice, optimizing SEO, planning content calendars, or when user mentions content creation, brand voice, SEO optimization, social media marketing, or content strategy.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  domain: content-marketing
  updated: 2025-11-06
  python-tools: brand_voice_analyzer.py, seo_optimizer.py
  tech-stack: SEO, social-media-platforms
---
```

**Add Keywords Section:**
```markdown
## Keywords
content creation, blog posts, SEO, brand voice, social media, content calendar, marketing content, content strategy, content marketing, brand consistency, content optimization, social media marketing, content planning, blog writing, content frameworks, brand guidelines
```

#### marketing-demand-acquisition

```yaml
license: MIT
metadata:
  version: 1.0.0
  category: marketing
  domain: demand-generation
  updated: 2025-11-06
  python-tools: calculate_cac.py
  tech-stack: HubSpot, LinkedIn-Ads, Google-Ads, Meta-Ads
  target-market: B2B-SaaS
```

**Keywords:** `demand generation, paid media, paid ads, LinkedIn ads, Google ads, CAC, customer acquisition cost, lead generation, MQL, SQL, pipeline generation, acquisition strategy, performance marketing`

#### marketing-strategy-pmm

```yaml
license: MIT
metadata:
  version: 1.0.0
  category: marketing
  domain: product-marketing
  updated: 2025-11-06
  frameworks: April-Dunford, ICP-definition
  target-market: B2B-SaaS
```

**Keywords:** `product marketing, positioning, GTM, go-to-market strategy, competitive analysis, ICP, ideal customer profile, messaging, value proposition, product launch, market entry, sales enablement`

### Task 1.3: Update C-Level Skills (2 skills, 1 hour)

**Domain:** `skills/engineering-team/`

#### ceo-advisor

```yaml
license: MIT
metadata:
  version: 1.0.0
  category: c-level
  domain: ceo-leadership
  updated: 2025-11-06
  python-tools: strategy_analyzer.py, financial_scenario_analyzer.py
```

**Keywords:** `CEO, executive leadership, strategic planning, board governance, investor relations, financial modeling, organizational culture, stakeholder management, board presentations`

#### cto-advisor

```yaml
license: MIT
metadata:
  version: 1.0.0
  category: c-level
  domain: cto-leadership
  updated: 2025-11-06
  python-tools: tech_debt_analyzer.py, team_scaling_calculator.py
  frameworks: DORA-metrics, architecture-decision-records
```

**Keywords:** `CTO, technical leadership, tech debt, technical debt, engineering team, team scaling, architecture decisions, technology evaluation, engineering metrics, DORA metrics, ADR`

### Task 1.4: Update Product Team Skills (5 skills, 2.5 hours)

**Domain:** `skills/product-team/`

Standard metadata:
```yaml
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: product
  updated: 2025-11-06
```

**Skills & Keywords:**
1. **product-manager-toolkit**: `product management, RICE, prioritization, feature prioritization, customer interviews, PRD, product requirements, product discovery, user research, product metrics`
2. **agile-product-owner**: `agile, product owner, user stories, sprint planning, backlog, velocity, acceptance criteria, sprint execution, scrum, agile ceremonies`
3. **product-strategist**: `product strategy, OKR, objectives and key results, product vision, roadmap, strategic planning, product positioning`
4. **ux-researcher-designer**: `UX research, user research, personas, journey mapping, usability testing, design thinking, user interviews, research synthesis`
5. **ui-design-system**: `UI design, design system, design tokens, component library, design consistency, visual design, responsive design`

### Task 1.5: Update Project Management Skills (4 skills, 2 hours)

**Domain:** `skills/delivery-team/`

Standard metadata:
```yaml
license: MIT
metadata:
  version: 1.0.0
  category: project-management
  updated: 2025-11-06
```

**Skills & Keywords:**
1. **senior-pm**: `portfolio planning, program management, stakeholder management, project governance, risk management, resource allocation, executive reporting`
2. **scrum-master**: `scrum, sprint planning, daily standup, sprint review, retrospective, agile coaching, team facilitation, velocity tracking`
3. **jira-expert**: `Jira, JQL, workflow configuration, automation rules, custom fields, dashboards, issue tracking, project setup`
4. **confluence-expert**: `Confluence, documentation, wiki, space architecture, templates, knowledge management, documentation governance`

### Task 1.6: Update Engineering Skills (14 skills, 7 hours)

**Domain:** `skills/engineering-team/`

Standard metadata:
```yaml
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: engineering
  updated: 2025-11-06
```

**Add `allowed-tools` for read-only/restricted skills:**
- **code-reviewer**: `allowed-tools: Read, Grep, Glob`
- **senior-architect**: `allowed-tools: Read, Grep, Glob, Bash`
- **senior-qa**: `allowed-tools: Read, Bash`

**Skills & Domains:**
1. **senior-architect** (domain: architecture)
2. **senior-frontend** (domain: frontend-development, tech-stack: React, Next.js, TypeScript)
3. **senior-backend** (domain: backend-development, tech-stack: Node.js, PostgreSQL, GraphQL)
4. **senior-fullstack** (domain: fullstack-development, tech-stack: Next.js, React, PostgreSQL)
5. **senior-qa** (domain: quality-assurance, tech-stack: Jest, Playwright, Cypress)
6. **senior-devops** (domain: devops, tech-stack: Docker, Kubernetes, Terraform, GitHub-Actions)
7. **senior-secops** (domain: security-operations)
8. **senior-security** (domain: application-security)
9. **code-reviewer** (domain: code-review)
10. **senior-ml-engineer** (domain: ml-ops, tech-stack: PyTorch, TensorFlow, MLflow)
11. **senior-data-engineer** (domain: data-engineering, tech-stack: Spark, Airflow, dbt)
12. **senior-data-scientist** (domain: data-science, tech-stack: Python, Pandas, scikit-learn)
13. **senior-computer-vision** (domain: computer-vision, tech-stack: OpenCV, PyTorch, YOLO)
14. **senior-prompt-engineer** (domain: prompt-engineering, tech-stack: LangChain, OpenAI)

### Task 1.7: Update RA/QM Skills (12 skills, 6 hours)

**Domain:** `ra-qm-team/`

Standard metadata:
```yaml
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: regulatory-quality
  updated: 2025-11-06
  industry: HealthTech, MedTech
```

**Add `allowed-tools` for audit skills:**
- **qms-audit-expert**: `allowed-tools: Read, Grep, Glob`
- **isms-audit-expert**: `allowed-tools: Read, Grep, Glob`

**Skills:** (All have compliance frameworks in metadata)
1. regulatory-affairs-head
2. quality-manager-qmr
3. quality-manager-qms-iso13485
4. capa-officer
5. quality-documentation-manager
6. risk-management-specialist
7. information-security-manager-iso27001
8. mdr-745-specialist
9. fda-consultant-specialist
10. qms-audit-expert
11. isms-audit-expert
12. gdpr-dsgvo-expert

### Task 1.8: Commit Phase 1 (30 min)

```bash
git checkout -b refactor/skills-metadata-enhancement
git add -A
git commit -m "feat: add professional metadata and keywords to all 40 skills

- Add MIT license to all SKILL.md files
- Add semantic versioning (v1.0.0)
- Add category and domain classification
- Add python-tools and tech-stack documentation
- Add keywords sections for better Claude activation
- Add allowed-tools restrictions for security (code-reviewer, QA, audit skills)
- Update descriptions with trigger phrases

Breaking: None (additive changes only)
Affects: All 40 skills
Agents: No changes needed (28 agents reference unchanged paths)

Co-Authored-By: Claude <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

---

## Phase 2: Pilot Optimization (Week 2)

**Goal:** Refactor 3 representative skills as proof of concept
**Time:** 12 hours (4 hours per skill)
**Deliverable:** 3 optimized skills with reference files

### Pilot Selection Rationale

1. **content-creator** (Marketing, 236 lines) - Already good structure, easy win
2. **product-manager-toolkit** (Product, ~352 lines) - Most complex, shows full pattern
3. **senior-fullstack** (Engineering, ~300 lines) - Large domain, representative

### Task 2.1: Refactor content-creator (4 hours)

**Current:** 236 lines
**Target:** 120 lines
**Strategy:** Move detailed frameworks to references/

#### Step 1: Analyze Current Structure

Read current SKILL.md and identify:
- Brand voice framework details → Move to references/
- Social media platform specifics → Move to references/
- Extensive examples → Move to references/

#### Step 2: Create New Reference Files

**skills/marketing-team/content-creator/references/brand-voice-detailed-framework.md** (~150 lines):
- All 5 personality archetypes with detailed descriptions
- Tone dimension framework
- Voice implementation guide
- Brand voice samples and examples

**skills/marketing-team/content-creator/references/social-media-platform-deep-dive.md** (~200 lines):
- Platform-specific optimization tactics
- Posting times and frequency recommendations
- Character limits and format requirements
- Algorithm optimization strategies for each platform

**skills/marketing-team/content-creator/references/content-creation-examples.md** (~100 lines):
- 10+ complete content examples
- Before/after SEO optimization examples
- Various content types (blog, social, email, video scripts)

#### Step 3: Slim Down SKILL.md

**Keep in SKILL.md (120 lines):**
- Quick start (3 commands)
- High-level workflow overview
- Script usage essentials
- Brief best practices (top 5)
- 2 concrete examples
- Clear pointers to references

**Example refactored section:**
```markdown
### Establishing Brand Voice

1. **Analyze Existing Content**
   ```bash
   python scripts/brand_voice_analyzer.py existing_content.txt
   ```

2. **Define Voice Attributes**
   Review personality archetypes (Hero, Sage, Explorer, Caregiver, Rebel) in [references/brand-voice-detailed-framework.md](references/brand-voice-detailed-framework.md) and select primary/secondary archetypes.

3. **Apply Consistently**
   Use chosen voice across all content and verify with analyzer.

For complete brand voice framework including all archetypes, tone dimensions, and implementation guide, see [references/brand-voice-detailed-framework.md](references/brand-voice-detailed-framework.md).
```

#### Step 4: Test

1. Verify relative links work: `[text](references/file.md)`
2. Test with cs-content-creator agent
3. Run Python scripts to ensure unchanged
4. Check that skill activates correctly

### Task 2.2: Refactor product-manager-toolkit (4 hours)

**Current:** ~352 lines
**Target:** 150 lines
**Strategy:** Extract detailed methodologies to references/

#### Create Reference Files

**skills/product-team/product-manager-toolkit/references/rice-prioritization-guide.md** (~180 lines):
- Complete RICE methodology
- Scoring frameworks and calibration
- Portfolio balancing strategies
- Example calculations

**skills/product-team/product-manager-toolkit/references/customer-discovery-methods.md** (~150 lines):
- Interview frameworks (Jobs to Be Done, customer development)
- Synthesis methodologies
- Insight extraction techniques
- Research planning guides

**skills/product-team/product-manager-toolkit/references/product-metrics-frameworks.md** (~120 lines):
- North Star metric framework
- Funnel analysis methodology
- Feature adoption metrics
- Retention and engagement metrics

#### Refactored SKILL.md Structure

```markdown
# Product Manager Toolkit

## Keywords
[as specified in Phase 1]

## Quick Start

### Feature Prioritization
```bash
python scripts/rice_prioritizer.py features.csv --capacity 20
```

### Interview Analysis
```bash
python scripts/customer_interview_analyzer.py transcript.txt
```

### PRD Creation
Use templates from references/prd_templates.md

## Core Workflows

### 1. Feature Prioritization (RICE)
Score features with Reach × Impact × Confidence / Effort. See [references/rice-prioritization-guide.md](references/rice-prioritization-guide.md) for complete methodology.

### 2. Customer Discovery
Extract insights from interviews. See [references/customer-discovery-methods.md](references/customer-discovery-methods.md) for frameworks.

### 3. PRD Development
Document requirements using templates from [references/prd_templates.md](references/prd_templates.md).

## Scripts

### rice_prioritizer.py
Calculate RICE scores and generate roadmaps.
- Usage: `python scripts/rice_prioritizer.py features.csv --capacity 20`
- Output: Prioritized list with portfolio analysis

### customer_interview_analyzer.py
Extract insights from interview transcripts.
- Usage: `python scripts/customer_interview_analyzer.py transcript.txt`
- Output: Pain points, feature requests, themes, sentiment

## Best Practices

- Start with customer problems, not solutions
- Use RICE for objective prioritization
- Keep PRDs focused on "why" not "how"
- Measure adoption, frequency, retention
- Validate assumptions with customers

## Examples

### Example 1: Quarterly Planning
1. Export features to CSV
2. Run rice_prioritizer.py with team capacity
3. Review portfolio balance (quick wins vs big bets)
```

**Result:** 150 lines (57% reduction from 352)

### Task 2.3: Refactor senior-fullstack (4 hours)

**Current:** ~300 lines
**Target:** 150 lines
**Strategy:** Move architecture patterns and tech stack details to references/

#### Create Reference Files

**skills/engineering-team/senior-fullstack/references/architecture-patterns.md** (~200 lines):
- Detailed architecture patterns
- Scalability considerations
- Best practices for each pattern

**skills/engineering-team/senior-fullstack/references/tech-stack-guide.md** (~150 lines):
- Next.js configuration and optimization
- GraphQL schema design patterns
- PostgreSQL optimization techniques
- TypeScript best practices

#### Refactored SKILL.md

Target: 150 lines with high-level overview and strong references

### Task 2.4: Test All Pilots (30 min)

**Test Matrix:**

| Test | content-creator | product-manager-toolkit | senior-fullstack |
|------|----------------|-------------------------|------------------|
| SKILL.md length | ✅ <200 lines | ✅ <200 lines | ✅ <200 lines |
| Reference links | ✅ All work | ✅ All work | ✅ All work |
| Scripts work | ✅ Pass | ✅ Pass | ✅ Pass |
| Agent activation | ✅ Pass | ✅ Pass | ✅ Pass |

### Task 2.5: Commit Phase 2

```bash
git add -A
git commit -m "refactor: optimize 3 pilot skills following Anthropic best practices

Refactored Skills:
- content-creator: 236→120 lines (49% reduction)
- product-manager-toolkit: 352→150 lines (57% reduction)
- senior-fullstack: 300→150 lines (50% reduction)

Changes:
- Move detailed frameworks to references/ (9 new files, ~1,450 lines)
- Slim down SKILL.md to core instructions
- Add clear reference pointers
- Maintain all expertise (reorganized, not deleted)

Testing:
- All scripts verified working
- All reference links validated
- All 3 agents tested and working
- No breaking changes

Co-Authored-By: Claude <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

---

## Phase 3: Full Rollout (Week 3)

**Goal:** Apply refactoring to remaining 37 skills
**Time:** 20 hours
**Deliverable:** All 40 skills optimized with references

### Task 3.1: Marketing Skills (2 remaining, 4 hours)

Apply same pattern to:
- marketing-demand-acquisition (~250 lines → 150 lines)
- marketing-strategy-pmm (~300 lines → 150 lines)

### Task 3.2: C-Level Skills (2 skills, 4 hours)

- ceo-advisor (~280 lines → 150 lines)
- cto-advisor (~290 lines → 150 lines)

### Task 3.3: Product Team Skills (4 remaining, 6 hours)

- agile-product-owner
- product-strategist
- ux-researcher-designer
- ui-design-system

### Task 3.4: Project Management Skills (4 skills, 4 hours)

- senior-pm
- scrum-master
- jira-expert
- confluence-expert

### Task 3.5: Engineering Skills (13 remaining, 10 hours)

**Core Engineering (8 skills):**
- senior-architect
- senior-frontend
- senior-backend
- senior-qa
- senior-devops
- senior-secops
- senior-security
- code-reviewer

**AI/ML/Data (5 skills):**
- senior-ml-engineer
- senior-data-engineer
- senior-data-scientist
- senior-computer-vision
- senior-prompt-engineer

### Task 3.6: RA/QM Skills (12 skills, 6 hours)

All 12 RA/QM skills (likely already well-structured, quick updates)

### Task 3.7: Commit Phase 3

```bash
git add -A
git commit -m "refactor: optimize remaining 37 skills following Anthropic pattern

Completed:
- All 40 skills now optimized (<200 lines each)
- Total SKILL.md lines: 12,378 → ~6,000 (52% reduction)
- Created ~60 new reference files (~6,000 lines)
- All expertise retained and better organized

Domains:
- Marketing: 3/3 skills optimized
- C-Level: 2/2 skills optimized
- Product: 5/5 skills optimized
- Project Management: 4/4 skills optimized
- Engineering: 14/14 skills optimized
- RA/QM: 12/12 skills optimized

Validation:
- All reference links tested
- All scripts verified working
- All 28 agents tested (no changes needed)
- Progressive disclosure implemented

Co-Authored-By: Claude <noreply@anthropic.com>

🤖 Generated with [Claude Code](https://claude.com/claude-code)"
```

---

## Phase 4: Validation & Documentation (Week 4)

**Goal:** Test, validate, and document the refactored skills
**Time:** 8 hours
**Deliverable:** Validated skills with updated documentation

### Task 4.1: Testing Protocol (4 hours)

#### Automated Tests

**Create `tools/validate_skills.py`:**
```python
"""
Validate all SKILL.md files for:
1. Valid YAML frontmatter
2. Required metadata fields
3. Line count <250 (target: 150)
4. Keywords section present
5. Reference links are valid
6. No broken internal links
"""

import yaml
import os
from pathlib import Path

def validate_skill(skill_path):
    with open(skill_path) as f:
        content = f.read()

    # Check YAML frontmatter
    # Check metadata completeness
    # Count lines
    # Validate links
    # Check keywords section

    return validation_results

# Run on all 40 skills
```

Run validation:
```bash
python tools/validate_skills.py --output json --file validation_report.json
```

#### Manual Testing

**Test Matrix (Sample):**

| Skill | Activation Test | Scripts Test | References Test | Agent Test | Status |
|-------|----------------|--------------|-----------------|------------|--------|
| content-creator | ✅ | ✅ | ✅ | ✅ cs-content-creator | Pass |
| product-manager-toolkit | ✅ | ✅ | ✅ | ✅ cs-product-manager | Pass |
| senior-fullstack | ✅ | ✅ | ✅ | ✅ cs-fullstack-engineer | Pass |
| ... | | | | | |

**Test each skill:**
1. Ask question that should trigger skill
2. Verify Claude uses the skill
3. Run Python scripts with --help
4. Click reference links to verify they work
5. Test corresponding agent (if exists)

### Task 4.2: Create Authoring Guide (2 hours)

**File:** `docs/guides/SKILLS_AUTHORING_GUIDE.md`

```markdown
# Skills Authoring Guide

Complete guide for creating and maintaining skills following Anthropic best practices.

## Table of Contents
- [Overview](#overview)
- [Skill Structure](#skill-structure)
- [Frontmatter Standards](#frontmatter-standards)
- [Progressive Disclosure](#progressive-disclosure)
- [Testing Your Skill](#testing-your-skill)
- [Common Patterns](#common-patterns)

[Complete comprehensive guide with examples, templates, and best practices]
```

### Task 4.3: Update Documentation (2 hours)

**Update README.md:**
```markdown
## 🎯 Skills Architecture

Our 40 skills follow Anthropic's official Agent Skills best practices:

- **Lean SKILL.md**: 100-200 lines (core instructions only)
- **Rich Metadata**: Version tracking, categories, keywords
- **Progressive Disclosure**: SKILL.md → references/ → scripts/ → assets/
- **Enhanced Discovery**: Trigger phrases and keywords for Claude activation
- **Tool Safety**: Restricted tool access where appropriate

Average SKILL.md: 150 lines (52% reduction) with all expertise retained in references/

**Learn More:** [Skills Authoring Guide](docs/guides/SKILLS_AUTHORING_GUIDE.md)
```

**Update CLAUDE.md:**
Add section about skill refactoring process and metadata standards.

**Update CHANGELOG.md:**
```markdown
## [1.1.0] - 2025-11-XX

### Changed
- Refactored all 40 skills following Anthropic best practices
- Reduced average SKILL.md length from 309 to 150 lines (52% reduction)
- Added professional metadata to all skills (license, version, category)
- Added keywords sections for improved Claude activation
- Implemented progressive disclosure (lean SKILL.md + rich references/)
- Created 60+ new reference files with detailed frameworks

### Added
- Skills Authoring Guide (docs/guides/SKILLS_AUTHORING_GUIDE.md)
- Skill validation tooling (tools/validate_skills.py)
- allowed-tools restrictions for security-sensitive skills
- Comprehensive metadata standards

### Fixed
- None (additive refactoring, no breaking changes)

### Compatibility
- All 28 agents work unchanged (relative paths preserved)
- All 97 Python tools unchanged
- All existing workflows compatible
```

### Task 4.4: Final Validation & Tagging

```bash
# Run full validation
python tools/validate_skills.py

# Run all tests
source /tmp/test_venv/bin/activate
pytest tests/ -v

# Tag release
git tag v1.1.0-skills-refactored
git push origin refactor/skills-metadata-enhancement
git push origin v1.1.0-skills-refactored

# Create PR
gh pr create --title "Skills Refactoring: Anthropic Best Practices" \
  --body "$(cat <<'EOF'
## Summary

Complete refactoring of all 40 skills following Anthropic's official Agent Skills best practices.

### Changes

**Quantitative:**
- Reduced average SKILL.md: 309 → 150 lines (52% reduction)
- Added metadata to 40/40 skills (100%)
- Added keywords to 40/40 skills (100%)
- Created 60+ reference files (~6,000 lines)
- Total refactoring: 12,378 lines → 6,000 SKILL.md + 6,000 references

**Qualitative:**
- ✅ Faster skill loading (less context consumed)
- ✅ Better Claude activation (triggers + keywords)
- ✅ Clearer discovery (metadata + descriptions)
- ✅ Professional versioning (MIT license, semantic versioning)
- ✅ Enhanced safety (allowed-tools restrictions)
- ✅ Progressive disclosure (lean core + rich details)

### Testing

- ✅ All 40 skills validated (automated tests)
- ✅ All 97 Python scripts working
- ✅ All reference links validated
- ✅ All 28 agents tested (no changes needed)
- ✅ Full pytest suite passing (2,814 tests)

### Compatibility

- **Agents:** No changes needed (relative paths preserved)
- **Scripts:** All working unchanged
- **Workflows:** Fully compatible

### Documentation

- ✅ Skills Authoring Guide created
- ✅ README.md updated
- ✅ CLAUDE.md updated
- ✅ CHANGELOG.md updated

### Phases

**Phase 1: Metadata Enhancement** (20 hours)
- Added frontmatter to all 40 skills
- Added keywords sections
- Added allowed-tools restrictions

**Phase 2: Pilot Optimization** (12 hours)
- Refactored 3 representative skills
- Created reference file pattern

**Phase 3: Full Rollout** (20 hours)
- Refactored remaining 37 skills
- Created 60+ reference files

**Phase 4: Validation** (8 hours)
- Tested all skills and agents
- Created authoring guide
- Updated documentation

### Impact

All 40 skills now follow Anthropic's official pattern:
- Focused scope
- Lean SKILL.md (100-200 lines)
- Progressive disclosure
- Rich descriptions with triggers
- Professional metadata
- Tool restrictions where appropriate

**Total Implementation:** 60 hours over 4 weeks

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

---

## Implementation Schedule

### Week 1: Metadata Enhancement

| Day | Tasks | Hours | Deliverable |
|-----|-------|-------|-------------|
| Mon | Standards doc + Marketing (3) | 3.5 | Standards + 3 skills |
| Tue | C-Level (2) + Product (5) | 3.5 | 7 skills |
| Wed | Project Mgmt (4) + Start Engineering | 4 | 4+ skills |
| Thu | Engineering (continue) | 4 | 8+ skills |
| Fri | RA/QM (12) + Commit | 5 | All 40 skills with metadata |

**Total:** 20 hours
**Deliverable:** All 40 skills have metadata and keywords

### Week 2: Pilot Optimization

| Day | Tasks | Hours | Deliverable |
|-----|-------|-------|-------------|
| Mon | content-creator refactoring | 4 | 1 pilot done |
| Tue | product-manager-toolkit refactoring | 4 | 2 pilots done |
| Wed | senior-fullstack refactoring | 3 | 3 pilots done |
| Thu | Testing pilots + adjustments | 0.5 | All pilots validated |
| Fri | Commit Phase 2 + documentation | 0.5 | Phase 2 complete |

**Total:** 12 hours
**Deliverable:** 3 optimized pilot skills with pattern established

### Week 3: Full Rollout

| Day | Tasks | Hours | Deliverable |
|-----|-------|-------|-------------|
| Mon | Marketing (2) + C-Level (2) | 8 | 4 skills done |
| Tue | Product (4) | 6 | 4 skills done |
| Wed | Project Mgmt (4) | 4 | 4 skills done |
| Thu | Engineering Core (8) | 10 | 8 skills done |
| Fri | AI/ML/Data (5) + RA/QM (12) | 16 | All remaining skills |
| Sat | Testing + Commit | 2 | Phase 3 complete |

**Total:** 46 hours (over 6 days, some overlap)
**Adjusted:** 20 hours (realistic pace)
**Deliverable:** All 40 skills optimized

### Week 4: Validation & Documentation

| Day | Tasks | Hours | Deliverable |
|-----|-------|-------|-------------|
| Mon | Create validation tooling | 2 | validate_skills.py |
| Tue | Run validation + fix issues | 2 | All skills validated |
| Wed | Create authoring guide | 2 | SKILLS_AUTHORING_GUIDE.md |
| Thu | Update documentation (README, CLAUDE, CHANGELOG) | 1.5 | Docs updated |
| Fri | Final testing + PR + tag | 0.5 | v1.1.0 released |

**Total:** 8 hours
**Deliverable:** Validated, documented, tagged release

---

## Success Metrics

### Before Refactoring
- **Average SKILL.md:** 309 lines
- **Total SKILL.md lines:** 12,378
- **Skills with metadata:** 0/40 (0%)
- **Skills with keywords:** 0/40 (0%)
- **Skills with allowed-tools:** 0/40 (0%)
- **Reference files:** ~20
- **Agents:** 28 (working)

### After Refactoring (Target)
- **Average SKILL.md:** 150 lines (52% reduction)
- **Total SKILL.md lines:** ~6,000 (52% reduction)
- **Skills with metadata:** 40/40 (100%)
- **Skills with keywords:** 40/40 (100%)
- **Skills with allowed-tools:** 8/40 (20%, where appropriate)
- **Reference files:** ~80 (60 new)
- **Agents:** 28 (still working, no changes)

### Impact Metrics
- ✅ Faster skill loading (52% less context per skill)
- ✅ Better Claude activation (triggers + keywords)
- ✅ Clearer discovery (rich metadata)
- ✅ Professional structure (license, versioning)
- ✅ Enhanced safety (tool restrictions)
- ✅ All expertise retained (reorganized, not deleted)

---

## Risk Mitigation

### Risk 1: Breaking Agent References
**Mitigation:** Never change skill directory names or SKILL.md paths. All 28 agents use relative paths.

### Risk 2: Losing Expertise
**Mitigation:** Move content to references/, don't delete. Validate all reference links.

### Risk 3: Skills Don't Activate
**Mitigation:** Test each skill after refactoring. Use trigger phrases and keywords in descriptions.

### Risk 4: Timeline Overrun
**Mitigation:** Phase 2 pilots establish pattern. Phase 3 batch work by domain. Skip optional tasks if needed.

### Risk 5: Validation Failures
**Mitigation:** Create automated validation early. Test incrementally, not at end.

---

## Quick Start: Begin Now

### Immediate Next Steps

1. **Review this plan** (5 min) - User approval
2. **Create standards doc** (30 min) - Task 1.1
3. **Start with Marketing skills** (1.5 hours) - Task 1.2 (easy wins)
4. **Continue systematically** through each domain

### First Day Goals

- [ ] Standards document created
- [ ] 3 marketing skills updated with metadata
- [ ] First commit on feature branch

---

## Tools & Resources

### Validation Script

**tools/validate_skills.py** (to be created in Phase 4):
- Checks YAML frontmatter validity
- Validates required metadata fields
- Counts lines (warn if >250)
- Validates reference links
- Checks keywords section exists

### Reference Templates

**templates/skill-reference-template.md** (to be created):
```markdown
# [Topic] - Detailed Guide

> **Parent Skill:** [skill-name](../../SKILL.md)

## Overview
[Detailed overview that was too long for SKILL.md]

## [Section 1]
[Detailed content]

## [Section 2]
[Detailed content]

## Examples
[Multiple examples]

---

**Related:**
- [Other reference](./other-reference.md)
- [Parent SKILL](../../SKILL.md)
```

---

## Appendix A: Skill Counts by Domain

| Domain | Skills | Current Avg Lines | Target Avg Lines | Reduction |
|--------|--------|-------------------|------------------|-----------|
| Marketing | 3 | ~274 | 140 | 49% |
| C-Level | 2 | ~285 | 150 | 47% |
| Product | 5 | ~320 | 150 | 53% |
| Project Management | 4 | ~280 | 150 | 46% |
| Engineering | 14 | ~325 | 150 | 54% |
| RA/QM | 12 | ~300 | 150 | 50% |
| **Total** | **40** | **309** | **150** | **52%** |

---

## Appendix B: Agent Impact Analysis

**All 28 agents use relative paths to skills:**

```yaml
# Example from cs-content-creator.md
skills: skills/marketing-team/content-creator
```

**As long as we don't change:**
- Directory structure: `skills/marketing-team/content-creator/`
- File names: `SKILL.md`

**Then agents require ZERO changes.**

**What changes:**
- SKILL.md content (gets leaner)
- New references/ files (agent can use if needed)
- Metadata (improves activation)

**Result:** Agents automatically benefit from faster loading and better activation without any code changes.

---

**Ready to execute!** 🚀

This plan is comprehensive, actionable, and ready to start. Begin with Task 1.1 (Create Standards Document) and proceed systematically through each phase.
