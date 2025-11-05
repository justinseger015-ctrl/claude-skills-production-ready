# RA/QM Team: Placeholder Script Migration Guide

**Date Created:** November 5, 2025
**Status:** 1 production script migrated, 11 placeholders documented
**Reference Standards:** `standards/cli-standards.md`

---

## Executive Summary

This guide documents the placeholder scripts across the RA/QM team skills library and provides a clear path for their implementation. Currently, 11 out of 12 RA/QM skills contain placeholder example scripts (19 lines each) that are not production-ready. This document explains why they were skipped in the initial migration and provides implementation guidance for when they become active.

**Current State:**
- **Production Scripts:** 1 (regulatory_tracker.py - migrated)
- **Placeholder Scripts:** 11 (ready for migration when implemented)
- **Migration Readiness:** 100% documented and ready to implement

---

## What Are Placeholder Scripts?

Placeholder scripts are skeleton implementations found in the `scripts/example.py` files across the RA/QM team. Each contains:

**Characteristics:**
- 19 lines of code (consistent across all 11 skills)
- Basic structure with `main()` function
- TODO comments indicating where actual logic should be implemented
- Example comments referencing other skills
- No actual compliance logic or data processing
- Marked as "not production-ready"

**Example Structure:**
```python
#!/usr/bin/env python3
"""Example helper script for [skill-name]

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.
"""

def main():
    print("This is an example script for [skill-name]")
    # TODO: Add actual script logic here

if __name__ == "__main__":
    main()
```

---

## Why Placeholder Scripts Were Skipped

### Reason 1: Not Production-Ready
These scripts contain no functional implementation. They serve as placeholders to indicate where production scripts should eventually be created. Migrating non-functional code to follow CLI standards would be premature before actual logic is defined.

### Reason 2: No Compliance Logic
Each placeholder lacks the core domain expertise:
- CAPA Officer: No root cause analysis logic
- Quality Managers: No QMS process handling
- Risk Management: No ISO 14971 analysis
- Security Manager: No ISMS controls
- Auditors: No audit workflows
- FDA/MDR Specialists: No submission validation
- GDPR Expert: No data protection assessment

### Reason 3: Focus on Quality Over Quantity
The migration strategy prioritizes migrating ONE production script perfectly (`regulatory_tracker.py`) over partially implementing 11 placeholders. This ensures:
- High-quality reference implementation
- Clear pattern for future migrations
- Documented standards compliance
- Real value delivered today

---

## Placeholder Scripts Inventory

### Strategic Leadership (2 skills)

**1. regulatory-affairs-head**
- Script: `regulatory-affairs-head/scripts/regulatory_tracker.py`
- Status: ✅ **MIGRATED TO PRODUCTION (v2.0.0)**
- Features: Regulatory submission tracking, compliance reporting (text/JSON output)
- Lines: 431 (was 199)

**2. quality-manager-qmr**
- Script: `quality-manager-qmr/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: Quality management review automation
- Future Features: QMS process validation, management review reporting
- Migration Priority: High (strategic QMS leadership)

### Quality Systems (3 skills)

**3. quality-manager-qms-iso13485**
- Script: `quality-manager-qms-iso13485/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: ISO 13485 compliance management
- Future Features: QMS process mapping, compliance documentation
- Migration Priority: High (ISO 13485 core competency)

**4. capa-officer**
- Script: `capa-officer/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: CAPA (Corrective and Preventive Action) management
- Future Features: Root cause analysis, CAPA tracking, effectiveness verification
- Migration Priority: High (QMS integral process)

**5. quality-documentation-manager**
- Script: `quality-documentation-manager/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: Quality documentation management
- Future Features: DHF/DMR/DHR document control, version tracking
- Migration Priority: Medium (supporting QMS function)

### Risk & Security (2 skills)

**6. risk-management-specialist**
- Script: `risk-management-specialist/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: ISO 14971 risk management
- Future Features: Risk assessment FMEA/FMECA, risk register management
- Migration Priority: High (regulatory requirement)

**7. information-security-manager-iso27001**
- Script: `information-security-manager-iso27001/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: ISO 27001 ISMS management
- Future Features: Security controls assessment, compliance audit
- Migration Priority: High (data protection critical)

### Regulatory Specialists (2 skills)

**8. mdr-745-specialist**
- Script: `mdr-745-specialist/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: EU MDR 2017/745 compliance
- Future Features: Technical documentation validation, MDR checklist
- Migration Priority: High (EU market requirement)

**9. fda-consultant-specialist**
- Script: `fda-consultant-specialist/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: FDA compliance (510(k), PMA, QSR)
- Future Features: FDA submission pathway analysis, regulatory requirements
- Migration Priority: High (US market critical)

### Audit & Compliance (3 skills)

