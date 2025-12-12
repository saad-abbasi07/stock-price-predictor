import os
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return "Stock Price Predictor is running!"
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sample_prediction = {"predicted_price": 100.0}
    return jsonify(sample_prediction)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
