def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI given height in cm and weight in kg"""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    """Return BMI category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_health_tips(category):
    """Return health tips based on BMI category"""
    tips = {
        "Underweight": "Eat more calories with nutritious food, include proteins and carbs.",
        "Normal weight": "Maintain your current lifestyle, exercise regularly.",
        "Overweight": "Consider a balanced diet and regular exercise.",
        "Obese": "Consult a doctor, follow a strict diet and exercise plan."
    }
    return tips.get(category, "")
