from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import os
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

app = Flask(__name__)
CORS(app)

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.dirname(BASE_DIR)  # Parent directory (project root)

# Load model and scaler
try:
    with open(os.path.join(MODEL_DIR, 'insurance_model.pkl'), 'rb') as f:
        model = pickle.load(f)
    with open(os.path.join(MODEL_DIR, 'scaler.pkl'), 'rb') as f:
        scaler = pickle.load(f)
except Exception as e:
    print(f'Error loading model: {e}')

@app.route('/')
def home():
    return jsonify({'message': 'Insurance Cost Prediction API', 'status': 'running'})

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features
        age = float(data['age'])
        bmi = float(data['bmi'])
        children = int(data['children'])
        sex = data['sex']
        smoker = data['smoker']
        region = data['region']
        
        # Convert to model format
        sex_male = 1 if sex.lower() == 'male' else 0
        smoker_yes = 1 if smoker.lower() == 'yes' else 0
        
        region_northwest = 1 if region.lower() == 'northwest' else 0
        region_southeast = 1 if region.lower() == 'southeast' else 0
        region_southwest = 1 if region.lower() == 'southwest' else 0
        
        # Create DataFrame
        input_df = pd.DataFrame([[
            age, bmi, children,
            sex_male,
            smoker_yes,
            region_northwest,
            region_southeast,
            region_southwest
        ]], columns=[
            'age', 'bmi', 'children',
            'sex_male',
            'smoker_yes',
            'region_northwest',
            'region_southeast',
            'region_southwest'
        ])
        
        # Scale and predict
        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]
        
        return jsonify({
            'status': 'success',
            'prediction': float(prediction),
            'currency': 'USD'
        })
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
