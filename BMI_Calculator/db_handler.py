import csv
import os

FILE_NAME = "bmi_history.csv"

def save_bmi_record(name, height, weight, bmi, category):
    """Save BMI record to CSV"""
    file_exists = os.path.isfile(FILE_NAME)
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Height", "Weight", "BMI", "Category"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "Name": name,
            "Height": height,
            "Weight": weight,
            "BMI": round(bmi, 2),
            "Category": category
        })

def load_bmi_history():
    """Load BMI history from CSV"""
    if not os.path.isfile(FILE_NAME):
        return []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        return [{"Name": row["Name"], "Height": float(row["Height"]), "Weight": float(row["Weight"]),
                 "BMI": float(row["BMI"]), "Category": row["Category"]} for row in reader]
