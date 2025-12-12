from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os

app = Flask(__name__)

model_path = os.getenv("MODEL_PATH", "stock_lstm.keras")
model = load_model(model_path)

scaler = MinMaxScaler()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]
    data = np.array(data).reshape(1, 60, 1)
    scaled_pred = model.predict(data)
    pred_price = scaler.inverse_transform(scaled_pred)
    return jsonify({"predicted_price": float(pred_price[0,0])})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
