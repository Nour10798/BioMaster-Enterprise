from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "ONLINE" in response.json()["status"]

def test_predict_normal_protein():
    response = client.post("/predict_location", json={"length": 350, "weight": 45000})
    assert response.status_code == 200
    assert "Predicted_Location" in response.json()
    assert response.json()["Status"] == " Quality Passed"

def test_predict_anomaly_protein():
    
    response = client.post("/predict_location", json={"length": 86, "weight": 96391})
    assert response.status_code == 200
    assert "Error" in response.json()
