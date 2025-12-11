import tkinter as tk
from tkinter import messagebox
from api_handler import get_weather
from utils import format_weather_data


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Weather App (No API Key Required)")
        self.root.geometry("450x400")

        tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
        self.city_entry = tk.Entry(root, font=("Arial", 12))
        self.city_entry.pack(pady=5)

        tk.Button(root, text="Get Weather", command=self.get_weather, font=("Arial", 12)).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
        self.result_label.pack(pady=20)

    def get_weather(self):
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return

        data = get_weather(city)

        if not data:
            messagebox.showerror("Error", "Unable to fetch weather data")
            return

        self.result_label.config(text=format_weather_data(data))


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
