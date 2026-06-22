# Manchester Ride-Hailing Demand Analytics

A portfolio data analytics project analysing ride-hailing trip profitability across Greater Manchester using Python, SQL, interactive maps and Power BI.

## Business Problem

As a self-employed ride-hailing driver, profitability depends on more than simply being busy. The key question is:

> Which areas, times and trip types generate the best earnings per hour?

This project analyses simulated ride-hailing trip data based on real operational business questions, including airport-trip profitability, pickup-zone performance and revenue optimisation.

## Objectives

- Identify the most profitable pickup areas in Greater Manchester
- Compare airport and non-airport trip profitability
- Calculate earnings per hour and earnings per mile
- Build a repeatable ETL pipeline using Python
- Write SQL queries for business analysis
- Create an interactive profitability heatmap
- Design a Power BI dashboard for business decision-making

## Tech Stack

- Python
- Pandas
- SQL
- Power BI
- Folium
- Git
- GitHub

## Project Structure

```text
manchester-ride-hailing-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── generate_sample_data.py
│   ├── clean_data.py
│   ├── analyze_profitability.py
│   └── create_heatmap.py
│
├── sql/
│   ├── create_tables.sql
│   ├── profitability_analysis.sql
│   └── airport_analysis.sql
│
├── maps/
│   └── manchester_profitability_heatmap.html
│
├── dashboards/
│
├── README.md
├── requirements.txt
└── .gitignore