from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:user_pass@db:3306/qkv_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
