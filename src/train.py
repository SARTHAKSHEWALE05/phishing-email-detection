import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_model(data_file, model_file):

    # Create models folder if not exists
    os.makedirs("models", exist_ok=True)

    # Load preprocessed data
    with open(data_file, "rb") as f:
        X, y, vectorizer = pickle.load(f)
        # X, y, _ = pickle.load(f)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # # Save the trained model
    # with open(model_file, "wb") as f:
    #     pickle.dump(model, f)
    
    # Save model
    with open("models/phishing_detector.pkl", "wb") as f:
        pickle.dump(model, f)

    # Save vectorizer
    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    print("Model and vectorizer saved inside models folder.")

if __name__ == "__main__":
    train_model("data/preprocessed_data.pkl", "models/phishing_detector.pkl")