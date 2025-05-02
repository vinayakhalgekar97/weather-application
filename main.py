import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_current_weather_forecast():
    city = input("Enter City Name: ") 
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"
    response = requests.get(request_url).json()
    print("******** CURRENT WEATHER DATA *********")
    return f"City: {response['name']}\nCurrent Temperature: {response['main']['temp']} Degree Celsius. \nHumidity: {response['main']['humidity']}% \nDescription: {response['weather'][0]['description']}"

if __name__ == "__main__":
    print(get_current_weather_forecast())