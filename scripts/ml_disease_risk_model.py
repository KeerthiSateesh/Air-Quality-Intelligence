import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/processed/final_health_risk_dataset.csv")

df['Target'] = df['Health_Risk_Level'].map({
    'Low':0, 'Moderate':1, 'High':2, 'Severe':3
})

features = ['PM2.5','PM10','NO2','SO2','CO','O3','AQI']
X = df[features]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("ML Model Accuracy:", accuracy_score(y_test, pred))
