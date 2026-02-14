from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("models/phishing_detector.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email']

    # Convert text using TF-IDF
    email_vector = vectorizer.transform([email_text])

    # Prediction
    prediction = model.predict(email_vector)[0]

     # Predict probability
    probability = model.predict_proba(email_vector)[0]
    confidence = np.max(probability) * 100

    if prediction == 1:
        result = "Phishing Email ⚠"
        alert_type = "danger"
    else:
        result = "Legitimate Email ✅"
        alert_type = "success"

    return render_template("index.html",prediction=result,confidence=f"{confidence:.2f}",alert_type=alert_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

