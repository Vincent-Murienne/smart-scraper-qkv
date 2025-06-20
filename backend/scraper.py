import pandas as pd
from sqlalchemy import create_engine
from models import Base, Arme
import os
from tqdm import tqdm
import requests


# 🔗 URL de l'API
API_URL = "https://tabular-api.data.gouv.fr/api/resources/061194e2-f004-4933-9e44-e7b6f5468e29/data/"

# 🔐 Connexion MySQL via SQLAlchemy
MYSQL_USER = os.getenv("MYSQL_USER", "user")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "user_pass")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB", "my_db")

engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")

def fetch_data():
    print("📡 Récupération des données depuis l'API...")
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()["data"]

def scrape_and_store():

    data = fetch_data()

    # 📦 Créer les tables si elles n'existent pas
    Base.metadata.create_all(engine)

    # 💾 Insertion en base
    with engine.begin() as conn:  # begin() = auto-commit
        for row in tqdm(data, total=len(data), desc="📥 Insertion en base"):
            arme = Arme(
                referenceRGA=row.get('referenceRGA', ''),
                famille=row.get('famille', ''),
                typeArme=row.get('typeArme', ''),
                marque=row.get('marque', ''),
                modele=row.get('modele', ''),
                fabricant=row.get('fabricant', ''),
                paysFabricant=row.get('paysFabricant', ''),
                classementEuropeen=row.get('classementEuropeen', '')
            )
            conn.execute(Arme.__table__.insert().values(
                referenceRGA=arme.referenceRGA,
                famille=arme.famille,
                typeArme=arme.typeArme,
                marque=arme.marque,
                modele=arme.modele,
                fabricant=arme.fabricant,
                paysFabricant=arme.paysFabricant,
                classementEuropeen=arme.classementEuropeen
            ))


    print("✅ Données insérées avec succès.")

if __name__ == "__main__":
    scrape_and_store()