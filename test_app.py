from fastapi.testclient import TestClient
from main import app

# On crée un client de test qui simule ton API
client = TestClient(app)

def test_home():
    """Vérifie si la page d'accueil répond bien (Code 200)"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de recommandation d'orientation !"}

def test_prediction_medical():
    """Vérifie si un profil scientifique reçoit bien une recommandation médicale"""
    payload = {
        "Maths": 70,
        "History": 50,
        "Science": 95,      # Note très forte en science
        "English": 60,
        "Geograpgy": 40,    # Avec la faute d'orthographe
        "Hindi": 50
    }
    
    response = client.post("/predict", json=payload)
    
    # Vérifications
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    # On s'attend à ce que la médecine soit le premier choix
    assert data["recommendation_1"]["major"] == "Medical Science"

def test_prediction_arts():
    """Vérifie si un profil littéraire reçoit une recommandation adaptée"""
    payload = {
        "Maths": 40,
        "History": 90,      # Note très forte en histoire
        "Science": 30,
        "English": 85,
        "Geograpgy": 80,
        "Hindi": 70
    }
    
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    # On s'attend à History ou Literature
    first_choice = data["recommendation_1"]["major"]
    assert first_choice in ["History & Archaeology", "Literature & Journalism"]