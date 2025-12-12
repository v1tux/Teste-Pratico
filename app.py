from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Weather, Base
import os
import requests

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://usuario:senha@db:5432/weather_db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "São Paulo")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt"

def fetch_and_store_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        session = Session()
        entry = Weather(**weather_data)
        session.add(entry)
        session.commit()
        session.close()

@app.route("/weather", methods=["GET"])
def get_weather():
    session = Session()
    results = session.query(Weather).all()
    data = [
        {
            "city": w.city,
            "temperature": w.temperature,
            "humidity": w.humidity,
            "description": w.description
        } for w in results
    ]
    session.close()
    return jsonify(data)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    fetch_and_store_weather()
    app.run(host="0.0.0.0", port=5000)
