from fastapi import FastAPI
import joblib
import numpy as np

# 1. API nesnesini oluştur
app = FastAPI()

# 2. Eğittiğimiz modeli yükle
model = joblib.load("model.pkl")

@app.get("/")
def home():
   return {"mesaj": "Ev Fiyat Tahmin API'sine Hosgeldiniz"}

@app.get("/tahmin")
def tahmin_et(m2: float):
   # gelen m2 bilgisini modele uygun hale getir
   veri = np.array([[m2]])
   sonuc = model.predict(veri)
   return {"metrekare": m2, "tahmin_edilen_fiyat": float(sonuc[0])}
