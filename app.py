from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Stock Price Predictor API running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    ticker = data.get("ticker", "").upper().strip()  # normalize input

    if not ticker:
        return jsonify({"error": "Ticker required"}), 400

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="30d")  # last 30 days

        if hist.empty:
            return jsonify({"error": f"No data found for ticker '{ticker}'"}), 404

        last_close = hist['Close'][-1]
        predicted_price = round(last_close * 1.01, 2)  # example: 1% increase

        return jsonify({
            "ticker": ticker,
            "last_close": round(last_close, 2),
            "predicted_price": predicted_price
        })

    except Exception as e:
        print(f"Error fetching prediction for {ticker}: {e}")
        return jsonify({"error": f"Error fetching prediction for '{ticker}'"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
