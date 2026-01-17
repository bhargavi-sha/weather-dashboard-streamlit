import requests
import psycopg2

API_KEY = "f91b07f8d7532931ff19d6d483db411d"
CITY = "Delhi"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# 1️⃣ Call Weather API
response = requests.get(url)
data = response.json()

city = data["name"]
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
weather_condition = data["weather"][0]["description"]

# 2️⃣ Connect to Neon PostgreSQL
conn = psycopg2.connect(
    host="ep-still-term-ah5qr6gm-pooler.c-3.us-east-1.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_PEseny68pDNA",
    port="5432",
    sslmode="require"
)

cur = conn.cursor()

# 3️⃣ Insert data
cur.execute(
    """
    INSERT INTO weather_data
    (city, temperature, humidity, wind_speed, weather_condition)
    VALUES (%s, %s, %s, %s, %s)
    """,
    (city, temperature, humidity, wind_speed, weather_condition)
)

conn.commit()
cur.close()
conn.close()

print("✅ Weather data inserted successfully")
