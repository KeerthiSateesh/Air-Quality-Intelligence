import pandas as pd

# Load AQI data
aqi = pd.read_csv("data/raw/city_day.csv")

# Load Health data
health = pd.read_csv("data/raw/RS_249_AU3438.csv")

# Clean AQI
aqi = aqi[['City','Date','PM2.5','PM10','NO2','SO2','CO','O3','AQI']]
aqi['Date'] = pd.to_datetime(aqi['Date'])
aqi = aqi.dropna()
aqi['Year'] = aqi['Date'].dt.year

# Clean Health
health = health[['Year','Cases']]
health = health.dropna()

# Merge on Year
master = pd.merge(aqi, health, on='Year', how='left')

# Save final dataset
master.to_csv("data/processed/master_aqi_health.csv", index=False)

print("SUCCESS! Master AQI + Health dataset created!")
print(master.head())

