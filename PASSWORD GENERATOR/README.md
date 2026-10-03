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



```

---

## REQUIREMENTS

This application uses Python's standard library. No external `pip` dependencies are needed.

* **Python Version**: 3.6 or higher
* **Standard Modules**: `tkinter`, `secrets`, `string`

### Linux Setup

If `tkinter` is not installed by default on your Linux distribution:

```bash
sudo apt install python3-tk       
sudo dnf install python3-tkinter  

```

---

## GETTING STARTED

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/password-generator.git](https://github.com/your-username/password-generator.git)
cd password-generator

```


2. **Run the application:**
```bash
pip install -r requirements.txt
python Password_Gen.py

```





---

## HOW TO USE

1. **Select Length**: Adjust the password length (8 to 64 characters) using the slider or spinbox.
2. **Choose Character Sets**: Select which character types to include (Uppercase, Lowercase, Numbers, Symbols).
3. **Toggle Ambiguous Filter**: Check "Exclude Ambiguous Characters" if you want to leave out similar-looking characters like `0`, `O`, `1`, `l`, `I`, and `|`.
4. **Generate**: Click **Generate Password** to create a new password.
5. **Copy**: Click **Copy** to copy the generated password to your clipboard.
6. **Reuse History**: Select any item from the **Password History** box at the bottom to re-populate the output field.

---

## SECURITY NOTE

* **Cryptographically Secure Randomness**: Passwords are generated using Python's `secrets` module (Cryptographically Secure Pseudo-Random Number Generator), making them secure against brute-force pattern predictions.
* **Zero Disk Persistence**: Password history is stored strictly in temporary application memory (`RAM`). Nothing is saved to a database, log file, or external server.
* **Clipboard Security**: Be mindful when copying passwords to your system clipboard; clear your clipboard after pasting to prevent other local background software from reading sensitive values.

---



---

# 👤 AUTHOR

### **DEVELOPED BY @ NIRAJ JAIN**


