from flask import Flask, jsonify
from flask_cors import CORS

from scraper import scrape_and_store
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/scrape", methods=["POST"])
def trigger_scrape():
    try:
        scrape_and_store()
        return jsonify({"message": "Scraping terminé avec succès ✅"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/", methods=["GET"])
def default():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)