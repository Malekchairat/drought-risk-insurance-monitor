import pandas as pd
import requests

# 1. Define target locations in France (Latitude, Longitude)
CITIES = {
    "Paris (75)": {"lat": 48.8566, "lon": 2.3522},
    "Marseille (13)": {"lat": 43.2965, "lon": 5.3698},
    "Toulouse (31)": {"lat": 43.6047, "lon": 1.4442},
    "Lyon (69)": {"lat": 45.7640, "lon": 4.8357},
}


def get_weather_data():
    records = []

    for city, coords in CITIES.items():
        # Open-Meteo public API endpoint
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": coords["lat"],
            "longitude": coords["lon"],
            "daily": "temperature_2m_max,precipitation_sum",
            "past_days": 14,  # Fetch last 2 weeks of data
            "timezone": "Europe/Paris",
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            daily = data.get("daily", {})

            # Parse daily records
            dates = daily.get("time", [])
            temp_max = daily.get("temperature_2m_max", [])
            precip = daily.get("precipitation_sum", [])

            for i in range(len(dates)):
                records.append(
                    {
                        "Region": city,
                        "Date": dates[i],
                        "Max_Temp_C": temp_max[i],
                        "Precipitation_mm": precip[i],
                    }
                )

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    df = get_weather_data()
    print("✅ Data successfully fetched!")
    print(df.head(10))
    # Save raw data to CSV
    df.to_csv("drought_data.csv", index=False)