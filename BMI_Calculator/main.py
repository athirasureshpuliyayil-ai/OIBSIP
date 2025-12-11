import tkinter as tk
from tkinter import messagebox
from bmi_utils import calculate_bmi, get_bmi_category, get_health_tips
from db_handler import save_bmi_record, load_bmi_history
import matplotlib.pyplot as plt

# Main Application Class
class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced BMI Calculator")
        self.root.geometry("400x500")

        # User Input
        tk.Label(root, text="Enter Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Height (cm):").pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        tk.Label(root, text="Weight (kg):").pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        tk.Button(root, text="Calculate BMI", command=self.calculate_bmi).pack(pady=10)
        tk.Button(root, text="Show BMI History", command=self.show_history).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def calculate_bmi(self):
        name = self.name_entry.get().strip()
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Height and Weight must be numbers.")
            return

        if height <= 0 or weight <= 0:
            messagebox.showerror("Invalid Input", "Height and Weight must be positive numbers.")
            return

        bmi = calculate_bmi(height, weight)
        category = get_bmi_category(bmi)
        tips = get_health_tips(category)
        self.result_label.config(text=f"{name}'s BMI: {bmi:.2f}\nCategory: {category}\nTips: {tips}")

        # Save to CSV
        save_bmi_record(name, height, weight, bmi, category)

    def show_history(self):
        history = load_bmi_history()
        if not history:
            messagebox.showinfo("History", "No BMI records found.")
            return

        names = [record['Name'] for record in history]
        bmis = [record['BMI'] for record in history]

        plt.figure(figsize=(8,5))
        plt.bar(names, bmis, color='skyblue')
        plt.ylabel("BMI")
        plt.title("BMI History")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
