# weather_cli_tool/main.py
import requests
from pydantic import BaseModel, ValidationError
from config import settings

# Define a Pydantic model for the weather data response
class WeatherResponse(BaseModel):
    temp: float
    description: str
    humidity: int

def get_weather(city: str):
    # Prepare request parameters
    params = {
        "q": city,
        "appid": settings.api_key,
        "units": settings.units
    }

    # Make the API request
    try:
        response = requests.get(settings.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Parse response with Pydantic model
        weather = WeatherResponse(
            temp=data['main']['temp'],
            description=data['weather'][0]['description'],
            humidity=data['main']['humidity']
        )

        # Display weather data
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {weather.temp}°C")
        print(f"Condition: {weather.description.capitalize()}")
        print(f"Humidity: {weather.humidity}%")

    except ValidationError as e:
        print("Data validation error:", e)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
