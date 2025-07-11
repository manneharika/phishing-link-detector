def extract_features(url):
    features = []

    # Basic features
    features.append(len(url))                              # url_length
    features.append(1 if url.startswith("https") else 0)   # has_https
    features.append(1 if any(part.isdigit() for part in url.split('/')[2].split('.')) else 0)  # has_ip
    features.append(1 if '@' in url else 0)                # has_at_symbol
    features.append(url.count('.'))                        # num_dots

    # Keyword-based features
    phishing_keywords = ['login', 'secure', 'update', 'verify', 'bank', 'account', 'paypal', 'password']
    keyword_flags = [1 if keyword in url.lower() else 0 for keyword in phishing_keywords]
    features.extend(keyword_flags)

    return features
