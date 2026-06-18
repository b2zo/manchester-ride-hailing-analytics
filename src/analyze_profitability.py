import pandas as pd

df = pd.read_csv("data/processed/trips_clean.csv")

print("\nTOP PICKUP AREAS BY REVENUE\n")

area_profit = (
    df.groupby("pickup_area")["total_earnings"]
    .sum()
    .sort_values(ascending=False)
)

print(area_profit)

print("\nTOP AREAS BY EARNINGS PER HOUR\n")

hourly_profit = (
    df.groupby("pickup_area")["earnings_per_hour"]
    .mean()
    .sort_values(ascending=False)
)

print(hourly_profit)

print("\nAIRPORT VS NON-AIRPORT\n")

airport = (
    df.groupby("airport_trip")["earnings_per_hour"]
    .mean()
)

print(airport)