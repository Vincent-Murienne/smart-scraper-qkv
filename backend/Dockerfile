FROM python:3.11-slim

# Créer et définir le dossier de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le backend dans le conteneur
COPY . .

# Exposer le port de Flask
EXPOSE 5050

# Lancer le serveur Flask
CMD ["python", "app.py"]