**10. qms-audit-expert**
- Script: `qms-audit-expert/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: ISO 13485 internal audits
- Future Features: Audit planning, findings tracking, audit reporting
- Migration Priority: High (certification requirement)

**11. isms-audit-expert**
- Script: `isms-audit-expert/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: ISO 27001 security audits
- Future Features: Security audit workflows, control effectiveness assessment
- Migration Priority: Medium (supporting security function)

**12. gdpr-dsgvo-expert**
- Script: `gdpr-dsgvo-expert/scripts/example.py`
- Status: 📋 Placeholder (19 lines)
- Purpose: GDPR/DSGVO compliance
- Future Features: DPIA templates, data protection assessment
- Migration Priority: High (compliance requirement)

---

## Migration Pattern for Placeholders

When implementing placeholder scripts into production, follow this pattern:

### Step 1: Reference CLI Standards

Review `standards/cli-standards.md` for:
- Argparse ArgumentParser structure
- Required flags: `input`, `--output`, `--file`, `--verbose`
- Output formats: text (default), json
- Error handling and exit codes
- File validation and exception handling

### Step 2: Use Python CLI Template

Start from `templates/python-cli-template.py` which includes:
```python
#!/usr/bin/env python3
"""Description of what script does"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any

def process_content(content: str) -> Dict[str, Any]:
    """Main processing logic"""
    pass

def format_text_output(results: Dict[str, Any]) -> str:
    """Format as human-readable text"""
    pass

def format_json_output(results: Dict[str, Any]) -> str:
    """Format as JSON with metadata"""
    pass

def main():
    parser = argparse.ArgumentParser(
        description='[Purpose statement]',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  %(prog)s input.txt
  %(prog)s input.txt --output json
  %(prog)s input.txt -o json -f results.json -v
        """
    )

    parser.add_argument('input', help='Input file')
    parser.add_argument('--output', '-o', choices=['text', 'json'],
                       default='text', help='Output format')
    parser.add_argument('--file', '-f', help='Output file')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')

    args = parser.parse_args()
    # Implementation continues...
```

### Step 3: Domain-Specific Implementation

Implement actual domain logic:

**For CAPA Officer (root cause analysis):**
- Input: Problem description, affected systems
- Output: Root cause analysis results (text/JSON)
- Features: 5-Why analysis, Fishbone diagram, CAPA action plan

**For Risk Management (ISO 14971):**
- Input: Device description, intended use
- Output: Risk assessment results (text/JSON)
- Features: Risk matrix, FMEA scoring, risk evaluation

**For FDA Specialist (submission pathways):**
- Input: Device classification, predicate devices
- Output: Recommended submission pathway
- Features: 510(k)/De Novo/PMA determination, requirements checklist

**For Security Manager (ISO 27001):**
- Input: Asset inventory, security requirements
- Output: Security controls assessment (text/JSON)
- Features: Control gap analysis, remediation planning

### Step 4: Add to CLI Standards Compliance

Ensure compliance with standards:
```bash
# Test 1: Help flag works
python script.py --help

# Test 2: Input validation works
python script.py nonexistent.txt  # Should exit 1

# Test 3: JSON output works
python script.py input.txt --output json

# Test 4: File output works
python script.py input.txt -f output.txt

# Test 5: Verbose mode works
python script.py input.txt -v
```

### Step 5: Update SKILL.md

Update `SKILL.md` with new script documentation:

```markdown
### New Scripts

#### example_analysis.py

Automated analysis for [domain] compliance.

**Usage:**
```bash
python example_analysis.py input.txt
python example_analysis.py input.txt --output json
python example_analysis.py input.txt -o json -f results.json -v
```

**Parameters:**
- `input`: Data file for analysis
- `--output, -o`: Output format (text/json, default: text)
- `--file, -f`: Save results to file
- `--verbose, -v`: Detailed output including all findings

**Output Formats:**

*Text (Default):*
```
=== Analysis Results ===

Key Finding 1: ...
Key Finding 2: ...

Recommendations:
- Action 1
- Action 2
```

*JSON:*
```json
{
  "metadata": {
    "tool": "example_analysis.py",
    "version": "1.0.0",
    "timestamp": "2025-11-05T10:30:00Z"
  },
  "results": {
    "findings": [...],
    "recommendations": [...]
  }
}
```
```

### Step 6: Commit with Standards

Use conventional commits:
```bash
feat(capa-officer): implement root cause analysis script

- Add FMEA analysis engine
- Support JSON output for quality dashboard
- Add --verbose for detailed RCA output

Follows: standards/cli-standards.md
```

---

## Implementation Priority Roadmap

**Priority Tier 1 (Q4 2025)** - Core Quality Systems:
1. quality-manager-qmr - QMS oversight
2. capa-officer - Root cause analysis
3. quality-manager-qms-iso13485 - ISO 13485 compliance

**Priority Tier 2 (Q1 2026)** - Risk & Regulatory:
4. risk-management-specialist - ISO 14971 analysis
5. mdr-745-specialist - EU MDR compliance
6. fda-consultant-specialist - FDA pathways

