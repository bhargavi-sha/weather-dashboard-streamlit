import requests
import psycopg2
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

CITY = "Delhi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("""
INSERT INTO weather_data
(city, temperature, humidity, wind_speed, weather_condition)
VALUES (%s, %s, %s, %s, %s)
""", (
    data["name"],
    data["main"]["temp"],
    data["main"]["humidity"],
    data["wind"]["speed"],
    data["weather"][0]["description"]
))

conn.commit()
cur.close()
conn.close()

print("✅ Weather data inserted successfully")
