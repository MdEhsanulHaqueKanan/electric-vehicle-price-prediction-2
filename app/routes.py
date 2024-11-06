from flask import render_template, request, jsonify
from app import app
from app.model import predict_price

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    
    # Convert the form data into the correct format for prediction
    features = [
        data['county'],
        data['city'],
        data['zip_code'],
        data['model_year'],
        data['make'],
        data['model'],
        data['ev_type'],
        data['cafv_eligibility'],
        data['legislative_district']
    ]
    
    # Get the prediction result
    price = predict_price(features)
    
    return jsonify({'predicted_price': price})

