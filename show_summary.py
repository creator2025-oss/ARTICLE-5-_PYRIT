#!/usr/bin/env python3
"""
Display final summary of PyRIT compliance testing results
"""

import json
import os

def main():
    # Find the latest JSON report
    json_files = [f for f in os.listdir('.') if f.startswith('fixed_pyrit_compliance_report_') and f.endswith('.json')]
    
    if not json_files:
        print("No PyRIT compliance report JSON files found!")
        return
    
    latest_file = sorted(json_files)[-1]
    
    with open(latest_file, 'r') as f:
        data = json.load(f)

    summary = data.get('pyrit_summary', {})
    metadata = data.get('test_metadata', {})
    
    print('🛡️ PYRIT EU AI ACT COMPLIANCE TESTING - FINAL SUMMARY')
    print('='*70)
    print(f'📊 Total Test Cases: {summary.get("total_test_cases", 0)}')
    print(f'📋 Total Prompts Tested: {summary.get("total_prompts_tested", 0)}')
    print()
    print('🎯 COMPLIANCE RESULTS:')
    print(f'   ✅ Compliant Responses: {summary.get("pyrit_compliant_responses", 0)} ({summary.get("pyrit_compliance_rate", 0)*100:.1f}%)')
    print(f'   🚨 Potential Violations: {summary.get("pyrit_potential_violations", 0)} ({summary.get("pyrit_violation_rate", 0)*100:.1f}%)')
    print(f'   🛡️ Proper Refusals: {summary.get("pyrit_proper_refusals", 0)} ({summary.get("pyrit_refusal_rate", 0)*100:.1f}%)')
    print(f'   ⚠️ Harmful Patterns: {summary.get("pyrit_harmful_patterns_detected", 0)} ({summary.get("pyrit_harm_detection_rate", 0)*100:.1f}%)')
    print()
    print('📈 COMPLIANCE DISTRIBUTION:')
    compliance_dist = summary.get('pyrit_compliance_distribution', {})
    for status, count in compliance_dist.items():
        print(f'   {status}: {count} prompts')
    print()
    print('📈 RISK DISTRIBUTION:')
    risk_dist = summary.get('pyrit_risk_distribution', {})
    for risk, count in risk_dist.items():
        print(f'   {risk}: {count} prompts')
    print()
    print('🔧 ASSESSMENT DETAILS:')
    print(f'   Method: {metadata.get("assessment_method", "Fixed PyRIT Enhanced EU AI Act Testing")}')
    print(f'   Response Generation: {metadata.get("response_generation", "OpenAI API Direct")}')
    print(f'   Risk Assessment: {metadata.get("risk_assessment", "PyRIT Enhanced Framework")}')
    print()
    print('✅ TESTING COMPLETED SUCCESSFULLY!')
    print('📁 Files Generated:')
    print(f'   • JSON Report: {latest_file}')
    
    # Find HTML report
    html_files = [f for f in os.listdir('.') if f.startswith('comprehensive_pyrit_compliance_report_') and f.endswith('.html')]
    if html_files:
        latest_html = sorted(html_files)[-1]
        print(f'   • HTML Report: {latest_html}')
    
    print()
    print('🌐 Use "python view_comprehensive_report.py" to open the detailed HTML report')

if __name__ == "__main__":
    main()
