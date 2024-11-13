# weather_cli_tool/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    base_url: str = "http://api.openweathermap.org/data/2.5/weather"
    units: str = "metric"

    class Config:
        env_file = ".env"

settings = Settings()
