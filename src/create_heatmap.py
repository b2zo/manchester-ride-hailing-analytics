import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("data/processed/trips_clean.csv")

area_coordinates = {
    "Manchester Airport": [53.3650, -2.2727],
    "Piccadilly": [53.4774, -2.2309],
    "Deansgate": [53.4740, -2.2500],
    "MediaCityUK": [53.4721, -2.2973],
    "Trafford Centre": [53.4658, -2.3499],
    "Salford Quays": [53.4701, -2.2936],
    "Old Trafford": [53.4631, -2.2913],
    "Stockport": [53.4106, -2.1575],
}

area_profit = (
    df.groupby("pickup_area")
    .agg(
        total_trips=("trip_id", "count"),
        avg_earnings_per_hour=("earnings_per_hour", "mean"),
        total_earnings=("total_earnings", "sum"),
    )
    .reset_index()
)

area_profit["lat"] = area_profit["pickup_area"].map(
    lambda x: area_coordinates[x][0]
)

area_profit["lon"] = area_profit["pickup_area"].map(
    lambda x: area_coordinates[x][1]
)

heat_data = area_profit[
    ["lat", "lon", "avg_earnings_per_hour"]
].values.tolist()

m = folium.Map(
    location=[53.4808, -2.2426],
    zoom_start=11
)

HeatMap(
    heat_data,
    radius=35,
    blur=20,
    max_zoom=13
).add_to(m)

for _, row in area_profit.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=(
            f"<b>{row['pickup_area']}</b><br>"
            f"Trips: {row['total_trips']}<br>"
            f"Avg earnings/hour: £{row['avg_earnings_per_hour']:.2f}<br>"
            f"Total earnings: £{row['total_earnings']:.2f}"
        ),
        tooltip=row["pickup_area"]
    ).add_to(m)

m.save("maps/manchester_profitability_heatmap.html")

print("Heatmap created successfully")