from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Stock Price Predictor API running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    ticker = data.get("ticker")

    if not ticker:
        return jsonify({"error": "Ticker required"}), 400

    prediction = round(100 + len(ticker) * 5, 2)

    return jsonify({
        "ticker": ticker.upper(),
        "predicted_price": prediction
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
