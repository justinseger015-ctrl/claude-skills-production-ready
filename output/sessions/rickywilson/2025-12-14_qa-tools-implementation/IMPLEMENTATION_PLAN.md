# Priority 8: QA Tools Implementation Plan

**Session:** 2025-12-14_qa-tools-implementation
**Target:** 3 Python scripts for senior-qa skill
**Path:** `skills/engineering-team/senior-qa/scripts/`

---

## Executive Summary

Implement 3 production-ready QA Python tools that are currently placeholders (139-160 lines each with no actual logic). Each script must use Python standard library only and follow the patterns established by existing implementations like `fixture_generator.py` (454 lines).

**Estimated Total:** ~2,100-2,400 lines of code (700-800 per script)

---

## Current State Analysis

### Placeholder Scripts (To Be Implemented)

| Script | Current Lines | Status | Implementation Needed |
|--------|--------------|--------|----------------------|
| `coverage_analyzer.py` | 139 | Placeholder | Coverage report parsing, gap identification, trend analysis |
| `e2e_test_scaffolder.py` | 139 | Placeholder | Playwright/Cypress scaffolding, page objects, CI/CD integration |
| `test_suite_generator.py` | 160 | Placeholder | Test case generation, boundary analysis, fixture creation |

### Already Implemented (Reference)

| Script | Lines | Quality |
|--------|-------|---------|
| `fixture_generator.py` | 454 | Full implementation - boundary values, edge cases, factories |
| `format_detector.py` | 431 | Full implementation - framework detection |
| `refactor_analyzer.py` | 649 | Full implementation - code smells, safety checks |
| `tdd_workflow.py` | 409 | Full implementation - red/green/refactor phases |
| `test_spec_generator.py` | 706 | Full implementation - Given-When-Then specs |

---

## Implementation Plan

### Script 1: coverage_analyzer.py

**Purpose:** Parse test coverage reports (lcov, cobertura, istanbul) and identify coverage gaps with actionable recommendations.

**Target Lines:** 700-800

#### Features to Implement

1. **Coverage Report Parsing**
   - LCOV format parsing (`lcov.info`)
   - Cobertura XML parsing (`coverage.xml`)
   - Istanbul JSON parsing (`coverage-final.json`)
   - Jest coverage summary (`coverage-summary.json`)

2. **Coverage Metrics Calculation**
   - Line coverage percentage
   - Branch coverage percentage
   - Function coverage percentage
   - Statement coverage percentage
   - Per-file coverage breakdown

3. **Gap Identification**
   - Uncovered lines by file
   - Uncovered branches by function
   - Critical path analysis (prioritize business logic)
   - Complexity-weighted coverage scoring

4. **Trend Analysis**
   - Compare current vs. baseline coverage
   - Track coverage delta over time
   - Identify regression patterns

5. **Recommendations Engine**
   - Priority-ranked files needing tests
   - Effort estimates (easy, medium, hard)
   - Test suggestions for uncovered code

#### CLI Interface

```bash
# Parse LCOV coverage
python coverage_analyzer.py --input coverage/lcov.info --format lcov

# Parse Cobertura with baseline comparison
python coverage_analyzer.py --input coverage.xml --format cobertura --baseline 80

# Output JSON for CI/CD
python coverage_analyzer.py --input . --auto-detect --output json

# Generate detailed report
python coverage_analyzer.py --input . -v --threshold 85 --file report.json
```

#### Data Structures

```python
results = {
    'status': 'success',
    'coverage': {
        'lines': {'covered': 450, 'total': 500, 'percentage': 90.0},
        'branches': {'covered': 120, 'total': 150, 'percentage': 80.0},
        'functions': {'covered': 45, 'total': 50, 'percentage': 90.0},
    },
    'files': [
        {'path': 'src/auth.ts', 'line_coverage': 85.0, 'branch_coverage': 70.0, 'uncovered_lines': [45, 67, 89]},
    ],
    'gaps': [
        {'file': 'src/auth.ts', 'severity': 'high', 'reason': 'Critical auth logic uncovered', 'lines': [45, 67]},
    ],
    'recommendations': [
        {'priority': 1, 'file': 'src/auth.ts', 'effort': 'medium', 'suggestion': 'Add tests for error handling'},
    ],
    'trend': {'delta': -2.5, 'baseline': 85.0, 'current': 82.5, 'status': 'declining'},
}
```

