#!/usr/bin/env python3
"""
Quick browser opener for the comprehensive PyRIT compliance HTML report
"""

import os
import webbrowser
import glob

def main():
    """Find and open the latest comprehensive HTML report."""
    # Find the latest comprehensive HTML report
    html_files = glob.glob('comprehensive_pyrit_compliance_report_*.html')
    
    if not html_files:
        print("❌ No comprehensive HTML reports found!")
        print("Run 'python generate_comprehensive_html_report.py' first.")
        return
    
    # Use the latest file
    latest_file = sorted(html_files)[-1]
    
    # Get absolute path
    abs_path = os.path.abspath(latest_file)
    
    print(f"🌐 Opening comprehensive HTML report in browser...")
    print(f"📁 File: {latest_file}")
    
    # Open in default browser
    webbrowser.open(f'file://{abs_path}')
    
    print(f"✅ Report opened successfully!")
    print(f"📊 The report includes:")
    print(f"   • Executive summary with key metrics")
    print(f"   • Compliance matrix showing all test results")
    print(f"   • Detailed test results with AI responses")
    print(f"   • PyRIT framework analysis")
    print(f"   • Interactive charts and visualizations")
    print(f"   • Recommendations based on findings")

if __name__ == "__main__":
    main()
