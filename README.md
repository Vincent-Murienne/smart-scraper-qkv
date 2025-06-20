# 📊 SmartScraper - QKV

Extraction automatisée de données Open Data avec Flask, React.js, MySQL et Docker.

![image](https://github.com/user-attachments/assets/5fb8fc0d-63f5-442b-b0ad-a444865ab6c4)


## 🎯 Objectif du projet

Ce projet vise à développer une application permettant :

- L’identification et l’utilisation de sources Open Data autorisant le scraping ou l’accès via API.
- L’implémentation d’un module de scraping en Python.
- Le stockage des données dans une base de données relationnelle (MySQL).
- La création d’une API REST sécurisée avec Flask.
- La conception d’une interface utilisateur dynamique avec React.js.
- La conteneurisation et le déploiement complet de l’infrastructure avec Docker.
- La collaboration via GitHub avec gestion de versions, branches et documentation.

---

## 🔐 Légalité et éthique

**Source utilisée** :  
👉 https://www.data.gouv.fr/fr/datasets/referentiel-general-des-armes/reuses_and_dataservices/

**Licence** : Licence Ouverte Etalab  

Le scraping est **légal** car les données sont ouvertes, publiques et couvertes par une licence qui autorise explicitement leur réutilisation automatisée.

---

## ⚙️ Technologies utilisées

- **Frontend** : React.js (Vite)
- **Backend** : Flask (Python)
- **Scraping** : BeautifulSoup, Requests
- **Base de données** : MySQL 8
- **ORM** : SQLAlchemy
- **Interface DB** : phpMyAdmin
- **Conteneurisation** : Docker, docker-compose

---

## 🗂️ Arborescence du projet
    smart-scraper-qkv/
    ├── backend/
    │ ├── api.py
    │ ├── app.py
    │ ├── db.py
    │ ├── models.py
    │ ├── scraper.py
    │ ├── requirements.txt
    │ └── Dockerfile
    ├── frontend/
    │ ├── public/
    │ ├── src/
    │ ├── index.html
    │ ├── package.json
    │ ├── vite.config.ts
    │ └── Dockerfile
    ├── docker-compose.yml
    ├── README.md
    └── .gitignore

## ✅ Fonctionnalités implémentées

### 1. Scraping / collecte automatisée
- Connexion à une API JSON Open Data
- Extraction de plusieurs champs : referenceRGA, famille, typeArme, marque, modele, ...
- Nettoyage et normalisation des données

### 2. Persistance
- Base de données MySQL (via volume Docker)
- ORM SQLAlchemy pour la gestion des modèles

### 3. API REST Flask
- `GET /api/armes` : Liste complète des armes
- `GET /api/data?type=<type>` : Filtrage par type
- `POST /api/scrape` : Déclenchement du scraper
- Headers CORS et gestion d'erreurs

### 4. Interface React
- Récupération dynamique des données via axios
- Affichage sous forme de tableau
- Filtres par type, famille, etc.
- Responsive design

### 5. Dockerisation
- Dockerfile pour le backend Flask
- Dockerfile pour le frontend React
- docker-compose pour lancer tous les services :
  - Backend
  - Frontend
  - MySQL
  - phpMyAdmin

---

## 🐳 Lancement avec Docker

### 1. Cloner le dépôt

```bash
git clone https://github.com/Vincent-Murienne/smart-scraper-qkv.git
cd smart-scraper-qkv
```

### 2. Accès via Docker
```bash
docker-compose up --build -d
```

### 3. Accès aux services
![image](https://github.com/user-attachments/assets/d76e4c98-af31-4936-994b-b864b4a6bee5)

### 4. Accéder à la base de donnée MySQL
Envoyer la data dans la base de donnée qkv_db :
    - Exécuter la réquête POST : localhost:5050/api/scrape

### 5. Maintenant il est possible d'accéder au site web localhost:5173

🧠 Auteurs
Projet réalisé par le groupe QKV (@quentbt, @dasilv-h3, @Vincent-Murienne)
HITEMA - Master 1 Développement Web & Logiciel