---

### Script 2: e2e_test_scaffolder.py

**Purpose:** Scaffold complete E2E testing infrastructure for Playwright or Cypress with page objects, fixtures, and CI/CD integration.

**Target Lines:** 700-800

#### Features to Implement

1. **Framework Detection & Setup**
   - Auto-detect existing framework (Playwright, Cypress, none)
   - Generate framework-specific configuration
   - Initialize project structure

2. **Page Object Model Generation**
   - Base page class template
   - Login page object
   - Navigation component
   - Form component patterns
   - Action methods (click, fill, wait)
   - Assertion helpers

3. **Test Structure Scaffolding**
   - Test suite organization
   - Spec file templates
   - Describe/it blocks with best practices
   - Setup/teardown patterns

4. **Fixture & Test Data Management**
   - Fixture file structure
   - Mock data generators
   - Environment-specific data
   - Sensitive data handling patterns

5. **CI/CD Integration Templates**
   - GitHub Actions workflow
   - GitLab CI configuration
   - CircleCI config
   - Parallel execution setup
   - Artifact collection

6. **Configuration Generation**
   - Playwright config (playwright.config.ts)
   - Cypress config (cypress.config.ts)
   - Environment variables template
   - Test reporters setup

#### CLI Interface

```bash
# Scaffold Playwright tests
python e2e_test_scaffolder.py --input . --framework playwright --output ./e2e

# Scaffold Cypress with CI/CD
python e2e_test_scaffolder.py --input . --framework cypress --ci github-actions

# Generate page objects only
python e2e_test_scaffolder.py --input . --framework playwright --pages-only

# Full scaffold with custom base URL
python e2e_test_scaffolder.py --input . --framework playwright --base-url http://localhost:3000
```

#### Generated Structure

```
e2e/
  playwright.config.ts
  pages/
    base.page.ts
    login.page.ts
    home.page.ts
  tests/
    auth.spec.ts
    navigation.spec.ts
  fixtures/
    test-data.json
    users.json
  utils/
    helpers.ts
    constants.ts
  .github/
    workflows/
      e2e.yml
```

---

### Script 3: test_suite_generator.py

**Purpose:** Generate comprehensive test suites from source code analysis with unit tests, integration test stubs, and edge case coverage.

**Target Lines:** 700-800

#### Features to Implement

1. **Source Code Analysis**
   - Function/method extraction
   - Parameter type inference
   - Return type inference
   - Dependency detection
   - Complexity assessment

2. **Test Case Generation**
   - Happy path tests
   - Error condition tests
   - Boundary value tests
   - Edge case tests
   - Integration test stubs

3. **Framework-Specific Output**
   - Jest test templates
   - Vitest test templates
   - Pytest test templates
   - Mocha test templates

4. **Coverage Optimization**
   - Branch coverage targets
   - Condition coverage targets
   - Path coverage suggestions

5. **Test Data Generation**
   - Mock data for parameters
   - Expected return values
   - Error scenarios

6. **Test Organization**
   - Describe blocks by class/module
   - It blocks by method
   - Nested describes for scenarios
   - beforeEach/afterEach setup

#### CLI Interface

```bash
# Generate tests for single file
python test_suite_generator.py --input src/auth.ts --framework jest

# Generate tests for directory
python test_suite_generator.py --input src/ --framework pytest --recursive

# Generate with mocks
python test_suite_generator.py --input src/api.ts --framework jest --with-mocks

# Output to file
python test_suite_generator.py --input src/ --framework vitest --output tests/
```

#### Generated Output Example

