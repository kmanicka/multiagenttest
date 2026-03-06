#!/bin/bash
# Basic mathcli usage examples

echo "======================================"
echo "mathcli - Basic Usage Examples"
echo "======================================"
echo

echo "=== Addition ==="
echo "$ mathcli add 5 10"
mathcli add 5 10
echo

echo "$ mathcli add 1.5 2.5 3.0"
mathcli add 1.5 2.5 3.0
echo

echo "$ mathcli add -5 10 -3"
mathcli add -5 10 -3
echo

echo "=== Subtraction ==="
echo "$ mathcli subtract 10 3"
mathcli subtract 10 3
echo

echo "$ mathcli subtract 100 25 10 5"
mathcli subtract 100 25 10 5
echo

echo "$ mathcli subtract 5 10  # Negative result"
mathcli subtract 5 10
echo

echo "=== Multiplication ==="
echo "$ mathcli multiply 5 4"
mathcli multiply 5 4
echo

echo "$ mathcli multiply 2 3 4"
mathcli multiply 2 3 4
echo

echo "$ mathcli multiply 2.5 4"
mathcli multiply 2.5 4
echo

echo "=== Division ==="
echo "$ mathcli divide 20 4"
mathcli divide 20 4
echo

echo "$ mathcli divide 100 2 5"
mathcli divide 100 2 5
echo

echo "$ mathcli divide 10 3  # With decimals"
mathcli divide 10 3
echo

echo "======================================"
echo "Examples completed successfully!"
echo "======================================"
