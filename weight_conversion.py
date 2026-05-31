import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        kg = kg_var.get().strip()
        n = n_var.get().strip()
        kn = kn_var.get().strip()

        filled = sum(bool(x) for x in [kg, n, kn])

        if filled != 1:
            messagebox.showerror(
                "Input Error",
                "Please enter value in only one field."
            )
            return

        if kg:
            kg_val = float(kg)
            n_val = kg_val * 9.81
            kn_val = n_val / 1000

        elif n:
            n_val = float(n)
            kg_val = n_val / 9.81
            kn_val = n_val / 1000

        elif kn:
            kn_val = float(kn)
            n_val = kn_val * 1000
            kg_val = n_val / 9.81

        kg_var.set(f"{kg_val:.2f}")
        n_var.set(f"{n_val:.2f}")
        kn_var.set(f"{kn_val:.2f}")

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Please enter a valid numeric value."
        )

def reset():
    kg_var.set("")
    n_var.set("")
    kn_var.set("")

# Main Window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("350x220")
root.resizable(False, False)

# Variables
kg_var = tk.StringVar()
n_var = tk.StringVar()
kn_var = tk.StringVar()

# Labels and Entries
tk.Label(root, text="Kg", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=kg_var, width=20).grid(row=0, column=1)

tk.Label(root, text="N", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=n_var, width=20).grid(row=1, column=1)

tk.Label(root, text="kN", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=kn_var, width=20).grid(row=2, column=1)

# Buttons
tk.Button(root, text="Calculate", width=12, command=calculate).grid(
    row=3, column=0, pady=20
)

tk.Button(root, text="Reset", width=12, command=reset).grid(
    row=3, column=1
)

root.mainloop()