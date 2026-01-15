import pandas as pd

df = pd.read_csv("data/processed/master_aqi_health.csv")

def calculate_hri(row):
    score = 0
    
    if row['PM2.5'] > 35: score += 2
    if row['PM10'] > 150: score += 2
    if row['NO2'] > 200: score += 1
    if row['O3'] > 180: score += 1
    if row['CO'] > 10: score += 1
    
    return score

df['Health_Risk_Score'] = df.apply(calculate_hri, axis=1)

def risk_level(score):
    if score <= 1: return "Low"
    elif score <= 3: return "Moderate"
    elif score <= 5: return "High"
    else: return "Severe"

df['Health_Risk_Level'] = df['Health_Risk_Score'].apply(risk_level)

df.to_csv("data/processed/final_health_risk_dataset.csv", index=False)

print("Health Risk Intelligence Dataset Created!")
print(df[['City','Date','AQI','Health_Risk_Level']].head())
