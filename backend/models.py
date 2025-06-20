from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Arme(Base):
    __tablename__ = 'armes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    referenceRGA = Column(String(100))
    famille = Column(String(100))
    typeArme = Column(String(100))
    marque = Column(String(100))
    modele = Column(String(100))
    fabricant = Column(String(100))
    paysFabricant = Column(String(100))
    classementEuropeen = Column(String(100))