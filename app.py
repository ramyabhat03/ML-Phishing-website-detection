import streamlit as st
import numpy as np
import joblib
from urllib.parse import urlparse
import re

# Feature extraction function
def extract_features(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.netloc
        path = parsed.path

        if not hostname:
            hostname = ''
        if not path:
            path = ''

        features = []
        features.append(len(url))  # 1. URL length
        features.append(len(hostname))  # 2. Hostname length
        features.append(hostname.count('.'))  # 3. Count of dots in hostname
        features.append(hostname.count('-'))  # 4. Count of hyphens in hostname
        features.append(url.count('@'))  # 5. Count of @ symbols
        features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', hostname) else 0)  # 6. IP address
        features.append(1 if parsed.scheme == 'https' else 0)  # 7. HTTPS
        keywords = ['login', 'signin', 'bank', 'secure', 'account', 'update', 'free']
        features.append(1 if any(keyword in url.lower() for keyword in keywords) else 0)  # 8. Suspicious words
        features.append(len(path))  # 9. Path length
        features.append(len(hostname.split('.')) - 2)  # 10. Subdomain level

        return features
    except Exception:
        return [0]*10

# Load model once
@st.cache_resource
def load_model():
    return joblib.load('phishing_model.pkl')

model = load_model()

# Streamlit app UI
st.title(" Phishing URL Detection")
st.write("Enter a URL below to check if it is phishing or legitimate.")

url_input = st.text_input("Enter URL", "")

if st.button("Check URL"):
    if url_input.strip() == "":
        st.warning("Please enter a valid URL.")
    else:
        features = np.array(extract_features(url_input)).reshape(1, -1)
        prediction = model.predict(features)[0]
        if prediction.lower() == 'phishing':
            st.error(" The URL is predicted to be **Phishing**.")
        else:
            st.success(" The URL is predicted to be **Legitimate**.")

        # Optionally show extracted features
        with st.expander("Show extracted features"):
            feature_names = [
                "URL length",
                "Hostname length",
                "Dots in hostname",
                "Hyphens in hostname",
                "Count of '@'",
                "IP address usage (1 or 0)",
                "HTTPS usage (1 or 0)",
                "Suspicious keywords presence (1 or 0)",
                "Path length",
                "Subdomain level"
            ]
            features_list = features.flatten().tolist()
            feature_dict = {name: value for name, value in zip(feature_names, features_list)}
            st.json(feature_dict)
