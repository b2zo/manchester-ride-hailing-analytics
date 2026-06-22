import pandas as pd
import random
from datetime import datetime, timedelta

areas = {
    "Manchester Airport": [53.3650, -2.2727],
    "Piccadilly": [53.4774, -2.2309],
    "Deansgate": [53.4740, -2.2500],
    "MediaCityUK": [53.4721, -2.2973],
    "Trafford Centre": [53.4658, -2.3499],
    "Salford Quays": [53.4701, -2.2936],
    "Old Trafford": [53.4631, -2.2913],
    "Stockport": [53.4106, -2.1575],
}

area_distance_band = {
    "Manchester Airport": (8, 22),
    "Piccadilly": (1.5, 9),
    "Deansgate": (1.5, 9),
    "MediaCityUK": (3, 12),
    "Trafford Centre": (4, 14),
    "Salford Quays": (3, 12),
    "Old Trafford": (3, 12),
    "Stockport": (6, 18),
}

def get_time_period(hour):
    if 5 <= hour <= 9:
        return "Early Morning"
    if 10 <= hour <= 15:
        return "Midday"
    if 16 <= hour <= 20:
        return "Evening Peak"
    if 21 <= hour <= 23 or 0 <= hour <= 2:
        return "Night"
    return "Quiet Hours"

def weighted_pickup(hour, day):
    weekend = day in ["Friday", "Saturday", "Sunday"]

    weights = {
        "Manchester Airport": 12,
        "Piccadilly": 14,
        "Deansgate": 14,
        "MediaCityUK": 10,
        "Trafford Centre": 9,
        "Salford Quays": 9,
        "Old Trafford": 8,
        "Stockport": 7,
    }

    if 5 <= hour <= 9:
        weights["Manchester Airport"] += 16
        weights["Stockport"] += 4

    if 16 <= hour <= 20:
        weights["MediaCityUK"] += 8
        weights["Salford Quays"] += 6
        weights["Trafford Centre"] += 5

    if hour >= 21 or hour <= 2:
        weights["Piccadilly"] += 16
        weights["Deansgate"] += 16
        if weekend:
            weights["Manchester Airport"] += 6

    if weekend and hour >= 20:
        weights["Piccadilly"] += 10
        weights["Deansgate"] += 10

    return random.choices(
        list(weights.keys()),
        weights=list(weights.values()),
        k=1
    )[0]

def duration_minutes(distance, hour):
    if 7 <= hour <= 9 or 16 <= hour <= 18:
        mins_per_mile = random.uniform(3.2, 4.8)
    elif hour >= 22 or hour <= 5:
        mins_per_mile = random.uniform(1.8, 2.7)
    else:
        mins_per_mile = random.uniform(2.3, 3.5)

    return round(distance * mins_per_mile + random.uniform(2, 6), 1)

def demand_multiplier(hour, day, pickup, airport_trip):
    multiplier = 1.0

    if 5 <= hour <= 9 and airport_trip:
        multiplier += 0.25

    if pickup in ["Piccadilly", "Deansgate"] and (hour >= 21 or hour <= 2):
        multiplier += 0.30

    if day in ["Friday", "Saturday"] and (hour >= 20 or hour <= 2):
        multiplier += 0.35

    if 16 <= hour <= 19:
        multiplier += 0.15

    if 10 <= hour <= 15:
        multiplier -= 0.08

    return max(multiplier, 0.85)

rows = []
start_date = datetime(2025, 1, 1)

for trip_id in range(1, 7001):
    trip_date = start_date + timedelta(days=random.randint(0, 364))
    day_of_week = trip_date.strftime("%A")

    hour = random.choices(
        population=list(range(24)),
        weights=[
            5, 4, 3, 1, 2,
            8, 9, 10, 9, 7,
            5, 5, 5, 5, 5, 6,
            9, 10, 10, 9, 8,
            10, 11, 8
        ],
        k=1
    )[0]

    minute = random.randint(0, 59)
    start_time = trip_date.replace(hour=hour, minute=minute)

    pickup = weighted_pickup(hour, day_of_week)
    dropoff = random.choice(list(areas.keys()))

    while dropoff == pickup:
        dropoff = random.choice(list(areas.keys()))

    airport_trip = pickup == "Manchester Airport" or dropoff == "Manchester Airport"

    low, high = area_distance_band[pickup]
    distance = round(random.uniform(low, high), 2)

    if airport_trip:
        distance = round(random.uniform(8, 24), 2)

    duration = duration_minutes(distance, hour)

    demand = demand_multiplier(hour, day_of_week, pickup, airport_trip)

    base_fare = 3.00
    per_mile_rate = random.uniform(0.75, 1.10)

    if airport_trip:
        per_mile_rate += random.uniform(0.05, 0.12)

    fare = round((base_fare + distance * per_mile_rate) * demand, 2)

    tip = round(
        random.choices(
            [0, random.uniform(1, 4)],
            weights=[82, 18],
            k=1
        )[0],
        2
    )

    total = round(fare + tip, 2)

    estimated_cost = round(distance * 0.45, 2)
    net_profit = round(total - estimated_cost, 2)

    rows.append([
        trip_id,
        start_time,
        start_time.date(),
        day_of_week,
        start_time.hour,
        get_time_period(start_time.hour),
        pickup,
        dropoff,
        areas[pickup][0],
        areas[pickup][1],
        areas[dropoff][0],
        areas[dropoff][1],
        distance,
        duration,
        fare,
        tip,
        total,
        estimated_cost,
        net_profit,
        airport_trip
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "trip_id",
        "start_datetime",
        "trip_date",
        "day_of_week",
        "hour_of_day",
        "time_period",
        "pickup_area",
        "dropoff_area",
        "pickup_lat",
        "pickup_lon",
        "dropoff_lat",
        "dropoff_lon",
        "distance_miles",
        "duration_minutes",
        "fare",
        "tip",
        "total_earnings",
        "estimated_cost",
        "net_profit",
        "airport_trip"
    ]
)

df.to_csv("data/raw/trips_raw.csv", index=False)

print("Dataset created successfully")