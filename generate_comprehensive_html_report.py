#!/usr/bin/env python3
"""
Comprehensive HTML Report Generator for PyRIT EU AI Act Compliance Testing
Creates a detailed, professional HTML report showing compliance, classifications, and violations.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any

class ComprehensiveHTMLReportGenerator:
    def __init__(self, json_file_path: str):
        """Initialize the report generator with JSON results."""
        self.json_file_path = json_file_path
        with open(json_file_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
    
    def generate_html_report(self, output_file: str = None) -> str:
        """Generate comprehensive HTML report."""
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"comprehensive_pyrit_compliance_report_{timestamp}.html"
        
        html_content = self._build_html_content()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Comprehensive HTML report generated: {output_file}")
        return output_file
    
    def _build_html_content(self) -> str:
        """Build the complete HTML content."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyRIT EU AI Act Article 5 Compliance Report</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        {self._get_css_styles()}
    </style>
</head>
<body>
    <div class="container">
        {self._generate_header()}
        {self._generate_executive_summary()}
        {self._generate_compliance_matrix()}
        {self._generate_detailed_results()}
        {self._generate_pyrit_analysis()}
        {self._generate_recommendations()}
        {self._generate_footer()}
    </div>
    <script>
        {self._get_javascript()}
    </script>
</body>
</html>"""
    
    def _get_css_styles(self) -> str:
        """Get CSS styles for the report."""
        return """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .section {
            background: white;
            margin-bottom: 30px;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .section h2 {
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        
        .section h3 {
            font-size: 1.4em;
            margin-bottom: 15px;
            color: #34495e;
        }
        
        .executive-summary {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 25px;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .metric-card h4 {
            font-size: 1.1em;
            margin-bottom: 10px;
            opacity: 0.9;
        }
        
        .metric-card .value {
            font-size: 2.2em;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .metric-card .percentage {
            font-size: 1.1em;
            opacity: 0.8;
        }
        
        .compliance-matrix {
            overflow-x: auto;
        }
        
        .matrix-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        .matrix-table th,
        .matrix-table td {
            padding: 12px 8px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .matrix-table th {
            background-color: #34495e;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
        }
        
        .matrix-table tr:hover {
            background-color: #f5f5f5;
        }
        
        .status-compliant {
            background-color: #d4edda;
            color: #155724;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .status-violation {
            background-color: #f8d7da;
            color: #721c24;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .status-partial {
            background-color: #fff3cd;
            color: #856404;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .status-needs-review {
            background-color: #e2e3e5;
            color: #383d41;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .risk-very-low {
            background-color: #d1ecf1;
            color: #0c5460;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .risk-low {
            background-color: #d4edda;
            color: #155724;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .risk-medium {
            background-color: #fff3cd;
            color: #856404;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .risk-high {
            background-color: #f8d7da;
            color: #721c24;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .risk-very-high {
            background-color: #dc3545;
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
        }
        
        .test-details {
            margin-bottom: 30px;
            border: 1px solid #dee2e6;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .test-header {
            background-color: #f8f9fa;
            padding: 15px 20px;
            border-bottom: 1px solid #dee2e6;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .test-header:hover {
            background-color: #e9ecef;
        }
        
        .test-header h4 {
            color: #495057;
            margin: 0;
        }
        
        .test-content {
            display: none;
            padding: 20px;
        }
        
        .test-content.active {
            display: block;
        }
        
        .prompt-result {
            margin-bottom: 25px;
            padding: 15px;
            border-left: 4px solid #3498db;
            background-color: #f8f9fa;
            border-radius: 0 5px 5px 0;
        }
        
        .prompt-text {
            font-weight: bold;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        
        .ai-response {
            background-color: white;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            border: 1px solid #dee2e6;
        }
        
        .assessment-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }
        
        .assessment-item {
            background-color: white;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #dee2e6;
        }
        
        .assessment-item strong {
            display: block;
            margin-bottom: 5px;
            color: #495057;
        }
        
        .charts-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            margin-top: 20px;
        }
        
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .chart-title {
            text-align: center;
            margin-bottom: 15px;
            font-size: 1.2em;
            color: #2c3e50;
        }
        
        .recommendations {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 20px;
            border-radius: 8px;
        }
        
        .recommendations h3 {
            color: #856404;
            margin-bottom: 15px;
        }
        
        .recommendations ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        .recommendations li {
            margin-bottom: 10px;
            padding-left: 25px;
            position: relative;
        }
        
        .recommendations li:before {
            content: "⚠️";
            position: absolute;
            left: 0;
        }
        
        .footer {
            text-align: center;
            padding: 20px;
            background-color: #2c3e50;
            color: white;
            border-radius: 10px;
            margin-top: 30px;
        }
        
        .toggle-icon {
            font-size: 1.2em;
            transition: transform 0.3s ease;
        }
        
        .toggle-icon.rotated {
            transform: rotate(180deg);
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .section {
                padding: 15px;
            }
            
            .charts-container {
                grid-template-columns: 1fr;
            }
        }
        """
    
    def _generate_header(self) -> str:
        """Generate the report header."""
        metadata = self.data.get('test_metadata', {})
        timestamp = metadata.get('timestamp', 'Unknown')
        
        return f"""
        <div class="header">
            <h1>🛡️ PyRIT EU AI Act Article 5 Compliance Report</h1>
            <p>Comprehensive AI Safety & Risk Assessment</p>
            <p><strong>Generated:</strong> {timestamp}</p>
            <p><strong>Assessment Method:</strong> {metadata.get('assessment_method', 'PyRIT Enhanced')}</p>
        </div>
        """
    
    def _generate_executive_summary(self) -> str:
        """Generate executive summary with key metrics."""
        summary = self.data.get('pyrit_summary', {})
        
        total_tests = summary.get('total_test_cases', 0)
        total_prompts = summary.get('total_prompts_tested', 0)
        compliant = summary.get('pyrit_compliant_responses', 0)
        violations = summary.get('pyrit_potential_violations', 0)
        refusals = summary.get('pyrit_proper_refusals', 0)
        harmful = summary.get('pyrit_harmful_patterns_detected', 0)
        
        compliance_rate = (compliant / total_prompts * 100) if total_prompts > 0 else 0
        violation_rate = (violations / total_prompts * 100) if total_prompts > 0 else 0
        refusal_rate = (refusals / total_prompts * 100) if total_prompts > 0 else 0
        
        return f"""
        <div class="section">
            <h2>📊 Executive Summary</h2>
            <div class="executive-summary">
                <div class="metric-card">
                    <h4>Total Test Cases</h4>
                    <div class="value">{total_tests}</div>
                    <div class="percentage">EU AI Act Articles</div>
                </div>
                <div class="metric-card">
                    <h4>Total Prompts Tested</h4>
                    <div class="value">{total_prompts}</div>
                    <div class="percentage">Compliance Checks</div>
                </div>
                <div class="metric-card">
                    <h4>Compliant Responses</h4>
                    <div class="value">{compliant}</div>
                    <div class="percentage">{compliance_rate:.1f}%</div>
                </div>
                <div class="metric-card">
                    <h4>Potential Violations</h4>
                    <div class="value">{violations}</div>
                    <div class="percentage">{violation_rate:.1f}%</div>
                </div>
                <div class="metric-card">
                    <h4>Proper Refusals</h4>
                    <div class="value">{refusals}</div>
                    <div class="percentage">{refusal_rate:.1f}%</div>
                </div>
                <div class="metric-card">
                    <h4>Harmful Patterns</h4>
                    <div class="value">{harmful}</div>
                    <div class="percentage">PyRIT Detected</div>
                </div>
            </div>
            
            <div class="charts-container">
                <div class="chart-container">
                    <div class="chart-title">Compliance Distribution</div>
                    <canvas id="complianceChart"></canvas>
                </div>
                <div class="chart-container">
                    <div class="chart-title">Risk Level Distribution</div>
                    <canvas id="riskChart"></canvas>
                </div>
            </div>
        </div>
        """
    
    def _generate_compliance_matrix(self) -> str:
        """Generate compliance matrix table."""
        results = self.data.get('results', [])
        
        matrix_rows = []
        for result in results:
            test_id = result.get('test_id', 'Unknown')
            clause = result.get('clause', 'Unknown')
            name = result.get('name', 'Unknown')
            prompt_results = result.get('prompt_results', [])
            
            total_prompts = len(prompt_results)
            compliant_count = 0
            violation_count = 0
            partial_count = 0
            needs_review_count = 0
            
            for prompt_result in prompt_results:
                assessment = prompt_result.get('pyrit_assessment', {})
                if 'error' not in assessment:
                    compliance_status = assessment.get('compliance_assessment', {}).get('compliance_status', 'UNKNOWN')
                    if compliance_status == 'COMPLIANT':
                        compliant_count += 1
                    elif compliance_status == 'VIOLATION':
                        violation_count += 1
                    elif compliance_status == 'PARTIAL':
                        partial_count += 1
                    elif compliance_status == 'NEEDS_REVIEW':
                        needs_review_count += 1
            
            compliance_rate = (compliant_count / total_prompts * 100) if total_prompts > 0 else 0
            
            matrix_rows.append(f"""
                <tr>
                    <td><strong>{test_id}</strong></td>
                    <td>{clause}</td>
                    <td>{name.replace('_', ' ').title()}</td>
                    <td>{total_prompts}</td>
                    <td><span class="status-compliant">{compliant_count}</span></td>
                    <td><span class="status-violation">{violation_count}</span></td>
                    <td><span class="status-partial">{partial_count}</span></td>
                    <td><span class="status-needs-review">{needs_review_count}</span></td>
                    <td><strong>{compliance_rate:.1f}%</strong></td>
                </tr>
            """)
        
        return f"""
        <div class="section">
            <h2>📋 Compliance Matrix</h2>
            <div class="compliance-matrix">
                <table class="matrix-table">
                    <thead>
                        <tr>
                            <th>Test ID</th>
                            <th>EU AI Act Article</th>
                            <th>Test Name</th>
                            <th>Prompts</th>
                            <th>Compliant</th>
                            <th>Violations</th>
                            <th>Partial</th>
                            <th>Needs Review</th>
                            <th>Compliance Rate</th>
                        </tr>
                    </thead>
                    <tbody>
                        {''.join(matrix_rows)}
                    </tbody>
                </table>
            </div>
        </div>
        """
    
    def _generate_detailed_results(self) -> str:
        """Generate detailed test results."""
        results = self.data.get('results', [])
        
        detailed_sections = []
        for result in results:
            test_id = result.get('test_id', 'Unknown')
            clause = result.get('clause', 'Unknown')
            name = result.get('name', 'Unknown')
            tags = result.get('tags', [])
            prompt_results = result.get('prompt_results', [])
            
            prompt_details = []
            for i, prompt_result in enumerate(prompt_results):
                prompt = prompt_result.get('prompt', 'Unknown')
                ai_response = prompt_result.get('ai_response', 'No response')
                assessment = prompt_result.get('pyrit_assessment', {})
                
                if 'error' in assessment:
                    assessment_html = f'<div class="assessment-item"><strong>Error:</strong> {assessment["error"]}</div>'
                else:
                    compliance_assessment = assessment.get('compliance_assessment', {})
                    risk_scoring = assessment.get('risk_scoring', {})
                    refusal_detection = assessment.get('refusal_detection', {})
                    harmful_detection = assessment.get('harmful_pattern_detection', {})
                    overall_assessment = assessment.get('overall_pyrit_assessment', {})
                    
                    compliance_status = compliance_assessment.get('compliance_status', 'UNKNOWN')
                    risk_level = risk_scoring.get('risk_level', 'UNKNOWN')
                    risk_score = risk_scoring.get('risk_score', 0)
                    properly_refused = refusal_detection.get('properly_refused', False)
                    harmful_patterns = harmful_detection.get('contains_harmful_patterns', False)
                    violation_detected = compliance_assessment.get('violation_detected', False)
                    
                    status_class = self._get_status_class(compliance_status)
                    risk_class = self._get_risk_class(risk_level)
                    
                    assessment_html = f"""
                    <div class="assessment-details">
                        <div class="assessment-item">
                            <strong>Compliance Status</strong>
                            <span class="{status_class}">{compliance_status}</span>
                        </div>
                        <div class="assessment-item">
                            <strong>Risk Level</strong>
                            <span class="{risk_class}">{risk_level}</span>
                        </div>
                        <div class="assessment-item">
                            <strong>Risk Score</strong>
                            {risk_score:.2f}/5.0
                        </div>
                        <div class="assessment-item">
                            <strong>Properly Refused</strong>
                            {'✅ Yes' if properly_refused else '❌ No'}
                        </div>
                        <div class="assessment-item">
                            <strong>Harmful Patterns</strong>
                            {'⚠️ Detected' if harmful_patterns else '✅ None'}
                        </div>
                        <div class="assessment-item">
                            <strong>Violation Detected</strong>
                            {'🚨 Yes' if violation_detected else '✅ No'}
                        </div>
                    </div>
                    """
                
                prompt_details.append(f"""
                    <div class="prompt-result">
                        <div class="prompt-text">Prompt {i+1}: {prompt}</div>
                        <div class="ai-response">
                            <strong>AI Response:</strong><br>
                            {ai_response}
                        </div>
                        <div class="pyrit-assessment">
                            <strong>PyRIT Assessment:</strong>
                            {assessment_html}
                        </div>
                    </div>
                """)
            
            detailed_sections.append(f"""
                <div class="test-details">
                    <div class="test-header" onclick="toggleTestContent('{test_id}')">
                        <div>
                            <h4>{test_id} - {name.replace('_', ' ').title()}</h4>
                            <p><strong>Article:</strong> {clause} | <strong>Tags:</strong> {', '.join(tags[:3])}{'...' if len(tags) > 3 else ''}</p>
                        </div>
                        <span class="toggle-icon" id="icon-{test_id}">▼</span>
                    </div>
                    <div class="test-content" id="content-{test_id}">
                        {''.join(prompt_details)}
                    </div>
                </div>
            """)
        
        return f"""
        <div class="section">
            <h2>🔍 Detailed Test Results</h2>
            <p>Click on each test to expand and view detailed results, AI responses, and PyRIT assessments.</p>
            {''.join(detailed_sections)}
        </div>
        """
    
    def _generate_pyrit_analysis(self) -> str:
        """Generate PyRIT analysis section."""
        metadata = self.data.get('test_metadata', {})
        summary = self.data.get('pyrit_summary', {})
        
        components_used = metadata.get('pyrit_components_used', [])
        compliance_dist = summary.get('pyrit_compliance_distribution', {})
        risk_dist = summary.get('pyrit_risk_distribution', {})
        
        return f"""
        <div class="section">
            <h2>🔬 PyRIT Framework Analysis</h2>
            <h3>Components Used</h3>
            <ul>
                {' '.join([f'<li><strong>{comp}</strong></li>' for comp in components_used])}
            </ul>
            
            <h3>Assessment Methodology</h3>
            <p><strong>Response Generation:</strong> {metadata.get('response_generation', 'OpenAI API Direct')}</p>
            <p><strong>Risk Assessment:</strong> {metadata.get('risk_assessment', 'PyRIT Enhanced')}</p>
            <p><strong>Assessment Method:</strong> {metadata.get('assessment_method', 'Fixed PyRIT Enhanced EU AI Act Testing')}</p>
            
            <h3>Distribution Analysis</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
                <div>
                    <h4>Compliance Distribution</h4>
                    <ul>
                        {' '.join([f'<li><strong>{status}:</strong> {count} prompts</li>' for status, count in compliance_dist.items()])}
                    </ul>
                </div>
                <div>
                    <h4>Risk Distribution</h4>
                    <ul>
                        {' '.join([f'<li><strong>{risk}:</strong> {count} prompts</li>' for risk, count in risk_dist.items()])}
                    </ul>
                </div>
            </div>
        </div>
        """
    
    def _generate_recommendations(self) -> str:
        """Generate recommendations based on findings."""
        summary = self.data.get('pyrit_summary', {})
        
        violations = summary.get('pyrit_potential_violations', 0)
        harmful = summary.get('pyrit_harmful_patterns_detected', 0)
        total_prompts = summary.get('total_prompts_tested', 1)
        compliance_rate = summary.get('pyrit_compliance_rate', 0)
        
        recommendations = []
        
        if violations > 0:
            recommendations.append(f"Address {violations} potential EU AI Act violations detected by PyRIT analysis")
        
        if harmful > 0:
            recommendations.append(f"Investigate {harmful} harmful pattern detections identified by PyRIT")
        
        if compliance_rate < 0.8:
            recommendations.append("Improve overall compliance rate which is currently below 80%")
        
        if not recommendations:
            recommendations.append("Maintain current compliance standards and continue regular monitoring")
        
        recommendations.extend([
            "Implement additional safety measures for high-risk EU AI Act categories",
            "Regular compliance monitoring with PyRIT framework",
            "Review and update AI safety policies based on these findings",
            "Consider additional red team testing for identified vulnerability areas"
        ])
        
        return f"""
        <div class="section">
            <h2>💡 Recommendations</h2>
            <div class="recommendations">
                <h3>Priority Actions</h3>
                <ul>
                    {' '.join([f'<li>{rec}</li>' for rec in recommendations])}
                </ul>
            </div>
        </div>
        """
    
    def _generate_footer(self) -> str:
        """Generate report footer."""
        return f"""
        <div class="footer">
            <p>Generated by PyRIT EU AI Act Compliance Testing Framework</p>
            <p>Report created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>🛡️ Ensuring AI Safety & Regulatory Compliance</p>
        </div>
        """
    
    def _get_status_class(self, status: str) -> str:
        """Get CSS class for compliance status."""
        status_map = {
            'COMPLIANT': 'status-compliant',
            'VIOLATION': 'status-violation',
            'PARTIAL': 'status-partial',
            'NEEDS_REVIEW': 'status-needs-review'
        }
        return status_map.get(status, 'status-needs-review')
    
    def _get_risk_class(self, risk_level: str) -> str:
        """Get CSS class for risk level."""
        risk_map = {
            'VERY_LOW_RISK': 'risk-very-low',
            'LOW_RISK': 'risk-low',
            'MEDIUM_RISK': 'risk-medium',
            'HIGH_RISK': 'risk-high',
            'VERY_HIGH_RISK': 'risk-very-high'
        }
        return risk_map.get(risk_level, 'risk-medium')
    
    def _get_javascript(self) -> str:
        """Get JavaScript for interactive features."""
        summary = self.data.get('pyrit_summary', {})
        compliance_dist = summary.get('pyrit_compliance_distribution', {})
        risk_dist = summary.get('pyrit_risk_distribution', {})
        
        return f"""
        // Toggle test content
        function toggleTestContent(testId) {{
            const content = document.getElementById('content-' + testId);
            const icon = document.getElementById('icon-' + testId);
            
            if (content.classList.contains('active')) {{
                content.classList.remove('active');
                icon.classList.remove('rotated');
            }} else {{
                content.classList.add('active');
                icon.classList.add('rotated');
            }}
        }}
        
        // Create compliance chart
        const complianceCtx = document.getElementById('complianceChart').getContext('2d');
        new Chart(complianceCtx, {{
            type: 'doughnut',
            data: {{
                labels: {list(compliance_dist.keys())},
                datasets: [{{
                    data: {list(compliance_dist.values())},
                    backgroundColor: [
                        '#28a745',  // COMPLIANT - green
                        '#dc3545',  // VIOLATION - red
                        '#ffc107',  // PARTIAL - yellow
                        '#6c757d'   // NEEDS_REVIEW - gray
                    ],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});
        
        // Create risk chart
        const riskCtx = document.getElementById('riskChart').getContext('2d');
        new Chart(riskCtx, {{
            type: 'doughnut',
            data: {{
                labels: {list(risk_dist.keys())},
                datasets: [{{
                    data: {list(risk_dist.values())},
                    backgroundColor: [
                        '#17a2b8',  // LOW - teal
                        '#6f42c1',  // MEDIUM - purple
                        '#fd7e14',  // HIGH - orange
                        '#dc3545'   // VERY HIGH - red
                    ],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});
        """

def main():
    """Main function to generate comprehensive HTML report."""
    # Find the latest JSON report
    json_files = [f for f in os.listdir('.') if f.startswith('fixed_pyrit_compliance_report_') and f.endswith('.json')]
    
    if not json_files:
        print("No PyRIT compliance report JSON files found!")
        return
    
    # Use the latest file
    latest_file = sorted(json_files)[-1]
    print(f"Processing: {latest_file}")
    
    generator = ComprehensiveHTMLReportGenerator(latest_file)
    output_file = generator.generate_html_report()
    
    print(f"✅ Comprehensive HTML report generated successfully!")
    print(f"📁 File: {output_file}")
    print(f"🌐 Open the file in your web browser to view the detailed compliance report")

if __name__ == "__main__":
    main()
