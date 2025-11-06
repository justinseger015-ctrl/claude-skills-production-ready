#!/bin/bash
# Test a single Python script for CLI standards compliance
# Usage: ./test_single_script.sh path/to/script.py [sample_input_file]

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

if [ $# -eq 0 ]; then
    echo "Usage: $0 <script_path> [sample_input_file]"
    echo ""
    echo "Example:"
    echo "  $0 marketing-skill/content-creator/scripts/brand_voice_analyzer.py"
    echo "  $0 marketing-skill/content-creator/scripts/brand_voice_analyzer.py marketing-skill/content-creator/assets/sample-content.txt"
    exit 1
fi

SCRIPT_PATH="$1"
SAMPLE_INPUT="${2:-}"

if [ ! -f "$SCRIPT_PATH" ]; then
    echo -e "${RED}Error: Script not found: $SCRIPT_PATH${NC}"
    exit 1
fi

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Testing: $(basename $SCRIPT_PATH)${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Test 1: Python syntax
echo -e "${YELLOW}[Test 1] Python Syntax Check${NC}"
if python3 -m py_compile "$SCRIPT_PATH" 2>/dev/null; then
    echo -e "  ${GREEN}✓ PASSED${NC} - Valid Python syntax"
else
    echo -e "  ${RED}✗ FAILED${NC} - Syntax errors found"
    python3 -m py_compile "$SCRIPT_PATH"
    exit 1
fi
echo ""

# Test 2: Has argparse
echo -e "${YELLOW}[Test 2] Argparse Usage${NC}"
if grep -q "import argparse" "$SCRIPT_PATH"; then
    echo -e "  ${GREEN}✓ PASSED${NC} - Uses argparse"
else
    echo -e "  ${RED}✗ FAILED${NC} - Does not import argparse"
    exit 1
fi
echo ""

# Test 3: Has main() function
echo -e "${YELLOW}[Test 3] Main Function${NC}"
if grep -q "def main():" "$SCRIPT_PATH"; then
    echo -e "  ${GREEN}✓ PASSED${NC} - Has main() function"
else
    echo -e "  ${YELLOW}⚠ WARNING${NC} - No main() function found"
fi
echo ""

# Test 4: --help flag
echo -e "${YELLOW}[Test 4] Help Flag${NC}"
if python3 "$SCRIPT_PATH" --help > /dev/null 2>&1; then
    echo -e "  ${GREEN}✓ PASSED${NC} - --help flag works"
    echo ""
    echo -e "${BLUE}Help Output Preview:${NC}"
    python3 "$SCRIPT_PATH" --help | head -20
    echo "  ..."
else
    echo -e "  ${RED}✗ FAILED${NC} - --help flag failed"
    python3 "$SCRIPT_PATH" --help
    exit 1
fi
echo ""

# Test 5: --version flag (optional)
echo -e "${YELLOW}[Test 5] Version Flag (Optional)${NC}"
if python3 "$SCRIPT_PATH" --version > /dev/null 2>&1; then
    VERSION=$(python3 "$SCRIPT_PATH" --version 2>&1)
    echo -e "  ${GREEN}✓ PASSED${NC} - $VERSION"
else
    echo -e "  ${YELLOW}⚠ SKIPPED${NC} - No --version flag (optional)"
fi
echo ""

# Test 6: Standard flags present in help
echo -e "${YELLOW}[Test 6] Standard Flags in Help${NC}"
HELP_OUTPUT=$(python3 "$SCRIPT_PATH" --help 2>&1)

FLAGS_FOUND=0
FLAGS_TOTAL=4

if echo "$HELP_OUTPUT" | grep -q "\-\-output"; then
    echo -e "  ${GREEN}✓${NC} --output flag documented"
    ((FLAGS_FOUND++))
else
    echo -e "  ${YELLOW}⚠${NC} --output flag missing"
fi

if echo "$HELP_OUTPUT" | grep -q "\-\-file"; then
    echo -e "  ${GREEN}✓${NC} --file flag documented"
    ((FLAGS_FOUND++))
else
    echo -e "  ${YELLOW}⚠${NC} --file flag missing"
fi

if echo "$HELP_OUTPUT" | grep -q "\-\-verbose"; then
    echo -e "  ${GREEN}✓${NC} --verbose flag documented"
    ((FLAGS_FOUND++))
else
    echo -e "  ${YELLOW}⚠${NC} --verbose flag missing"
fi

if echo "$HELP_OUTPUT" | grep -q "Examples:"; then
    echo -e "  ${GREEN}✓${NC} Usage examples included"
    ((FLAGS_FOUND++))
else
    echo -e "  ${YELLOW}⚠${NC} Usage examples missing"
fi

echo -e "  Standard flags: $FLAGS_FOUND/$FLAGS_TOTAL"
echo ""

# Test 7: Run with sample input (if provided)
if [ -n "$SAMPLE_INPUT" ]; then
    echo -e "${YELLOW}[Test 7] Execution with Sample Input${NC}"

    if [ ! -f "$SAMPLE_INPUT" ]; then
        echo -e "  ${RED}✗ FAILED${NC} - Sample input file not found: $SAMPLE_INPUT"
        exit 1
    fi

    echo "  Testing with: $SAMPLE_INPUT"
    echo ""

    # Test basic execution
    echo -e "  ${BLUE}7a) Basic execution:${NC}"
    if python3 "$SCRIPT_PATH" "$SAMPLE_INPUT" > /tmp/test_output.txt 2>&1; then
        echo -e "  ${GREEN}✓ PASSED${NC} - Script executed successfully"
        echo "  Output preview:"
        head -10 /tmp/test_output.txt | sed 's/^/    /'
        echo "    ..."
    else
        echo -e "  ${RED}✗ FAILED${NC} - Script execution failed"
        cat /tmp/test_output.txt
        exit 1
    fi
    echo ""

    # Test JSON output
    echo -e "  ${BLUE}7b) JSON output test:${NC}"
    if python3 "$SCRIPT_PATH" "$SAMPLE_INPUT" --output json > /tmp/test_json.json 2>&1; then
        if python3 -m json.tool /tmp/test_json.json > /dev/null 2>&1; then
            echo -e "  ${GREEN}✓ PASSED${NC} - Valid JSON output"
            echo "  JSON preview:"
            python3 -m json.tool /tmp/test_json.json | head -15 | sed 's/^/    /'
            echo "    ..."
        else
            echo -e "  ${RED}✗ FAILED${NC} - Invalid JSON output"
            cat /tmp/test_json.json
            exit 1
        fi
    else
        echo -e "  ${YELLOW}⚠ SKIPPED${NC} - JSON output not supported"
    fi
    echo ""

    # Test file output
    echo -e "  ${BLUE}7c) File output test:${NC}"
    OUTPUT_FILE="/tmp/test_script_output_$(date +%s).txt"
    if python3 "$SCRIPT_PATH" "$SAMPLE_INPUT" --file "$OUTPUT_FILE" > /dev/null 2>&1; then
        if [ -f "$OUTPUT_FILE" ]; then
            FILE_SIZE=$(wc -c < "$OUTPUT_FILE")
            echo -e "  ${GREEN}✓ PASSED${NC} - File created successfully ($FILE_SIZE bytes)"
            rm -f "$OUTPUT_FILE"
        else
            echo -e "  ${RED}✗ FAILED${NC} - File not created"
            exit 1
        fi
    else
        echo -e "  ${YELLOW}⚠ SKIPPED${NC} - File output not supported"
    fi
    echo ""

    # Test verbose mode
    echo -e "  ${BLUE}7d) Verbose mode test:${NC}"
    if python3 "$SCRIPT_PATH" "$SAMPLE_INPUT" --verbose > /tmp/test_verbose.txt 2>&1; then
        echo -e "  ${GREEN}✓ PASSED${NC} - Verbose mode works"
    else
        echo -e "  ${YELLOW}⚠ SKIPPED${NC} - Verbose mode not supported"
    fi

else
    echo -e "${YELLOW}[Test 7] Execution Test${NC}"
    echo -e "  ${YELLOW}⚠ SKIPPED${NC} - No sample input provided"
    echo ""
    echo "  To test with sample input, run:"
    echo "    $0 $SCRIPT_PATH <sample_input_file>"
fi
echo ""

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✓ All critical tests passed!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Cleanup
rm -f /tmp/test_output.txt /tmp/test_json.json /tmp/test_verbose.txt

exit 0
