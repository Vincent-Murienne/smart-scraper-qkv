from flask import Flask
from flask_cors import CORS

from models import Base
from db import engine
from api import api_bp

app = Flask(__name__)
CORS(app)

# Créer les tables
Base.metadata.create_all(bind=engine)

# Enregistrer les routes
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
