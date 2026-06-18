-- Airport vs non-airport profitability
SELECT
    airport_trip,
    COUNT(*) AS total_trips,
    ROUND(SUM(total_earnings), 2) AS total_revenue,
    ROUND(AVG(total_earnings), 2) AS avg_earnings_per_trip,
    ROUND(AVG(duration_minutes), 2) AS avg_duration_minutes,
    ROUND(AVG(distance_miles), 2) AS avg_distance_miles,
    ROUND(AVG(earnings_per_hour), 2) AS avg_earnings_per_hour,
    ROUND(AVG(earnings_per_mile), 2) AS avg_earnings_per_mile
FROM trips
GROUP BY airport_trip
ORDER BY avg_earnings_per_hour DESC;


-- Trips starting from Manchester Airport
SELECT
    dropoff_area,
    COUNT(*) AS total_airport_pickups,
    ROUND(SUM(total_earnings), 2) AS total_revenue,
    ROUND(AVG(total_earnings), 2) AS avg_earnings,
    ROUND(AVG(earnings_per_hour), 2) AS avg_earnings_per_hour
FROM trips
WHERE pickup_area = 'Manchester Airport'
GROUP BY dropoff_area
ORDER BY avg_earnings_per_hour DESC;


-- Trips ending at Manchester Airport
SELECT
    pickup_area,
    COUNT(*) AS total_airport_dropoffs,
    ROUND(SUM(total_earnings), 2) AS total_revenue,
    ROUND(AVG(total_earnings), 2) AS avg_earnings,
    ROUND(AVG(earnings_per_hour), 2) AS avg_earnings_per_hour
FROM trips
WHERE dropoff_area = 'Manchester Airport'
GROUP BY pickup_area
ORDER BY avg_earnings_per_hour DESC;