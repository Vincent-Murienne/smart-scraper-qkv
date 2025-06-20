from flask import Blueprint, request, jsonify
from models import Arme
from db import SessionLocal  

api_bp = Blueprint("api", __name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_bp.route("/armes", methods=["GET"])
def get_armes():
    db = next(get_db())
    query = db.query(Arme)

    # Appliquer les filtres s’ils existent dans les query params
    for field in [
        "famille", "typeArme", "marque", "modele",
        "fabricant", "paysFabricant", "classementEuropeen"
    ]:
        value = request.args.get(field)
        if value:
            query = query.filter(getattr(Arme, field) == value)

    armes = query.all()
    results = [arme.to_dict() for arme in armes]
    return jsonify(results), 200

@api_bp.route("/armes", methods=["POST"])
def create_arme():
    db = next(get_db())
    data = request.get_json()

    required_fields = [
        "famille", "typeArme", "marque", "modele",
        "fabricant", "paysFabricant", "classementEuropeen"
    ]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Champs manquants"}), 400

    arme = Arme(**data)
    db.add(arme)
    db.commit()
    db.refresh(arme)
    return jsonify(arme.to_dict()), 201
