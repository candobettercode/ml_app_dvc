from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestRegressor

import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load models
label_encoders = joblib.load('src/models/label_encoders.pkl')
scaler = joblib.load('src/models/scaler.pkl')
model = joblib.load('src/models/RFRegressor_best.pkl')

# Input columns expected
categorical_cols = ['sex', 'smoker', 'day', 'time']
numeric_cols = ['total_bill', 'size']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    total_bill = float(request.form['total_bill'])
    gender = request.form['gender']
    smoker = request.form['smoker']
    day = request.form['day']
    time = request.form['time']
    size = int(request.form['size'])

    # Create DataFrame for consistency
    data = pd.DataFrame({
        'total_bill': [total_bill],
        'sex': [gender],
        'smoker': [smoker],
        'day': [day],
        'time': [time],
        'size': [size]
    })

    # Apply Label Encoding
    for col in categorical_cols:
        le = label_encoders[col]
        data[col] = le.transform(data[col])

    # Scale the data
    X_scaled = scaler.transform(data)

    # Predict
    prediction = model.predict(X_scaled)[0]

    return f'<h2>Predicted Loan Status (Tip Amount or Similar): {prediction:.2f}</h2>'


if __name__ == '__main__':
    app.run(debug=True)
