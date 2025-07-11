from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from feature_extractor import extract_features

app = Flask(__name__)
CORS(app)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        url = data.get('url')
        features = extract_features(url)

        # Debugging print
        print("Model expects:", model.n_features_in_)
        print("Features sent:", len(features))

        prediction = model.predict([features])[0]
        return jsonify({'result': 'Phishing' if prediction == 1 else 'Legitimate'})
    except Exception as e:
        print("Error:", e)
        return jsonify({'result': 'Error occurred on server'}), 500

if __name__ == '__main__':
    app.run(debug=True)
