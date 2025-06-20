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
MYSQL_HOST = os.getenv("MYSQL_HOST", "db")
MYSQL_DB = os.getenv("MYSQL_DB", "qkv_db")

engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")

def fetch_all_data(max_pages=10):
    print("📡 Récupération des données paginées depuis l'API...")
    all_data = []
    url = API_URL
    page_count = 0

    with tqdm(desc="📄 Téléchargement pages") as pbar:
        while url and page_count < max_pages:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()

            page_data = json_data.get("data", [])
            all_data.extend(page_data)

            # Avancer à la page suivante si elle existe
            url = json_data.get("links", {}).get("next", None)
            page_count += 1
            pbar.update(1)

    print(f"✅ {len(all_data)} éléments récupérés en {page_count} pages.")
    return all_data

def scrape_and_store():
    data = fetch_all_data(max_pages=10)

    # 📦 Créer les tables si elles n'existent pas
    Base.metadata.create_all(engine)

    with engine.begin() as conn:
        for row in tqdm(data, total=len(data), desc="📥 Insertion en base"):
            conn.execute(Arme.__table__.insert().values(
                referenceRGA=row.get('referenceRGA', ''),
                famille=row.get('famille', ''),
                typeArme=row.get('typeArme', ''),
                marque=row.get('marque', ''),
                modele=row.get('modele', ''),
                fabricant=row.get('fabricant', ''),
                paysFabricant=row.get('paysFabricant', ''),
                classementEuropeen=row.get('classementEuropeen', '')
            ))

    print("✅ Données insérées avec succès.")

if __name__ == "__main__":
    scrape_and_store()