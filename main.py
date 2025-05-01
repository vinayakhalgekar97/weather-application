import requests
from dotenv import load_dotenv
import os

load_dotenv()

city = input("Enter city name: ") 

request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

response = requests.get(request_url)

print(response.json())