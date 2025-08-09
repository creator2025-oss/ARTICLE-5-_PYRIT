# 🚀 PyRIT EU AI Act Compliance Testing - Setup Instructions

## 📦 What's Included in This Package

This package contains a complete, working PyRIT-based EU AI Act Article 5 compliance testing system with:

### 🛠️ Core Files
- **`fixed_pyrit_test_runner.py`** - Main test runner (FIXED version that works!)
- **`eu_ai_act_article_5_tests.yaml`** - Test scenarios for all EU AI Act Article 5 provisions
- **`pyrit_scorer_config.yaml`** - PyRIT scorer configuration

### 📊 Report Generation
- **`generate_comprehensive_html_report.py`** - Creates beautiful interactive HTML reports
- **`view_comprehensive_report.py`** - Quick browser opener for reports
- **`show_summary.py`** - Command-line summary display

### 📈 Sample Results (Latest Run)
- **`fixed_pyrit_compliance_report_20250725_235735.json`** - Complete JSON results
- **`comprehensive_pyrit_compliance_report_20250726_000011.html`** - Interactive HTML dashboard

### 📚 Documentation
- **`README_FIXED_PYRIT_SYSTEM.md`** - Comprehensive system documentation
- **`SETUP_INSTRUCTIONS.md`** - This setup guide
- **`USAGE_GUIDE.md`** - Step-by-step usage instructions

## 🔧 Quick Setup (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install pyrit openai pyyaml
```

### Step 2: Set OpenAI API Key
**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your-openai-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your-openai-api-key-here
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

### Step 3: Test the System
```bash
python fixed_pyrit_test_runner.py
```

That's it! The system will run all 15 EU AI Act compliance tests and generate results.

## 📊 What You'll Get

After running, you'll have:
- **JSON Report**: Detailed machine-readable results
- **HTML Dashboard**: Beautiful interactive web report with charts
- **Command-line Summary**: Quick overview of results

## 🎯 Key Results from Latest Run

- ✅ **28.1% Compliant** responses (9/32 prompts)
- 🚨 **3.1% Violations** detected (1/32 prompts)
- 🛡️ **28.1% Proper Refusals** (9/32 prompts)
- ⚠️ **0% Harmful Patterns** detected

## 🔬 Technical Details

- **Response Generation**: Direct OpenAI API (gpt-3.5-turbo)
- **Risk Assessment**: PyRIT Enhanced Framework
- **Testing Coverage**: All EU AI Act Article 5 provisions
- **Report Format**: JSON + Interactive HTML with charts

## 🆘 Troubleshooting

### Common Issues:

1. **"No module named 'pyrit'"**
   ```bash
   pip install pyrit
   ```

2. **OpenAI API errors**
   - Check your API key is set correctly
   - Ensure you have OpenAI credits available

3. **Permission errors on Windows**
   - Run PowerShell as Administrator if needed

## 📞 Support

If you have any issues:
1. Check the `README_FIXED_PYRIT_SYSTEM.md` for detailed documentation
2. Review the sample results to see expected output format
3. The system has been tested and works reliably

## 🎉 Ready to Use!

This is a complete, working system. The PyRIT integration issues have been fixed, and you can start testing EU AI Act compliance immediately!
