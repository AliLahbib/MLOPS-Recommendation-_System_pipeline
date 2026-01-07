# 1. On part d'une image Python officielle légère (version 3.12)
FROM python:3.12-slim

# 2. On définit le dossier de travail dans le conteneur
WORKDIR /app

# 3. On copie le fichier des dépendances
COPY requirements.txt .

# 4. On installe les librairies
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le reste du code (main.py, le modèle .pkl, etc.) dans le conteneur
COPY . .

# 6. On expose le port 8000 (celui de FastAPI)
EXPOSE 8000

# 7. La commande pour lancer l'application quand le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]