import pandas as pd

df = pd.read_csv("data/raw/trips_raw.csv")

print(f"Rows loaded: {len(df)}")

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Create profitability metrics
df["earnings_per_mile"] = (
    df["total_earnings"] / df["distance_miles"]
)

df["earnings_per_hour"] = (
    df["total_earnings"] /
    (df["duration_minutes"] / 60)
)

# Airport flag
df["airport_trip"] = (
    (df["pickup_area"] == "Manchester Airport") |
    (df["dropoff_area"] == "Manchester Airport")
)

df.to_csv(
    "data/processed/trips_clean.csv",
    index=False
)

print("Cleaned dataset saved")