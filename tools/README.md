# Testing Tools

This directory contains shell scripts for testing and validating Python CLI tools across the repository.

## Available Tools

### test_single_script.sh

**Purpose:** Comprehensive testing of a single Python script

**Usage:**
```bash
# Basic test (checks syntax, argparse, --help)
./tools/test_single_script.sh path/to/script.py

# Full test with sample input (all 10 checks)
./tools/test_single_script.sh path/to/script.py path/to/sample_input.txt
```

**What it tests:**
1. Python syntax validity
2. Uses argparse (not manual sys.argv)
3. Has main() function
4. `--help` flag works
5. `--version` flag (optional)
6. Standard flags documented (--output, --file, --verbose)
7. Execution with sample input
8. JSON output validity
9. File output creation
10. Verbose mode

**Example:**
```bash
./tools/test_single_script.sh \
  marketing-skill/content-creator/scripts/brand_voice_analyzer.py \
  marketing-skill/content-creator/assets/sample-content.txt
```

---

### test_cli_standards.sh

**Purpose:** Batch testing of all Python scripts in the repository

**Usage:**
```bash
./tools/test_cli_standards.sh
```

**What it tests:**
- `--help` flag works
- Python syntax valid
- Uses argparse
- Has main() function

**Output:**
```
Testing: brand_voice_analyzer.py
  ✓ --help flag works
  ✓ Python syntax valid
  ✓ Uses argparse
  ✓ Has main() function
  PASSED (4 checks)

========================================
Test Summary:
  Total scripts tested: 67
  Passed: 67
  Failed: 0
========================================
```

---

## Documentation

For complete testing documentation, see:
- [TESTING_GUIDE.md](../TESTING_GUIDE.md) - Comprehensive testing guide
- [TESTING_QUICK_START.md](../TESTING_QUICK_START.md) - Quick reference
- [documentation/standards/cli-standards.md](../documentation/standards/cli-standards.md) - CLI standards

## CI/CD Integration

These tests are also run automatically in GitHub Actions:
- See [.github/workflows/ci-quality-gate.yml](../.github/workflows/ci-quality-gate.yml)
- Tests run on all pull requests
- 2,814 automated pytest tests (100% pass rate)

---

**Last Updated:** November 17, 2025
