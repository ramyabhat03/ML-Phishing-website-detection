import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('datasets/URL_dataset.csv')
data = data.dropna(subset=['url'])
data = data[data['url'].str.startswith(('http', 'https'))]

# Extract features
from feature_extraction import extract_features
features = data['url'].apply(extract_features)
X = pd.DataFrame(features.tolist(), columns=[
    'url_length', 'hostname_length', 'dot_count', 'hyphen_count', 'at_count',
    'ip_usage', 'https', 'suspicious_keyword', 'path_length', 'subdomain_level'
])
X['label'] = data['type'].map({'legitimate': 0, 'phishing': 1})  # Convert labels to numeric

# Bar Plot - Count of Phishing vs Legitimate URLs
plt.figure(figsize=(6, 4))
sns.countplot(x='label', data=X)
plt.title('Count of Legitimate (0) vs Phishing (1) URLs')
plt.xlabel('Label')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Heatmap - Feature Correlation
plt.figure(figsize=(10, 6))
sns.heatmap(X.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Features')
plt.tight_layout()
plt.show()
