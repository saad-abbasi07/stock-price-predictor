from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = load_model("stock_lstm.keras")

# Example: scaler (fit on your training data)
scaler = MinMaxScaler()
# You should fit this on the same data used during training or save/load it.

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]  # expects last 60 prices
    data = np.array(data).reshape(1, 60, 1)
    scaled_pred = model.predict(data)
    pred_price = scaler.inverse_transform(scaled_pred)
    return jsonify({"predicted_price": float(pred_price[0,0])})

if __name__ == "__main__":
    app.run(debug=True)
