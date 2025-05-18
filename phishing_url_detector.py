import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from tqdm import tqdm
from feature_extraction import extract_features

# Load dataset
data = pd.read_csv('datasets/URL_dataset.csv')
data = data.dropna(subset=['url'])
data = data[data['url'].str.startswith(('http', 'https'))]

# Extract features
tqdm.pandas()
print("Extracting features...")
features = data['url'].progress_apply(extract_features)
X = np.array(features.tolist())
y = np.array(data['type'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluation
print("\n Model Performance:")
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(clf, 'phishing_model.pkl')
print("\n Model saved as phishing_model.pkl")

#  User input for prediction
from urllib.parse import urlparse

def predict_url(url):
    try:
        features = np.array(extract_features(url)).reshape(1, -1)
        model = joblib.load('phishing_model.pkl')
        prediction = model.predict(features)[0]
        print(f"\n🔗 URL: {url}")
        print(" Prediction:", "Phishing" if prediction.lower() == "phishing" else "Legitimate")
    except Exception as e:
        print(" Error analyzing URL:", str(e))

# Prompt user input
user_url = input("\n Enter a URL to check: ").strip()
predict_url(user_url)
