from urllib.parse import urlparse
import re

def extract_features(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.netloc
        path = parsed.path

        # Handle malformed or missing components
        if not hostname:
            hostname = ''
        if not path:
            path = ''

        features = []

        # 1. URL length
        features.append(len(url))

        # 2. Hostname length
        features.append(len(hostname))

        # 3. Count of dots in hostname
        features.append(hostname.count('.'))

        # 4. Count of hyphens in hostname
        features.append(hostname.count('-'))

        # 5. Count of @ symbols
        features.append(url.count('@'))

        # 6. Use of IP address
        features.append(1 if re.match(r'\d+\.\d+\.\d+\.\d+', hostname) else 0)

        # 7. Use of HTTPS
        features.append(1 if parsed.scheme == 'https' else 0)

        # 8. Presence of suspicious words
        keywords = ['login', 'signin', 'bank', 'secure', 'account', 'update', 'free']
        features.append(1 if any(keyword in url.lower() for keyword in keywords) else 0)

        # 9. Path length
        features.append(len(path))

        # 10. Subdomain level
        features.append(len(hostname.split('.')) - 2)  # e.g., sub.domain.com → 1

        return features

    except Exception as e:
        # Return a default "invalid" feature vector (e.g., all zeros)
        return [0]*10
