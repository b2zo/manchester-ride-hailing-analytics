CREATE TABLE trips (
    trip_id INTEGER PRIMARY KEY,
    trip_date DATE,
    pickup_area VARCHAR(100),
    dropoff_area VARCHAR(100),
    distance_miles NUMERIC(10,2),
    duration_minutes NUMERIC(10,2),
    fare NUMERIC(10,2),
    tip NUMERIC(10,2),
    total_earnings NUMERIC(10,2),
    earnings_per_mile NUMERIC(10,2),
    earnings_per_hour NUMERIC(10,2),
    airport_trip BOOLEAN
);