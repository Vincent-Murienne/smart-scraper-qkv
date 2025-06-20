from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:my_root_password@db:3306/qkv_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
