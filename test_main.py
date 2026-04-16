from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend is running"}

def test_chat_without_pdf():
    response = client.post("/chat", json={"question": "Hello"})
    assert response.status_code == 200
    assert "Text-based querying" in response.json()["answer"]

def test_summary_without_pdf():
    response = client.post("/summary")
    assert response.status_code == 200
    assert "Summary is available" in response.json()["summary"]