import pandas as pd
import mlflow
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv('data.csv')
X = df[['metrekare']].values
y = df['fiyat'].values

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X, y)
    
    # Metrikleri kaydet
    score = model.score(X, y)
    mlflow.log_metric("r2_score", score)
    
    # Modeli kaydet
    joblib.dump(model, "model.pkl")
    print(f"Model eğitildi, skor: {score}")
