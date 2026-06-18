print("Script started")
import pandas as pd
import random
from datetime import datetime, timedelta

areas = [
    "Manchester Airport",
    "Piccadilly",
    "Deansgate",
    "MediaCityUK",
    "Trafford Centre",
    "Salford Quays",
    "Old Trafford",
    "Stockport"
]

rows = []

start_date = datetime(2025, 1, 1)

for trip_id in range(1, 5001):

    trip_date = start_date + timedelta(
        days=random.randint(0, 365)
    )

    pickup = random.choice(areas)
    dropoff = random.choice(areas)

    distance = round(random.uniform(1, 25), 2)

    duration = round(distance * random.uniform(2, 4), 1)

    fare = round(distance * random.uniform(1.8, 3.0), 2)

    tip = round(random.uniform(0, 5), 2)

    total = fare + tip

    rows.append([
        trip_id,
        trip_date,
        pickup,
        dropoff,
        distance,
        duration,
        fare,
        tip,
        total
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "trip_id",
        "trip_date",
        "pickup_area",
        "dropoff_area",
        "distance_miles",
        "duration_minutes",
        "fare",
        "tip",
        "total_earnings"
    ]
)

df.to_csv(
    "data/raw/trips_raw.csv",
    index=False
)

print("Dataset created successfully")