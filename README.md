# 🏡 House Price Prediction API  

## 📌 Overview  
This project provides a **machine learning-powered API** for predicting house prices using **Flask**. The model is trained using **Linear Regression** and incorporates feature preprocessing techniques such as scaling and encoding.  

---

## 📂 Project Structure  

├── app.py # Flask API for serving predictions ├── prediction.ipynb # Jupyter Notebook for model training & evaluation ├── house_price_model.pkl # Trained Linear Regression model (saved with pickle) ├── scaler.pkl # StandardScaler for feature normalization ├── label_encoder.pkl # Label encoder for categorical data transformation ├── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
2️⃣ Install Dependencies
Ensure you have Python 3.7+ installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, install: flask numpy pandas scikit-learn pickle5)

3️⃣ Run the Flask API
bash
Copy
Edit
python app.py
The API will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
🔍 API Usage
📌 Endpoint: /predict (POST Request)
Request Format (JSON)
json
Copy
Edit
{
  "Location": "New York",
  "Size_sqft": 1500,
  "Bedrooms": 3,
  "Bathrooms": 2,
  "House_Age": 10,
  "Garage": 1,
  "Pool": 0,
  "Distance_to_City_Center_miles": 5
}
Response Format (JSON)
json
Copy
Edit
{
  "predicted_price": [350000.0]
}
📊 Model Performance
The Linear Regression model was chosen based on evaluation metrics:

Metric	Linear Regression
RMSE (Lower is better)	39,797.35
MAE (Lower is better)	31,989.14
R² Score (Closer to 1 is better)	0.99
