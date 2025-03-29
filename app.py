from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model, scaler, and label encoder using pickle
with open("house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route('/')
def home():
    return "Linear Regression Model API"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get request data
        data = request.get_json()

        # Define required features
        required_features = ["Location", "Size_sqft", "Bedrooms", "Bathrooms", 
                             "House_Age", "Garage", "Pool", "Distance_to_City_Center_miles"]

        # Check for missing values
        if not all(feature in data for feature in required_features):
            return jsonify({'error': 'Missing required features'}), 400

        # Encode categorical feature (Location)
        location = data["Location"]

        # Ensure the location exists in the trained encoder
        if location not in label_encoder.classes_:
            return jsonify({'error': f"Unknown location: {location}. Available: {list(label_encoder.classes_)}"}), 400

        location_encoded = label_encoder.transform([location])[0]  # Convert to number

        # Prepare numerical features
        numerical_features = np.array([
            data["Size_sqft"], data["Bedrooms"], data["Bathrooms"], 
            data["House_Age"], data["Garage"], data["Pool"], 
            data["Distance_to_City_Center_miles"]
        ]).reshape(1, -1)

        # Combine location encoding with numerical features
        features = np.append(location_encoded, numerical_features ).reshape(1, -1)

        # Normalize features using the saved scaler
        features_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(features_scaled)
        print(features_scaled)

        # Return the predicted price
        return jsonify({'predicted_price': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)