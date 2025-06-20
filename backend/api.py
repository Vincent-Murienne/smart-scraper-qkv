from flask import Blueprint, request, jsonify
from models import Arme
from db import SessionLocal
from sqlalchemy import or_

api_bp = Blueprint("api", __name__)

@api_bp.route("/armes", methods=["GET"])
def get_armes():
    session = SessionLocal()

    search = request.args.get("search", "", type=str).lower()
    famille = request.args.get("famille", "", type=str).lower()
    type_arme = request.args.get("typeArme", "", type=str).lower()
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 10, type=int)

    query = session.query(Arme)

    if search:
        search_like = f"%{search}%"
        query = query.filter(
            or_(
                Arme.referenceRGA.ilike(search_like),
                Arme.famille.ilike(search_like),
                Arme.typeArme.ilike(search_like),
                Arme.marque.ilike(search_like),
                Arme.modele.ilike(search_like),
                Arme.fabricant.ilike(search_like),
                Arme.paysFabricant.ilike(search_like),
                Arme.classementEuropeen.ilike(search_like)
            )
        )

    if famille:
        query = query.filter(Arme.famille.ilike(f"%{famille}%"))

    if type_arme:
        query = query.filter(Arme.typeArme.ilike(f"%{type_arme}%"))

    total = query.count()
    results = query.offset((page - 1) * limit).limit(limit).all()


    armes_list = [arme.to_dict() for arme in results]
    session.close()

    return jsonify({
        "total": total,
        "page": page,
        "limit": limit,
        "data": armes_list
    })