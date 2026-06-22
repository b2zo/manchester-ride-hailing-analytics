import pandas as pd

df = pd.read_csv("data/raw/trips_raw.csv")

print(f"Rows loaded: {len(df)}")

df = df.drop_duplicates()
df = df.dropna()

df["start_datetime"] = pd.to_datetime(df["start_datetime"])
df["trip_date"] = pd.to_datetime(df["trip_date"])

df["earnings_per_mile"] = df["total_earnings"] / df["distance_miles"]

df["earnings_per_hour"] = (
    df["total_earnings"] /
    (df["duration_minutes"] / 60)
)

df["profit_per_hour"] = (
    df["net_profit"] /
    (df["duration_minutes"] / 60)
)

df["is_weekend"] = df["day_of_week"].isin(["Friday", "Saturday", "Sunday"])

df.to_csv("data/processed/trips_clean.csv", index=False)

print("Cleaned dataset saved")