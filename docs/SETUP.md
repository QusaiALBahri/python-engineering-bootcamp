# 🚀 SETUP GUIDE - Python Training Environment

Complete step-by-step instructions to set up your Python training environment.

## System Requirements

- **Python:** 3.9 or higher
- **OS:** Windows, macOS, or Linux
- **RAM:** 4GB minimum
- **Disk:** 1GB free space

Check your Python version:
```bash
python --version
```

If you need to install Python: https://www.python.org/downloads/

---

## 1️⃣ Create Virtual Environment

**Why?** A virtual environment isolates this project's dependencies from your system Python.

### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` at the start of your terminal now.

---

## 2️⃣ Install Dependencies

Upgrade pip first:
```bash
pip install --upgrade pip
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

Verify installation:
```bash
pip list
```

---

## 3️⃣ Configure Environment Variables (Optional but Recommended)

For Days 11-12 (AI integration), you'll need API keys.

1. Copy the template:
```bash
cp .env.example .env
```

2. Edit `.env` with your API keys:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

3. Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

⚠️ **Security:** Never share your `.env` file or API keys!

---

## 4️⃣ Directory Structure

```
python-training/
├── day01_basics/              # Day 1: Print, Input, Variables, Strings
├── day02_logic_functions/     # Day 2: if/elif/else, Functions
├── day03_loops_structures/    # Day 3: for, while, Lists, Dicts
├── day04_power_user/          # Day 4: Comprehensions, Files, Decorators
├── day05_workflow_debugging/  # Day 5: Debugging, Git, PEP 8
├── day06_systems_gpa/         # Day 6: System Engineering, GPA System
├── day07_refactor_oop/        # Day 7: OOP Advanced
├── day08_agile_sprints_libs/  # Day 8: Agile, Sprints, Libraries
├── day09_data_viz/            # Day 9: Pandas, Matplotlib
├── day10_gui_tkinter/         # Day 10: GUI, Tkinter, Flask intro
├── day11_web_flask_ai/        # Day 11: Flask, Automation, AI APIs
├── day12_extra_resources/     # Day 12: Resources, Advanced topics
├── day13_colab_pandas_matplotlib/  # Day 13: Pandas workshop
├── day14_logreg_ml/           # Day 14: ML, Logistic Regression
├── docs/                      # Documentation
├── tests/                     # Unit tests
├── samples/                   # Quick sample scripts
├── requirements.txt           # Dependencies
├── .env.example              # Environment template
└── README.md                 # This file
```

---

## 5️⃣ Running Your First Program

### Simple Test:
```bash
python day01_basics/01_hello.py
```

### Run All Samples:
```bash
python samples/hello.py
python samples/discount.py
python samples/grades_miniclass.py
```

---

## 6️⃣ Running Tests

First install pytest:
```bash
pip install pytest
```

Run tests:
```bash
pytest tests/
pytest tests/ -v  # Verbose output
```

---

## 7️⃣ Deactivate Virtual Environment

When you're done:
```bash
deactivate
```

To reactivate later:
```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

---

## 🆘 Troubleshooting

### "Python command not found"
```bash
# Try:
python3 --version
# Then use python3 instead of python in all commands
```

### "pip install fails"
```bash
# Upgrade pip:
python -m pip install --upgrade pip

# Then try again:
pip install -r requirements.txt
```

### " ModuleNotFoundError: No module named 'tkinter'"
On Linux, install separately:
```bash
sudo apt-get install python3-tk  # Ubuntu/Debian
brew install python-tk  # macOS
```

### Virtual environment not activating?
Make sure you're in the correct directory:
```bash
cd path/to/python-training
.venv\Scripts\activate  # Windows
```

---

## 📦 Optional: Create requirements.txt yourself

If you prefer to manage dependencies manually:

```bash
# Record what you have installed
pip freeze > requirements.txt

# Later, reinstall from that file
pip install -r requirements.txt
```

---

## ✅ You're Ready!

- [ ] Python 3.9+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Environment variables configured
- [ ] First program runs successfully

**Start with:** `python day01_basics/01_hello.py`

---

## 📚 Next Steps

1. Read `day01_basics/README.md`
2. Run `day01_basics/01_hello.py`
3. Complete exercises in `EXERCISES.md`
4. Move through days sequentially

---

## Need Help?

- **Python Docs:** https://docs.python.org/3/
- **GitHub Issues:** Post questions as issues
- **Discord/Community:** [Add your community link]

Happy learning! 🎓
