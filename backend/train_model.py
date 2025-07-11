import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Simulated dataset with 13 features
data = {
    'url_length': [60, 20, 120],
    'has_https': [1, 1, 0],
    'has_ip': [0, 0, 1],
    'has_at_symbol': [0, 0, 1],
    'num_dots': [2, 1, 5],
    'has_login': [1, 0, 1],
    'has_secure': [1, 0, 1],
    'has_update': [0, 0, 1],
    'has_verify': [0, 0, 1],
    'has_bank': [0, 0, 0],
    'has_account': [0, 0, 1],
    'has_paypal': [1, 0, 1],
    'has_password': [0, 0, 1],
    'label': [1, 0, 1]
}

df = pd.DataFrame(data)
X = df.drop('label', axis=1)
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained with 13 features and saved as model.pkl")
