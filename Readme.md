# 🔐 PASSWORD GENERATOR

**A sleek, cryptographically secure desktop application built with Python & Tkinter.**

![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=for-the-badge)

<br/>

---

</div>

# 🌟 FEATURES

> Designed with simplicity, usability, and top-tier security in mind.

| Feature | Description |
| :--- | :--- |
| 🔒 **Cryptographically Secure** | Leverages Python's native `secrets` module to generate truly unpredictable passwords. |
| 🔣 **Custom Character Sets** | Full control over Uppercase (`A-Z`), Lowercase (`a-z`), Numbers (`0-9`), and Symbols. |
| 👁️ **No Ambiguous Characters** | Filter out visually confusing characters (`0`, `O`, `l`, `1`, `I`, `|`) with a single click. |
| 📏 **Flexible Length Control** | Adjust password length seamlessly between **8 and 64 characters** via interactive slider or spinbox. |
| 🎲 **Guaranteed Diversity** | Guarantees at least one character from every enabled character set before secure shuffling. |
| 📋 **Quick Clipboard Copy** | One-click copy action directly to system clipboard for immediate use. |
| 📜 **Recent History** | Keeps a running log of the last **5 generated passwords** for easy re-selection. |
| 💻 **Compact Native GUI** | Modern, clutter-free user interface built with Tkinter using the clean `clam` theme. |

---

# 📁 PROJECT STRUCTURE

```text
password-generator/
│
├── .gitignore          # Files and directories ignored by Git
├── Password_Gen.py     # Main application entry point & Tkinter GUI
├── Password_Logic.py   # Core password generation & security logic
├── requirements.txt    # Dependency notes (Standard library only)
└── README.md           # Project documentation
📋 REQUIREMENTS
System Prerequisites
This application runs purely on Python Standard Library packages — zero external pip dependencies are required!

Python Version: 3.6 or higher

Standard Modules: tkinter, secrets, string

💡 Linux Users: If tkinter is not installed on your system by default, install it via your package manager:

Bash
sudo apt install python3-tk    # Ubuntu / Debian
sudo dnf install python3-tkinter # Fedora / RHEL
🚀 GETTING STARTED
1. Download or Clone
Clone the repository or download the source code:

Bash
git clone [https://github.com/your-username/password-generator.git](https://github.com/your-username/password-generator.git)
cd password-generator
2. Run the Application
Launch the desktop GUI with Python:

Bash
python Password_Gen.py
👤 AUTHOR
Developed by @ Niraj Jain

Crafted for security, convenience, and privacy.