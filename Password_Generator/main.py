import tkinter as tk
from tkinter import messagebox
from password_utils import generate_password, check_strength
from storage import save_password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x400")

        # Password length
        tk.Label(root, text="Password Length:").pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()
        self.length_entry.insert(0, "12")

        # Options
        self.include_upper = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Uppercase", variable=self.include_upper).pack()
        self.include_lower = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Lowercase", variable=self.include_lower).pack()
        self.include_digits = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).pack()
        self.include_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols).pack()

        # Buttons
        tk.Button(root, text="Generate Password", command=self.generate).pack(pady=10)
        tk.Button(root, text="Save Password", command=self.save_password).pack(pady=5)
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

        # Output
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, width=30, font=("Helvetica", 12))
        self.password_entry.pack(pady=10)

        self.strength_label = tk.Label(root, text="", font=("Helvetica", 10))
        self.strength_label.pack()

    def generate(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Length must be a number")
            return

        password = generate_password(length,
                                     self.include_upper.get(),
                                     self.include_lower.get(),
                                     self.include_digits.get(),
                                     self.include_symbols.get())
        self.password_var.set(password)
        self.strength_label.config(text=f"Strength: {check_strength(password)}")

    def save_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showerror("Error", "No password to save")
            return
        save_password(password)
        messagebox.showinfo("Saved", "Password saved successfully!")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
