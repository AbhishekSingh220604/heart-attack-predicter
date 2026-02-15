from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("heart_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])[0]

        result = "High Risk of Heart Attack" if prediction == 1 else "Low Risk of Heart Attack"

        return render_template("index.html", prediction_text=result)
    except Exception as e:
        return render_template("index.html", prediction_text="Error in prediction")

if __name__ == "__main__":
    app.run(debug=True)