```typescript
// auth.test.ts
describe('AuthService', () => {
  describe('login', () => {
    it('should return user on valid credentials', async () => {
      // Arrange
      const credentials = { email: 'test@example.com', password: 'password123' };

      // Act
      const result = await authService.login(credentials);

      // Assert
      expect(result).toHaveProperty('user');
      expect(result.user.email).toBe(credentials.email);
    });

    it('should throw on invalid credentials', async () => {
      // Arrange
      const credentials = { email: 'invalid@example.com', password: 'wrong' };

      // Act & Assert
      await expect(authService.login(credentials)).rejects.toThrow('Invalid credentials');
    });

    // Edge cases
    it('should handle empty email', async () => {
      const credentials = { email: '', password: 'password123' };
      await expect(authService.login(credentials)).rejects.toThrow('Email required');
    });
  });
});
```

---

## Implementation Order

1. **coverage_analyzer.py** (First)
   - Most commonly needed by teams
   - Clear inputs/outputs (coverage files)
   - Can reference existing parsing patterns

2. **test_suite_generator.py** (Second)
   - Builds on code analysis patterns from refactor_analyzer.py
   - Generates actionable test code
   - High value for developers

3. **e2e_test_scaffolder.py** (Third)
   - Most complex (multi-file generation)
   - Framework-specific templates
   - CI/CD integration complexity

---

## Quality Requirements

### All Scripts Must:

- [ ] Use Python 3.8+ standard library only (no pip dependencies)
- [ ] Support `--help` with comprehensive documentation
- [ ] Support `--output json` for CI/CD integration
- [ ] Support `--output csv` for reporting
- [ ] Support `--verbose` for debugging
- [ ] Handle errors gracefully with useful messages
- [ ] Follow existing code patterns (from fixture_generator.py)
- [ ] Include docstrings for all classes and methods
- [ ] Provide actionable recommendations (not just data)

### Testing Verification

```bash
# Each script should pass these checks
python coverage_analyzer.py --help
python coverage_analyzer.py --input . --output json

python test_suite_generator.py --help
python test_suite_generator.py --input . --output json

python e2e_test_scaffolder.py --help
python e2e_test_scaffolder.py --input . --output json
```

---

## Implementation Steps

### Step 1: coverage_analyzer.py

1. Create CoverageAnalyzer class with proper structure
2. Implement LCOV parser (most common format)
3. Implement Cobertura XML parser
4. Implement Istanbul JSON parser
5. Add coverage metrics calculation
6. Add gap identification logic
7. Add recommendations engine
8. Add trend analysis (baseline comparison)
9. Add CLI interface with all options
10. Add text, JSON, CSV output formatters

### Step 2: test_suite_generator.py

1. Create TestSuiteGenerator class
2. Implement source code parser (function extraction)
3. Add parameter and return type inference
4. Create test case generator (happy path)
5. Add error scenario generator
6. Add boundary value test generator
7. Implement framework-specific templates (Jest, Pytest, Vitest)
8. Add mock generation support
9. Add CLI interface
10. Add output formatters

### Step 3: e2e_test_scaffolder.py

1. Create E2ETestScaffolder class
2. Implement framework detection
3. Create Playwright config generator
4. Create Cypress config generator
5. Implement page object templates
6. Add test spec templates
7. Create fixture file generators
8. Add CI/CD workflow generators
9. Implement file writing with directory creation
10. Add CLI interface and formatters

---

## Success Criteria

- [ ] All 3 scripts implemented with 700-800 lines each
- [ ] Total implementation ~2,100-2,400 lines
- [ ] All scripts pass `--help` verification
- [ ] All scripts produce valid JSON output
- [ ] No external dependencies (standard library only)
- [ ] Backlog updated with completion status
- [ ] SKILL.md updated if needed

---

## Reference Files

### Patterns to Follow
- [fixture_generator.py](skills/engineering-team/senior-qa/scripts/fixture_generator.py) - Data structures, CLI patterns
- [refactor_analyzer.py](skills/engineering-team/senior-qa/scripts/refactor_analyzer.py) - Code analysis patterns
- [test_spec_generator.py](skills/engineering-team/senior-qa/scripts/test_spec_generator.py) - Test generation patterns

### Backlog Update Location
- [BACKLOG.md](BACKLOG.md) - Update Priority 8 status and line counts
