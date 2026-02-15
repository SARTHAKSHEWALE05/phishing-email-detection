
📧 Phishing Email Detection using Machine Learning
🔍 Project Overview

This project detects phishing emails using Machine Learning and Natural Language Processing (TF-IDF).

The system classifies emails into:

✅ Legitimate Email

⚠ Phishing Email

It also displays a confidence score (%) for each prediction.

The project is deployed as a Flask web application with Bootstrap UI.

🚀 Live Demo

👉 (Add your Render link here after deployment)
Example:

https://phishing-email-detector.onrender.com

🛠 Tech Stack

Python

Scikit-learn

Pandas

NumPy

Flask

Bootstrap 5

Gunicorn (for deployment)

🧠 How It Works
1️⃣ Text Preprocessing

Cleans email text

Converts text into numerical vectors using TF-IDF Vectorization

2️⃣ Model Training

Uses Random Forest Classifier

Splits dataset into training and testing sets

Evaluates using Accuracy Score

3️⃣ Prediction

Takes user input email

Transforms text using saved TF-IDF vectorizer

Predicts:

Phishing ⚠

Legitimate ✅

Displays confidence probability

📊 Model Performance

Algorithm: Random Forest Classifier

Feature Extraction: TF-IDF

Evaluation Metric: Accuracy Score

(You can add your actual accuracy value here)

Example:

Model Accuracy: 0.94

📂 Project Structure
phishing-email-detection/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── Phishing_Email.csv
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│
├── templates/
│   └── index.html

⚙ Installation & Setup Guide
1️⃣ Clone the Repository
git clone https://github.com/SARTHAKSHEWALE05/phishing-email-detection.git
cd phishing-email-detection

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Preprocess Dataset
python src/preprocess.py

5️⃣ Train the Model
python src/train.py

6️⃣ Run the Web Application
python app.py


Open in browser:

http://127.0.0.1:5000

🌐 Deployment

This application can be deployed on:

Render

Railway

PythonAnywhere

Deployment uses:

gunicorn app:app

✨ Features

Email Classification (Phishing / Legitimate)

Confidence Score Display

Clean Bootstrap UI

Modular Code Structure

Deployment Ready

📌 Important Note

Large model files (.pkl) are not included in the repository due to GitHub size limits.

Please run:

python src/preprocess.py
python src/train.py


before starting the application.

👨‍💻 Author

Sarthak Shewale
Third-Year Computer Engineering Student
Amrutvahini College Of Engineering Sangamner
