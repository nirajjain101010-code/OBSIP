# OBSIP
Python Programming Internship projects — Oasis Infobyte (OIBSIP). Voice Assistant, BMI Calculator, Password Generator, Weather App, and a real-time Chat Application built with Python.
I have saved the formatted file for you. You can directly save and use the code below as your `README.md` file:

```markdown
# Password Generator

**Developer:** @ Niraj Jain

A desktop GUI application (tkinter) that generates strong, cryptographically
secure passwords based on user-defined length and character-type criteria,
with history tracking and one-click clipboard copy.

## Features

- [x] GUI with a slider + spinbox for length, and checkboxes for character
      type selection
- [x] Uses the `secrets` module (not `random`) for all randomness —
      cryptographically secure generation
- [x] Guaranteed inclusion of at least one character from every selected
      type (verified through character category enforcement)
- [x] "Copy to Clipboard" button using native `tkinter` clipboard support
- [x] Option to exclude ambiguous characters (`0 O 1 l I |`)
- [x] Session history — the last 5 generated passwords are shown in a
      list; nothing is ever written to disk, for security
- [x] Clean desktop UI styled with the modern Tkinter `clam` theme

## Project Structure


```

password-generator/
├── .gitignore
├── Password_Gen.py     # Main GUI application (entry point)
├── Password_Logic.py   # Core password generation & security logic
├── requirements.txt    # Dependency notes (Standard library only)
└── README.md

```

## Setup


```

python Password_Gen.py

```

`tkinter`, `secrets`, and `string` ship with Python's standard library — zero
third-party dependencies are required. On Linux, if `tkinter` is not installed by
default, install it via your package manager (`sudo apt install python3-tk`).

## How to Use

1. Set the desired **length** (8–64) with the slider or spinbox.
2. Check which **character types** to include (uppercase, lowercase, digits, symbols).
3. Optionally check **exclude ambiguous characters** to avoid characters
   that look alike (`0`/`O`, `1`/`l`/`I`/`|`).
4. Click **Generate Password** — the result is displayed and ready to use.
5. Click any entry in **Recent Passwords** to bring it back into the
   result field, or use the **Copy** button to copy it to your clipboard.

## Security Notes

- Randomness comes from `secrets.choice()` / `secrets.randbelow()`
  throughout — never Python's general-purpose `random` module, which is
  not safe for security-sensitive generation.
- The required-character-per-type guarantee is implemented by first
  drawing one guaranteed character from each selected pool, then filling
  the remainder and shuffling with a cryptographically secure
  Fisher–Yates shuffle (using `secrets.randbelow`) so the guaranteed
  characters aren't predictably placed at the start of the password.
- Generated passwords are kept in memory only for the current session
  and are never written to a file or database.

```
