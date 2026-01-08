import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

# 1. Basit bir veri seti oluşturalım (Ev m2 ve Fiyat)
# m2: 50, 60, 70, 80, 90, 100
X = np.array([[50], [60], [70], [80], [90], [100]])
# Fiyat: 500, 600, 700, 800, 900, 1000 (basit bir doğrusal ilişki)
y = np.array([500, 600, 700, 800, 900, 1000])

# 2. Modeli Tanımla ve Eğit
model = LinearRegression()
model.fit(X, y)

test_m2 = np.array([[120]])
tahmin = model.predict(test_m2)
print(f"120 m2 ev için tahmin edilen fiyat: {tahmin[0]}")

# 4. Modeli kaydet (Artifact) 
joblib.dump(model,"model.pkl")
print("Model başarıyla 'model.pkl' olarak kaydedildi.")
