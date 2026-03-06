#!/bin/bash
# Error handling examples for mathcli

echo "======================================"
echo "mathcli - Error Handling Examples"
echo "======================================"
echo

echo "=== Division by Zero ==="
echo "$ mathcli divide 10 0"
mathcli divide 10 0 2>&1
echo "Exit code: $?"
echo

echo "$ mathcli divide 100 2 0 5  # Zero in sequence"
mathcli divide 100 2 0 5 2>&1
echo "Exit code: $?"
echo

echo "=== Insufficient Arguments ==="
echo "$ mathcli add 5  # Needs at least 2 numbers"
mathcli add 5 2>&1
echo "Exit code: $?"
echo

echo "$ mathcli subtract 10  # Needs at least 2 numbers"
mathcli subtract 10 2>&1
echo "Exit code: $?"
echo

echo "$ mathcli multiply 7  # Needs at least 2 numbers"
mathcli multiply 7 2>&1
echo "Exit code: $?"
echo

echo "$ mathcli divide 100  # Needs at least 2 numbers"
mathcli divide 100 2>&1
echo "Exit code: $?"
echo

echo "=== Invalid Input ==="
echo "$ mathcli add 5 abc  # Non-numeric input"
mathcli add 5 abc 2>&1
echo "Exit code: $?"
echo

echo "$ mathcli multiply 10 xyz 20  # Non-numeric in middle"
mathcli multiply 10 xyz 20 2>&1
echo "Exit code: $?"
echo

echo "=== Invalid Command ==="
echo "$ mathcli invalid 5 10  # Unknown command"
mathcli invalid 5 10 2>&1
echo "Exit code: $?"
echo

echo "=== No Arguments ==="
echo "$ mathcli  # No command specified"
mathcli 2>&1
echo "Exit code: $?"
echo

echo "=== Error Handling in Scripts ==="
echo "Example: Check exit code and handle errors"
echo
cat << 'EOF'
#!/bin/bash
if result=$(mathcli divide 100 5 2>/dev/null); then
    echo "Success: $result"
else
    echo "Error occurred (exit code: $?)"
fi
EOF
echo
echo "Running example:"
if result=$(mathcli divide 100 5 2>/dev/null); then
    echo "Success: $result"
else
    echo "Error occurred (exit code: $?)"
fi
echo

echo "Running with error:"
if result=$(mathcli divide 100 0 2>/dev/null); then
    echo "Success: $result"
else
    echo "Error occurred (exit code: $?)"
fi
echo

echo "======================================"
echo "Error handling examples completed!"
echo "Note: All error messages go to stderr"
echo "======================================"
