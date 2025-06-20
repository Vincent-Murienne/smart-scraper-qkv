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
    try:
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
    except Exception as e:
        print(f"Erreur dans GET /armes : {e}")
        return jsonify({"error": str(e)}), 500
