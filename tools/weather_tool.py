import os
import requests

def weather_fetch(city):
    """
    Fetches current weather for a city.
    Handles API errors gracefully.
    """
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {
            "error": "WEATHER_API_KEY is missing"
        }

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url, timeout=10)

    # ❗ Handle HTTP errors
    if response.status_code != 200:
        return {
            "error": f"Weather API error: {response.status_code}",
            "details": response.text
        }

    data = response.json()

    # ❗ Handle unexpected response format
    if "main" not in data:
        return {
            "error": "Unexpected weather API response",
            "response": data
        }

    return {
        "city": city,
        "temperature_celsius": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    }
