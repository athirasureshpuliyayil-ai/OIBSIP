def format_weather_data(data):
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        95: "Thunderstorm"
    }

    condition = weather_codes.get(data["weather_code"], "Unknown")

    return (
        f"City: {data['city']}\n"
        f"Temperature: {data['temperature']}°C\n"
        f"Wind Speed: {data['windspeed']} km/h\n"
        f"Condition: {condition}"
    )
