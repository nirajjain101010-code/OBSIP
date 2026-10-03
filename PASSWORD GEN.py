import math
import secrets
import string
import tkinter as tk
from tkinter import messagebox, ttk


class PasswordGeneratorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator by @ Niraj Jain")
        self.root.geometry("350x480")
        self.root.resizable(False, False)

        # Style setup
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Variables
        self.length_var = tk.IntVar(value=16)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.no_ambiguous = tk.BooleanVar(value=False)

        self.history = []

        self._build_ui()

    def _build_ui(self):
        ttk.Label(
            self.root, text="Password Generator Security", font=("Helvetica", 14, "bold")
        ).pack(pady=12)

        # Settings box
        options = ttk.LabelFrame(self.root, text=" Settings ", padding=(10, 5))
        options.pack(fill="x", padx=15, pady=5)

        # Length selection
        len_frame = ttk.Frame(options)
        len_frame.pack(fill="x", pady=5)

        ttk.Label(len_frame, text="Length:").pack(side="left")
        ttk.Spinbox(
            len_frame, from_=8, to=64, textvariable=self.length_var, width=5
        ).pack(side="right")
        ttk.Scale(
            len_frame,
            from_=8,
            to=64,
            variable=self.length_var,
            orient="horizontal",
        ).pack(side="right", fill="x", expand=True, padx=8)

        # Character options
        ttk.Checkbutton(
            options,
            text="Include Uppercase Letters",
            variable=self.use_upper,
        ).pack(anchor="w", pady=2)
        ttk.Checkbutton(
            options,
            text="Include Lowercase Letters",
            variable=self.use_lower,
        ).pack(anchor="w", pady=2)
        ttk.Checkbutton(
            options, text="Include Numbers", variable=self.use_digits
        ).pack(anchor="w", pady=2)
        ttk.Checkbutton(
            options, text="Include Symbols", variable=self.use_symbols
        ).pack(anchor="w", pady=2)
        ttk.Checkbutton(
            options,
            text="Exclude Ambiguous Characters",
            variable=self.no_ambiguous,
        ).pack(anchor="w", pady=2)

        ttk.Button(
            self.root, text="Generate Password", command=self.generate
        ).pack(pady=10)

        # Output field & copy button
        out_frame = ttk.Frame(self.root)
        out_frame.pack(fill="x", padx=15, pady=5)

        self.output_entry = ttk.Entry(out_frame, font=("Courier", 11))
        self.output_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        ttk.Button(out_frame, text="Copy", width=8, command=self.copy).pack(
            side="right"
        )

        self.strength_lbl = tk.Label(
            self.root, text="Strength: -", font=("Helvetica", 9, "bold")
        )
        self.strength_lbl.pack(pady=4)

        # History UI
        ttk.Label(self.root, text="Password History:").pack(
            anchor="w", padx=15, pady=(10, 2)
        )

        self.history_box = tk.Listbox(self.root, height=4, font=("Courier", 9))
        self.history_box.pack(fill="x", padx=15)
        self.history_box.bind("<<ListboxSelect>>", self.on_history_select)

    def generate(self):
        sets = []
        ambiguous = "0Ol1I|" if self.no_ambiguous.get() else ""

        def clean(chars):
            return "".join(c for c in chars if c not in ambiguous)

        if self.use_upper.get():
            sets.append(clean(string.ascii_uppercase))
        if self.use_lower.get():
            sets.append(clean(string.ascii_lowercase))
        if self.use_digits.get():
            sets.append(clean(string.digits))
        if self.use_symbols.get():
            sets.append(clean("!@#$%^&*()_+-=[]{}|;:,.<>?"))

        sets = [s for s in sets if s]

        if not sets:
            messagebox.showerror(
                "Error", "Please select at least one valid character set."
            )
            return

        length = self.length_var.get()
        if length < len(sets):
            messagebox.showerror(
                "Error", f"Length must be at least {len(sets)} for selected options."
            )
            return

        password_chars = [secrets.choice(s) for s in sets]
        full_pool = "".join(sets)
        password_chars += [
            secrets.choice(full_pool) for _ in range(length - len(sets))
        ]

        # Shuffle list securely
        for i in range(len(password_chars) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

        password = "".join(password_chars)

        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, password)

        self.check_strength(password, len(full_pool))
        self.add_to_history(password)

    def check_strength(self, pw, pool_size=0):
        if not pw:
            self.strength_lbl.config(text="Strength: -", fg="black")
            return

        # Calculate character pool size if not provided
        if pool_size == 0:
            pool = 0
            if any(c in string.ascii_uppercase for c in pw):
                pool += 26
            if any(c in string.ascii_lowercase for c in pw):
                pool += 26
            if any(c.isdigit() for c in pw):
                pool += 10
            if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pw):
                pool += 32
            pool_size = pool if pool > 0 else 26

        entropy = len(pw) * math.log2(pool_size)

        # Categorize password strength level
        if entropy < 36:
            label, color = "Very Weak", "#d9534f"  # Red
        elif entropy < 60:
            label, color = "Weak", "#f0ad4e"       # Orange
        elif entropy < 80:
            label, color = "Moderate", "#e6b800"   # Yellow
        elif entropy < 100:
            label, color = "Strong", "#5cb85c"     # Light Green
        else:
            label, color = "Very Strong", "#2b8a3e" # Dark Green

        self.strength_lbl.config(
            text=f"Strength: {label} ({int(entropy)} bits)", fg=color
        )

    def add_to_history(self, pw):
        if pw in self.history:
            return

        self.history.insert(0, pw)
        if len(self.history) > 5:
            self.history.pop()

        self.history_box.delete(0, tk.END)
        for item in self.history:
            self.history_box.insert(tk.END, item)

    def copy(self):
        pw = self.output_entry.get()
        if pw:
            self.root.clipboard_clear()
            self.root.clipboard_append(pw)
            messagebox.showinfo("Success", "Password copied to clipboard!")

    def on_history_select(self, event):
        sel = self.history_box.curselection()
        if not sel:
            return

        selected_pw = self.history_box.get(sel[0])
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, selected_pw)
        self.check_strength(selected_pw)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()