import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import pickle


# 1. Charger les données (Celles générées par le script précédent)
try:
    df = pd.read_csv('student_recommendations_final.csv')
except FileNotFoundError:
    print("❌ Lancez d'abord le script de génération de règles pour créer le fichier CSV !")
    exit()

print("📊 Chargement des données...")

# 2. Préparer les Features (X) et la Target (y)
# X = Les notes (Ce que le modèle voit)
X = df[['Hindi', 'English', 'Science', 'Maths', 'History', 'Geograpgy']]

# y = Le programme recommandé (Ce que le modèle doit prédire)
y = df['Recommended_Progam_1']

# 3. Séparation Train / Test (80% pour apprendre, 20% pour tester)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. LE MACHINE LEARNING : Initialisation et Entraînement
# On utilise un RandomForest (puissant pour la classification multiclasse)
model = RandomForestClassifier(n_estimators=100, random_state=42)

print("🧠 Entraînement du modèle en cours...")
model.fit(X_train, y_train)

# 5. Évaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n✅ Modèle entraîné avec succès !")
print(f"🎯 Précision du modèle (Accuracy) : {accuracy * 100:.2f}%")
print("\n--- Rapport de Classification ---")
print(classification_report(y_test, y_pred))

# 6. Sauvegarde du modèle (Pour l'utiliser dans l'API Docker plus tard)
# On sauvegarde le fichier .pkl (c'est le "cerveau" de l'IA)
with open("recommender_model.pkl", "wb") as f: # Ensure 'wb' is used here
    pickle.dump(model, f)
print("💾 Modèle sauvegardé sous 'recommender_model.pkl'")

# --- TEST RAPIDE ---
print("\n--- Test de prédiction sur un nouvel étudiant ---")
# Un étudiant fort en Maths et Science
new_student = [[50, 60, 95, 98, 40, 45]] # Hindi, Eng, Sci, Math, Hist, Geo
prediction = model.predict(new_student)
print(f"Notes : {new_student}")
print(f"Recommandation de l'IA : {prediction[0]}")