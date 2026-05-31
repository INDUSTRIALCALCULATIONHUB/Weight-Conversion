import tkinter as tk
from tkinter import messagebox


class WeightConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Conversion Calculator")
        self.root.geometry("450x250")
        self.root.resizable(False, False)

        # Variables
        self.kg_var = tk.StringVar()
        self.n_var = tk.StringVar()
        self.kn_var = tk.StringVar()

        # Heading
        heading = tk.Label(
            root,
            text="Weight Conversion Calculator",
            font=("Arial", 14, "bold")
        )
        heading.grid(row=0, column=0, columnspan=2, pady=15)

        # Input Fields
        tk.Label(root, text="Mass (kg)", font=("Arial", 11)).grid(
            row=1, column=0, padx=10, pady=10, sticky="w"
        )
        tk.Entry(root, textvariable=self.kg_var, width=25).grid(
            row=1, column=1, padx=10
        )

        tk.Label(root, text="Force (N)", font=("Arial", 11)).grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )
        tk.Entry(root, textvariable=self.n_var, width=25).grid(
            row=2, column=1, padx=10
        )

        tk.Label(root, text="Force (kN)", font=("Arial", 11)).grid(
            row=3, column=0, padx=10, pady=10, sticky="w"
        )
        tk.Entry(root, textvariable=self.kn_var, width=25).grid(
            row=3, column=1, padx=10
        )

        # Buttons
        tk.Button(
            root,
            text="Calculate",
            width=15,
            command=self.calculate,
            bg="lightgreen"
        ).grid(row=4, column=0, pady=20)

        tk.Button(
            root,
            text="Reset",
            width=15,
            command=self.reset,
            bg="lightcoral"
        ).grid(row=4, column=1)

    def calculate(self):
        try:
            kg = self.kg_var.get().strip()
            n = self.n_var.get().strip()
            kn = self.kn_var.get().strip()

            entered_fields = sum(bool(x) for x in [kg, n, kn])

            if entered_fields == 0:
                messagebox.showerror(
                    "Input Error",
                    "Please enter a value in one field."
                )
                return

            if entered_fields > 1:
                messagebox.showerror(
                    "Input Error",
                    "Enter value in only one field."
                )
                return

            # Conversion from kg
            if kg:
                kg_val = float(kg)
                n_val = kg_val * 9.81
                kn_val = n_val / 1000

            # Conversion from N
            elif n:
                n_val = float(n)
                kg_val = n_val / 9.81
                kn_val = n_val / 1000

            # Conversion from kN
            elif kn:
                kn_val = float(kn)
                n_val = kn_val * 1000
                kg_val = n_val / 9.81

            # Display results
            self.kg_var.set(f"{kg_val:.2f}")
            self.n_var.set(f"{n_val:.2f}")
            self.kn_var.set(f"{kn_val:.2f}")

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid numeric value."
            )

    def reset(self):
        self.kg_var.set("")
        self.n_var.set("")
        self.kn_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = WeightConverter(root)
    root.mainloop()