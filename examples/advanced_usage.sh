#!/bin/bash
# Advanced mathcli usage examples with command substitution and real-world scenarios

echo "======================================"
echo "mathcli - Advanced Usage Examples"
echo "======================================"
echo

echo "=== Chain Calculations (Command Substitution) ==="
echo "Calculate (10 + 5) * 2:"
echo "$ mathcli multiply \$(mathcli add 10 5) 2"
mathcli multiply $(mathcli add 10 5) 2
echo

echo "Calculate (100 - 25) / 5:"
echo "$ mathcli divide \$(mathcli subtract 100 25) 5"
mathcli divide $(mathcli subtract 100 25) 5
echo

echo "=== Financial Calculations ==="
echo "Split restaurant bill \$125.50 among 4 people:"
echo "$ mathcli divide 125.50 4"
mathcli divide 125.50 4
echo

echo "Calculate 15% tip on \$85.00:"
echo "$ mathcli multiply 85.00 0.15"
mathcli multiply 85.00 0.15
echo

echo "Total with tip (bill + 15%):"
echo "$ mathcli multiply 85.00 1.15"
mathcli multiply 85.00 1.15
echo

echo "=== Unit Conversions ==="
echo "Convert 5 miles to kilometers (1 mile = 1.60934 km):"
echo "$ mathcli multiply 5 1.60934"
mathcli multiply 5 1.60934
echo

echo "Convert 100 Fahrenheit to Celsius: (F-32)*5/9:"
echo "$ mathcli divide \$(mathcli multiply \$(mathcli subtract 100 32) 5) 9"
mathcli divide $(mathcli multiply $(mathcli subtract 100 32) 5) 9
echo

echo "=== Budget Planning ==="
echo "Total monthly expenses:"
echo "Rent: \$1200, Groceries: \$400, Utilities: \$150, Transport: \$200"
echo "$ mathcli add 1200 400 150 200"
mathcli add 1200 400 150 200
echo

echo "Remaining budget from \$3000 salary:"
echo "$ mathcli subtract 3000 1200 400 150 200"
mathcli subtract 3000 1200 400 150 200
echo

echo "=== Investment Calculations ==="
echo "Simple interest: Principal \$1000, Rate 5% (0.05), Time 3 years:"
echo "Interest = P * r * t"
echo "$ mathcli multiply 1000 0.05 3"
mathcli multiply 1000 0.05 3
echo

echo "Total amount (Principal + Interest):"
echo "$ mathcli add 1000 \$(mathcli multiply 1000 0.05 3)"
mathcli add 1000 $(mathcli multiply 1000 0.05 3)
echo

echo "=== Average Calculation ==="
echo "Average of test scores: 85, 92, 78, 95, 88"
echo "Sum: \$ mathcli add 85 92 78 95 88"
sum=$(mathcli add 85 92 78 95 88)
echo $sum
echo "Average (sum / count): $ mathcli divide $sum 5"
mathcli divide $sum 5
echo

echo "======================================"
echo "Advanced examples completed!"
echo "======================================"
