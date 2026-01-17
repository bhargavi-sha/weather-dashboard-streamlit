import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="Weather Dashboard", layout="centered")
st.title("🌤️ Live Weather Dashboard")

# Connect using DATABASE_URL
conn = psycopg2.connect(st.secrets["DATABASE_URL"])

query = """
SELECT city, temperature, humidity, wind_speed, weather_condition, recorded_at
FROM weather_data
ORDER BY recorded_at DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)
conn.close()

latest = df.iloc[0]

st.subheader(f"📍 City: {latest['city']}")

col1, col2, col3 = st.columns(3)
col1.metric("🌡 Temperature (°C)", latest["temperature"])
col2.metric("💧 Humidity (%)", latest["humidity"])
col3.metric("💨 Wind Speed", latest["wind_speed"])

st.markdown(f"**Condition:** {latest['weather_condition']}")

st.divider()
st.subheader("📊 Weather History")
st.dataframe(df)
