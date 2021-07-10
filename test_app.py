from fastapi.testclient import TestClient
from main import app
from datetime import datetime
# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong", "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica", "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
#Task2 Writing test cases
def test_alpha():
    with TestClient(app) as client:
        response = client.get("/alpha")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"alpha": "This is Shashank" , "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}

def test_beta():
    with TestClient(app) as client:
        response = client.get("/beta")
        # asserting the correct response is received
        
        assert response.status_code == 200
        assert response.json() == {"beta": "The Beta Group Rocks" , "timestamp": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}