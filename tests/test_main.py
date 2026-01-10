from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_predict_endpoint():
    # API'ye 100m2 için istek at
    response = client.get("/tahmin?m2=100")
    assert response.status_code == 200
    assert "tahmin_edilen_fiyat" in response.json()
