# feature_extraction.py
from urllib.parse import urlparse
import re

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
        features.append(len(url)) 
        features.append(len(hostname)) 
        features.append(hostname.count('.')) 
        features.append(hostname.count('-')) 
        features.append(url.count('@')) 
        features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', hostname) else 0)  
        features.append(1 if parsed.scheme == 'https' else 0)  
        keywords = ['login', 'signin', 'bank', 'secure', 'account', 'update', 'free']
        features.append(1 if any(k in url.lower() for k in keywords) else 0)  
        features.append(len(path)) 
        features.append(len(hostname.split('.')) - 2) 

        return features
    except Exception:
        return [0] * 10
