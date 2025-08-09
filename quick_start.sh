#!/bin/bash

echo "================================================================="
echo "PyRIT EU AI Act Compliance Testing - Quick Start"
echo "================================================================="
echo
echo "This will run the complete compliance testing suite"
echo "Make sure you have set your OPENAI_API_KEY environment variable"
echo
read -p "Press Enter to continue..."

echo "Running compliance tests..."
python3 fixed_pyrit_test_runner.py

echo
echo "Generating HTML report..."
python3 generate_comprehensive_html_report.py

echo
echo "Opening report in browser..."
python3 view_comprehensive_report.py

echo
echo "================================================================="
echo "Testing completed! Check the HTML report for detailed results."
echo "================================================================="
