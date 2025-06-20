from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from models import Arme
from app import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schéma Pydantic pour la validation des données en entrée (POST)
class ArmeCreate(BaseModel):
    famille: str
    typeArme: str
    marque: str
    modele: str
    fabricant: str
    paysFabricant: str
    classementEuropeen: str

# Schéma Pydantic pour la réponse (GET)
class ArmeResponse(ArmeCreate):
    referenceRGA: int

    class Config:
        orm_mode = True

# Route GET avec filtres facultatifs
@router.get("/armes", response_model=List[ArmeResponse])
def get_armes(
    famille: Optional[str] = Query(None),
    typeArme: Optional[str] = Query(None),
    marque: Optional[str] = Query(None),
    modele: Optional[str] = Query(None),
    fabricant: Optional[str] = Query(None),
    paysFabricant: Optional[str] = Query(None),
    classementEuropeen: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Arme)
    if famille:
        query = query.filter(Arme.famille == famille)
    if typeArme:
        query = query.filter(Arme.typeArme == typeArme)
    if marque:
        query = query.filter(Arme.marque == marque)
    if modele:
        query = query.filter(Arme.modele == modele)
    if fabricant:
        query = query.filter(Arme.fabricant == fabricant)
    if paysFabricant:
        query = query.filter(Arme.paysFabricant == paysFabricant)
    if classementEuropeen:
        query = query.filter(Arme.classementEuropeen == classementEuropeen)
    return query.all()

# Route POST pour ajouter une arme
@router.post("/armes", response_model=ArmeResponse)
def create_arme(arme: ArmeCreate, db: Session = Depends(get_db)):
    arme_obj = Arme(**arme.dict())
    db.add(arme_obj)
    db.commit()
    db.refresh(arme_obj)
    return arme_obj
