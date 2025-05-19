import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from tqdm import tqdm
from feature_extraction import extract_features

# Load dataset
print("Loading dataset...")
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

# Models to evaluate
models = {
    "Random Forest": RandomForestClassifier(),
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "SVM": LinearSVC(max_iter=10000),
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier()
}

best_model = None
best_accuracy = 0
best_model_name = ""

# Train and evaluate each model
print("\nTraining and evaluating models...")
for name, model in models.items():
    print(f"\nModel: {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_model_name = name

# Save best model
joblib.dump(best_model, 'phishing_model.pkl')
print(f"\n Best model ({best_model_name}) saved as phishing_model.pkl with accuracy: {best_accuracy:.4f}")
