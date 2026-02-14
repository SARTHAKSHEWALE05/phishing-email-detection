import pickle

def predict_email(model_file, vectorizer_file, email_text):
    # Load the model
    with open(model_file, "rb") as f:
        model = pickle.load(f)

    # Load the vectorizer
    with open(vectorizer_file, "rb") as f:
        vectorizer = pickle.load(f)

    # Vectorize the input email
    email_vector = vectorizer.transform([email_text]).toarray()

    # Make a prediction
    prediction = model.predict(email_vector)
    return "Phishing Email" if prediction[0] == 1 else "Safe Email"

if __name__ == "__main__":
    email_text = " Looks and sounds a hell of a lot like Clare's cat, Violence...A tall tail or is it a prowling panther?"
    # email_text = "Your account has been suspended. Click here to reset password."

    # result = predict_email("models/phishing_detector.pkl", "data/preprocessed_data.pkl", email_text)

    result = predict_email("models/phishing_detector.pkl","models/vectorizer.pkl",email_text)
    print(f"Prediction: {result}")
