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
        features.append(len(url))  # 1. URL length
        features.append(len(hostname))  # 2. Hostname length
        features.append(hostname.count('.'))  # 3. Count of dots
        features.append(hostname.count('-'))  # 4. Count of hyphens
        features.append(url.count('@'))  # 5. Count of '@'
        features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', hostname) else 0)  # 6. IP usage
        features.append(1 if parsed.scheme == 'https' else 0)  # 7. HTTPS
        keywords = ['login', 'signin', 'bank', 'secure', 'account', 'update', 'free']
        features.append(1 if any(k in url.lower() for k in keywords) else 0)  # 8. Suspicious keywords
        features.append(len(path))  # 9. Path length
        features.append(len(hostname.split('.')) - 2)  # 10. Subdomain level

        return features
    except Exception:
        return [0] * 10
