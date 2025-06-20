# backend/app.py
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from api import router

app = FastAPI()

# DATABASE_URL = "mysql+pymysql://root:@db:3306/qkv_db"
DATABASE_URL = "mysql+pymysql://user:user_pass@db:3306/my_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Créer les tables (attention à ne pas faire ça en production)
Base.metadata.create_all(bind=engine)

app.include_router(router)
