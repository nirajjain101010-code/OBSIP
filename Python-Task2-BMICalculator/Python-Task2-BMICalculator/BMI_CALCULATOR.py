import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

DB_FILE = "../bmi_records.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS bmi_history (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name TEXT NOT NULL,
recorded_at TEXT NOT NULL,
weight REAL NOT NULL,
height REAL NOT NULL,
bmi REAL NOT NULL,
category TEXT NOT NULL
)
""")
    conn.commit()
    conn.close()


class HistoryWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Saved History & Chart")
        self.geometry("750x600")
        self.grab_set()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",background="#2b2b2b",foreground="#ffffff",fieldbackground="#2b2b2b", rowheight=25)
        style.configure("Treeview.Heading",background="#1f1f1f",foreground="#ffffff",font=("Arial", 10, "bold"))

        cols = ("ID", "Name", "Date & Time", "Weight (kg)", "Height (m)", "BMI", "Category")
        self.tree = ttk.Treeview(self,columns=cols,show="headings",height=6)

        widths = [40, 100, 140, 80, 80, 60, 120]
        for c, w in zip(cols, widths):
            self.tree.heading(c,text=c)
            self.tree.column(c,width=w,anchor="center")

        self.tree.pack(fill="x", padx=15,pady=(15, 5))

        self.plot_frame = ctk.CTkFrame(self,fg_color="#2b2b2b")
        self.plot_frame.pack(fill="both",expand=True, padx=15,pady=10)

        btn_frame = ctk.CTkFrame(self,fg_color="transparent")
        btn_frame.pack(fill="x",padx=15, pady=(0, 15))

        self.del_all_btn = ctk.CTkButton(btn_frame,text="Clear History",fg_color="#c53030",hover_color="#9b2c2c",command=self.clear_all )
        self.del_all_btn.pack(side="left")

        self.del_btn = ctk.CTkButton(
        btn_frame,text="Delete Selected",command=self.delete_selected)
        self.del_btn.pack(side="right")

        self.load_data()

    def load_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)  # Syntax/TypeError
        try:
            conn = sqlite3.connect(DB_FILE)
            cur =conn.cursor()
            cur.execute("SELECT id, user_name, recorded_at, weight, height, bmi, category FROM bmi_history ORDER BY id DESC")
            records =cur.fetchall()
            conn.close()

            for row in records:
                self.tree.insert("","end",values=row)
            self.plot_chart(records)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load records: {e}")

    def plot_chart(self, records):
        for w in self.plot_frame.winfo_children():
            w.destroy()

        if not records:
            return

        sorted_recs=list(reversed(records))
        dates = [r[2].split(" ")[0] for r in sorted_recs]
        bmis=[r[5] for r in sorted_recs]

        fig, ax = plt.subplots(figsize=(6, 2.5),facecolor="#2b2b2b")
        ax.set_facecolor("#2b2b2b")
        ax.plot(dates, bmis, marker='o',color="#3b82f6",linewidth=2,markersize=6)

        ax.tick_params(colors='white',labelsize=8)
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('#2b2b2b')
        ax.spines['left'].set_color('white')
        ax.spines['right'].set_color('#2b2b2b')
        ax.set_ylabel("BMI Value", color="white", fontsize=9)
        ax.grid(True,color="#404040",linestyle="--",alpha=0.5)

        fig.autofmt_xdate(rotation=30)
        plt.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both",expand=True)

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning","Select a record to delete.")
            return

        vals = self.tree.item(selected[0], "values")
        if messagebox.askyesno("Confirm", f"Delete record #{vals[0]} for '{vals[1]}'?"):
            try:
                conn = sqlite3.connect(DB_FILE)
                cur = conn.cursor()
                cur.execute("DELETE FROM bmi_history WHERE id = ?",(vals[0],))
                conn.commit()
                conn.close()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all saved records?"):
            try:
                conn = sqlite3.connect(DB_FILE)
                cur = conn.cursor()
                cur.execute("DELETE FROM bmi_history")
                conn.commit()
                conn.close()
                self.load_data()
            except Exception as e:
                messagebox.showerror("Error", str(e))


class BMICalculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        init_db()
        self.title("BMI Calculator Made BY @Niraj Jain")
        self.geometry("500x520")
        self.resizable(False,False)
        self.weight_var = ctk.DoubleVar(value=70.0)
        self.height_var = ctk.DoubleVar(value=1.75)
        self.current_bmi = 22.86
        self.current_category = "Normal Weight"

        # User Name Input
        ctk.CTkLabel(self,text="User Name:",font=("Arial", 12, "bold")).pack(anchor="w", padx=25,pady=(20, 5))
        self.name_entry = ctk.CTkEntry(self,placeholder_text="Enter user name")
        self.name_entry.pack(fill="x" ,padx=25,pady=(0, 15))

        # Controls
        self.weight_lbl=ctk.CTkLabel(self, text="Weight: 70.0 kg", font=("Arial", 12))
        self.weight_lbl.pack(anchor="w",padx=25,pady=(5, 0))
        self.weight_slider = ctk.CTkSlider(self,from_=30, to=150,variable=self.weight_var,command=self.calculate_bmi)
        self.weight_slider.pack(fill="x",padx=25,pady=(5, 15))

        self.height_lbl = ctk.CTkLabel(self,text="Height: 1.75 m",font=("Arial", 12))
        self.height_lbl.pack(anchor="w",padx=25, pady=(5, 0))
        self.height_slider = ctk.CTkSlider(self,from_=1.0,to=2.3,variable=self.height_var,command=self.calculate_bmi)
        self.height_slider.pack(fill="x",padx=25,pady=(5, 20))

        # Result card
        self.card = ctk.CTkFrame(self,corner_radius=10)
        self.card.pack(fill="x",padx=25,pady=10)

        self.bmi_val_lbl = ctk.CTkLabel(self.card,text="22.86",font=("Arial", 36, "bold"),text_color="#22c55e")
        self.bmi_val_lbl.pack(pady=(15, 0))

        self.cat_lbl = ctk.CTkLabel(self.card,text="Normal Weight",font=("Arial", 12, "bold"),text_color="#22c55e")
        self.cat_lbl.pack(pady=(0, 15))

        # Buttons
        self.save_btn = ctk.CTkButton(self,text="Save Result",fg_color="#22c55e",hover_color="#16a34a",command=self.save_record)
        self.save_btn.pack(fill="x",padx=25,pady=(15, 5))

        self.hist_btn = ctk.CTkButton(self,text="View History",fg_color="transparent",border_width=1,command=self.open_history)
        self.hist_btn.pack(fill="x",padx=25,pady=5)

        self.calculate_bmi()

    def calculate_bmi(self, *args):
        w =self.weight_var.get()
        h =self.height_var.get()

        self.weight_lbl.configure(text=f"Weight:{w:.1f} kg")
        self.height_lbl.configure(text=f"Height:{h:.2f} m")

        if h>0:
            bmi =round(w / (h * h), 2)
            self.current_bmi = bmi

            if bmi < 18.5:
                cat = "Underweight"
                col = "#38bdf8"
            elif bmi < 25.0:
                cat = "Normal Weight"
                col = "#22c55e"
            elif bmi < 30.0:
                cat = "Overweight"
                col = "#f97316"
            else:
                cat = "Obese"
                col = "#ef4444"
            self.current_category = cat
            self.bmi_val_lbl.configure(text=f"{bmi:.2f}",text_color=col)
            self.cat_lbl.configure(text=cat,text_color=col)

    def save_record(self):
        name =self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Required", "Please enter a user name.")
            return

        try:
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cur.execute("""
                INSERT INTO bmi_history (user_name, recorded_at, weight, height, bmi, category)
                VALUES (?, ?, ?, ?, ?, ?)
            """,(name, now, self.weight_var.get(), self.height_var.get(), self.current_bmi, self.current_category))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success",f"Record saved for {name}.")
            self.name_entry.delete(0,"end")
        except Exception as e:
            messagebox.showerror("Database Error",f"Failed to save:{e}")

    def open_history(self):
        HistoryWindow(self)


if __name__ == "__main__":
    app = BMICalculator()
    app.mainloop()