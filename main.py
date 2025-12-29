import pickle
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Recommendation System")

# --- 1. Chargement du modèle ---
try:
    with open("recommender_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("✅ Modèle chargé.")
    
    # Récupération de l'ordre des colonnes (si disponible)
    if hasattr(model, "feature_names_in_"):
        expected_columns = list(model.feature_names_in_)
        print(f"📋 Ordre attendu : {expected_columns}")
    else:
        expected_columns = None 

except FileNotFoundError:
    print("❌ Erreur : Fichier modèle introuvable.")
    model = None
    expected_columns = None

# --- 2. Définition des données ---
class StudentGrades(BaseModel):
    Maths: float
    History: float
    Science: float
    English: float
    Geograpgy: float  # Faute d'orthographe conservée volontairement
    Hindi: float

# --- 3. Route Accueil (Celle qui manquait !) ---
@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de recommandation d'orientation !"}

# --- 4. Route Prédiction ---
@app.post("/predict")
def predict_orientation(grades: StudentGrades):
    if not model:
        return {"error": "Modèle non chargé."}

    # Correction Warning Pydantic : on utilise model_dump() au lieu de dict()
    input_data = pd.DataFrame([grades.model_dump()])

    # Réorganisation des colonnes
    if expected_columns:
        missing_cols = set(expected_columns) - set(input_data.columns)
        if missing_cols:
            return {"error": f"Colonnes manquantes : {missing_cols}"}
        input_data = input_data[expected_columns]

    try:
        probs = model.predict_proba(input_data)[0]
        class_labels = model.classes_
        results = list(zip(class_labels, probs))
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

        return {
            "status": "success",
            "recommendation_1": {
                "major": sorted_results[0][0],
                "confidence": f"{sorted_results[0][1] * 100:.2f}%"
            },
            "recommendation_2": {
                "major": sorted_results[1][0],
                "confidence": f"{sorted_results[1][1] * 100:.2f}%"
            }
        }

    except Exception as e:
        return {"error": f"Erreur interne : {str(e)}"}