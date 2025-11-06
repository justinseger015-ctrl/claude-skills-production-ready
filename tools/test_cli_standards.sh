#!/bin/bash
# CLI Standards Test Suite
# Tests Python scripts for compliance with claude-skills CLI standards
# See: standards/cli-standards.md

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
TOTAL=0
PASSED=0
FAILED=0

# Test results file
RESULTS_FILE="cli_test_results.txt"
> "$RESULTS_FILE"  # Clear file

echo "=== CLI Standards Test Suite ==="
echo ""

# Function to test a single script
test_script() {
    local script_path="$1"
    local script_name=$(basename "$script_path")

    echo "Testing: $script_name"
    TOTAL=$((TOTAL + 1))

    local pass_count=0
    local fail_count=0

    # Test 1: Help flag works
    if python3 "$script_path" --help > /dev/null 2>&1; then
        echo "  ✓ --help flag works"
        pass_count=$((pass_count + 1))
    else
        echo -e "  ${RED}✗ --help flag failed${NC}"
        fail_count=$((fail_count + 1))
    fi

    # Test 2: Script is syntax-valid
    if python3 -m py_compile "$script_path" 2>/dev/null; then
        echo "  ✓ Python syntax valid"
        pass_count=$((pass_count + 1))
    else
        echo -e "  ${RED}✗ Python syntax error${NC}"
        fail_count=$((fail_count + 1))
    fi

    # Test 3: Has argparse import
    if grep -q "import argparse" "$script_path"; then
        echo "  ✓ Uses argparse"
        pass_count=$((pass_count + 1))
    else
        echo -e "  ${YELLOW}⚠ No argparse import found${NC}"
        fail_count=$((fail_count + 1))
    fi

    # Test 4: Has main() function
    if grep -q "def main():" "$script_path"; then
        echo "  ✓ Has main() function"
        pass_count=$((pass_count + 1))
    else
        echo -e "  ${YELLOW}⚠ No main() function${NC}"
    fi

    # Summary for this script
    if [ $fail_count -eq 0 ]; then
        echo -e "  ${GREEN}PASSED${NC} ($pass_count checks)"
        PASSED=$((PASSED + 1))
        echo "$script_name: PASSED" >> "$RESULTS_FILE"
    else
        echo -e "  ${RED}FAILED${NC} ($fail_count issues)"
        FAILED=$((FAILED + 1))
        echo "$script_name: FAILED" >> "$RESULTS_FILE"
    fi

    echo ""
}

# Find all Python scripts in skills directories
echo "Scanning for Python scripts..."
echo ""

# Test scripts by domain
for domain in engineering-team c-level-advisor product-team marketing-skill ra-qm-team; do
    domain_path="/Users/ricky/Library/CloudStorage/GoogleDrive-rickydwilson@gmail.com/My Drive/Websites/GitHub/claude-skills/$domain"

    if [ -d "$domain_path" ]; then
        while IFS= read -r -d '' script; do
            test_script "$script"
        done < <(find "$domain_path" -name "*.py" -path "*/scripts/*" -print0 2>/dev/null)
    fi
done

# Final summary
echo "========================================"
echo "Test Summary:"
echo "  Total scripts tested: $TOTAL"
echo -e "  ${GREEN}Passed: $PASSED${NC}"
echo -e "  ${RED}Failed: $FAILED${NC}"
echo "========================================"
echo ""
echo "Detailed results saved to: $RESULTS_FILE"

# Exit with appropriate code
if [ $FAILED -gt 0 ]; then
    exit 1
else
    exit 0
fi
