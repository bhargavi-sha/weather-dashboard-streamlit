import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="Weather Dashboard", layout="centered")

st.title("🌤️ Live Weather Dashboard")

# Neon DB connection
conn = psycopg2.connect(
    host="ep-still-term-ah5qr6gm-pooler.c-3.us-east-1.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_PEseny68pDNA",
    port="5432",
    sslmode="require"
)

query = """
SELECT city, temperature, humidity, wind_speed, weather_condition, recorded_at
FROM weather_data
ORDER BY recorded_at DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)
conn.close()

# Display metrics
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