**Priority Tier 3 (Q1 2026)** - Audit & Compliance:
7. qms-audit-expert - Internal audit workflows
8. information-security-manager-iso27001 - ISMS management
9. gdpr-dsgvo-expert - Data protection

**Priority Tier 4 (Q2 2026)** - Supporting Functions:
10. isms-audit-expert - Security audits
11. quality-documentation-manager - Doc control

---

## Related Standards

All placeholder migrations must comply with:

1. **CLI Standards** (`standards/cli-standards.md`)
   - Argparse implementation
   - Output format standardization
   - Error handling patterns
   - Exit code conventions

2. **Quality Standards** (`standards/quality/quality-standards.md`)
   - Code quality requirements
   - Testing requirements
   - Documentation standards
   - Validation checklist

3. **Git Workflow** (`standards/git/git-workflow-standards.md`)
   - Conventional commits
   - Feature branch strategy
   - PR requirements

---

## Testing Checklist for Placeholder Migration

When migrating a placeholder script, verify:

```
CLI Functionality:
  ☐ --help flag displays correctly
  ☐ --version flag shows script version
  ☐ Input file validation works (missing file error)
  ☐ --output text works
  ☐ --output json works
  ☐ --file creates output file
  ☐ --verbose adds detailed information
  ☐ Short flags (-o, -f, -v) work
  ☐ Long flags (--output, --file, --verbose) work

Error Handling:
  ☐ Missing input file: exits with code 1
  ☐ Invalid format: exits with code 3
  ☐ Permission denied: exits with code 4
  ☐ Unexpected error: exits with code 1

Output Quality:
  ☐ Text output is human-readable
  ☐ JSON is valid (parseable)
  ☐ JSON includes metadata section
  ☐ JSON timestamps are ISO 8601 format
  ☐ File output matches stdout output

Documentation:
  ☐ SKILL.md updated with usage examples
  ☐ Docstrings include parameter descriptions
  ☐ Examples in --help match SKILL.md
  ☐ No broken references or links
```

---

## Frequently Asked Questions

### Q: Why aren't these scripts being migrated now?
**A:** They are placeholders with no functional implementation. Migrating empty shells to follow CLI standards would provide no value. We focus on migrating production-ready code first (`regulatory_tracker.py` is the reference implementation) and providing clear guidance for future migrations.

### Q: When will the placeholder scripts be implemented?
**A:** Implementation follows the priority roadmap above, starting with core quality systems (Q4 2025) and continuing through audit & compliance functions (Q2 2026). Priority is determined by regulatory criticality and business value.

### Q: Can I implement a placeholder script myself?
**A:** Yes! Follow the pattern in this guide and reference `standards/cli-standards.md` and `templates/python-cli-template.py`. Submit a PR with conventional commits following the git standards.

### Q: What if I need a placeholder script implemented before its priority tier?
**A:** Submit a feature request documenting your use case. Priorities can be adjusted based on business needs. Contact the RA/QM team lead to discuss.

### Q: How do I test if my implementation matches standards?
**A:** Use the testing checklist above. All items must pass before submitting for review. Additionally, run:
```bash
python script.py --help
python script.py --version
python -m py_compile script.py
```

### Q: Do placeholder scripts need to support CSV output?
**A:** The standards recommend text + json as minimum. CSV is optional. Check domain-specific needs in SKILL.md before implementing.

---

## Reference Implementation

The reference implementation is `regulatory-affairs-head/scripts/regulatory_tracker.py` (v2.0.0), which demonstrates:

**What was migrated:**
- Added argparse with input positional argument
- Added --output flag (text/json)
- Added --file flag for output file
- Added --verbose flag for detailed info
- Implemented JSON output with metadata
- Enhanced text output with verbose details
- Full error handling and exit codes
- Examples in --help epilog

**Statistics:**
- Original: 199 lines
- Migrated: 431 lines
- New features: 3 major (JSON format, verbose output, file export)
- Migration time: ~1 hour
- CLI Standards compliance: 100%

**Key improvements:**
- Now integrates with compliance dashboards via JSON
- Supports all standard CLI flags
- Proper error handling with meaningful messages
- Verbose mode for detailed debugging
- File output for batch processing

---

## Contact & Support

For questions about placeholder script migration:

1. Review this guide: `ra-qm-team/PLACEHOLDER_MIGRATION_GUIDE.md`
2. Check CLI standards: `standards/cli-standards.md`
3. See reference implementation: `regulatory-affairs-head/scripts/regulatory_tracker.py`
4. Review template: `templates/python-cli-template.py`
5. Contact RA/QM team lead for scheduling implementations

---

**Document Version:** 1.0.0
**Last Updated:** November 5, 2025
**Status:** Complete - 1 production, 11 documented placeholders
**Next Review:** Q4 2025 (priority tier 1 implementations)

