-- Total revenue by pickup area
SELECT
    pickup_area,
    COUNT(*) AS total_trips,
    ROUND(SUM(total_earnings), 2) AS total_revenue,
    ROUND(AVG(total_earnings), 2) AS avg_earnings_per_trip,
    ROUND(AVG(earnings_per_hour), 2) AS avg_earnings_per_hour,
    ROUND(AVG(earnings_per_mile), 2) AS avg_earnings_per_mile
FROM trips
GROUP BY pickup_area
ORDER BY avg_earnings_per_hour DESC;


-- Most profitable dropoff areas
SELECT
    dropoff_area,
    COUNT(*) AS total_trips,
    ROUND(SUM(total_earnings), 2) AS total_revenue,
    ROUND(AVG(total_earnings), 2) AS avg_earnings_per_trip
FROM trips
GROUP BY dropoff_area
ORDER BY total_revenue DESC;


-- Best overall trips by earnings per hour
SELECT
    trip_id,
    trip_date,
    pickup_area,
    dropoff_area,
    total_earnings,
    duration_minutes,
    ROUND(earnings_per_hour, 2) AS earnings_per_hour
FROM trips
ORDER BY earnings_per_hour DESC
LIMIT 20;