import requests

# Free Open-Meteo API (No API key needed)
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"


def get_weather(city):
    try:
        # 1. Convert city to latitude & longitude
        geo_response = requests.get(GEO_URL, params={"name": city})
        geo_data = geo_response.json()

        if "results" not in geo_data:
            return None

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # 2. Get weather for location
        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }
        )

        weather_data = weather_response.json()

        return {
            "city": city.title(),
            "temperature": weather_data["current_weather"]["temperature"],
            "windspeed": weather_data["current_weather"]["windspeed"],
            "weather_code": weather_data["current_weather"]["weathercode"]
        }

    except Exception as e:
        print("Error:", e)
        return None
