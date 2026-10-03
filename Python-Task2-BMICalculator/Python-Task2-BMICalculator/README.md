
---

# ⚡ Advanced BMI Workstation & Health Tracker

> **A sleek, desktop-grade Health & Fitness Analytics Suite built with Python, CustomTkinter, and Matplotlib.**

---

## 🌟 Overview

The **Advanced BMI Workstation** goes far beyond basic BMI calculators. Engineered with a modular architecture and built for modern desktop environments, this app provides real-time health metrics computation, multi-user profiling, dual-unit conversion support, persistent storage, and interactive trend visualization.

---

## ✨ Key Features

* 🖥️ **Pure GUI Application**: Built with Tkinter / CustomTkinter for a seamless desktop experience — no command line required.
* 📝 **Interactive Inputs & Action**: Input fields for user name, weight (kg), and height (m) featuring a responsive "Calculate BMI" button.
* 🎨 **Color-Coded Feedback**: Instant visual classification cards (blue = underweight, green = normal, orange = overweight, red = obese).
* 👥 **Multi-User Support**: Track and save records under different named user profiles.
* 💾 **Persistent SQLite Database**: Historical records are saved to an SQLite database (`bmi_records.db`), which is automatically created on first run.
* 📈 **Embedded Graph View**: Displays a line chart of a selected user's BMI trend over time using Matplotlib, cleanly embedded in its own dedicated window.
* 🛡 **Robust Input Validation**: Safeguards user entry with clear error dialogs for non-numeric, negative, zero, or empty values.
* ⚙️ **Database Error Handling**: Complete exception handling for database read/write failures.

---

## 📸 Screenshots & UI Preview

| Main Workstation | Analytics & Trends Window |
| --- | --- |
| *Calculates & records individual entries with live color-coded classification cards.* | *Browse, filter, plot, or delete historical health entries per profile.* |

---

## 📊 WHO BMI Classification Standard

The application categorizes measurements according to standard World Health Organization metrics:

| Category | BMI Range | Visual Indicator |
| --- | --- | --- |
| **Underweight** | < 18.5 | 🔵 Blue |
| **Normal Weight** | 18.5 - 24.9 | 🟢 Green |
| **Overweight** | 25.0 - 29.9 | 🟠 Orange |
| **Obese** | ≥ 30.0 | 🔴 Red |

```text
BMI Formula (Metric) = Weight (kg) / (Height (m))^2

```

---

## 🛠️ Architecture & Project Structure

The project follows a modular **Model-View-Controller (MVC)**-style structure for maintainability and clean separation of concerns:

```text
📦 BMI-Workstation
 ┣ 📜 main.py          # CustomTkinter GUI Presentation & Event Handlers
 ┣ 📜 database.py      # SQLite Database Layer & CRUD Operations
 ┣ 📜 bmi_logic.py     # Core Computations, Unit Conversions & Validation
 ┗ 📜 bmi_records.db   # Auto-generated SQLite Database File

```

---

## 🚀 Quick Start Guide

### Prerequisites

* **Python**: Version `3.8` or higher installed.

### 1️⃣ Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/bmi-workstation.git
cd bmi-workstation
pip install customtkinter matplotlib

```

### 2️⃣ Run the Application

Launch the application by running `main.py`:

```bash
python main.py

```

---

## 💡 How to Use

1. **Set Profile & Units**: Type in your name and choose your preferred unit system (**Metric** or **Imperial**).
2. **Compute & Save**: Enter your weight and height, then click **Calculate & Save Entry**.
3. **Analyze Progress**: Click **View Analytics & Trends** to open the history dashboard:
* Select a user filter to examine specific progress graphs over time.
* Highlight individual table rows to clear single entries or purge selected user logs.



---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👨‍💻 Author

* **Niraj Jain** ([GitHub Profile](https://github.com/))