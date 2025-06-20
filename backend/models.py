from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Arme(Base):
    __tablename__ = "armes"

    referenceRGA = Column(Integer, primary_key=True, autoincrement=True)
    famille = Column(String(100))
    typeArme = Column(String(100))
    marque = Column(String(100))
    modele = Column(String(100))
    fabricant = Column(String(100))
    paysFabricant = Column(String(100))
    classementEuropeen = Column(String(100))

    def to_dict(self):
        return {
            "referenceRGA": self.referenceRGA,
            "famille": self.famille,
            "typeArme": self.typeArme,
            "marque": self.marque,
            "modele": self.modele,
            "fabricant": self.fabricant,
            "paysFabricant": self.paysFabricant,
            "classementEuropeen": self.classementEuropeen,
        }
