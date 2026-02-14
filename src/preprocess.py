import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def preprocess_data(input_file, output_file):
    # Load the CSV file
    data = pd.read_csv(input_file)

    # Ensure the dataset has 'text' and 'Email Type' columns
    if 'Email Text' not in data.columns or 'Email Type' not in data.columns:
        raise ValueError("Input CSV must have 'Email Text' and 'Email Type' columns.")

    # Vectorize the text using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    data['Email Text'] = data['Email Text'].fillna("")
    X = vectorizer.fit_transform(data['Email Text']).toarray()

    # Extract Email Type
    # Convert labels to binary
    data['Email Type'] = data['Email Type'].map({
        'Safe Email': 0,
        'Phishing Email': 1
    })

    y = data['Email Type'].values

    # Save preprocessed data and vectorizer
    with open(output_file, "wb") as f:
        pickle.dump((X, y, vectorizer), f)

    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data("data/Phishing_Email.csv", "data/preprocessed_data.pkl")


