# Insurance Cost Prediction - Vercel Deployment Setup

This project is now configured for deployment on Vercel!

## Project Structure

- pi/index.py - Flask API backend (handles predictions)
- public/index.html - Web interface frontend
- insurance_model.pkl - Trained ML model
- scaler.pkl - Feature scaler
- ercel.json - Vercel configuration
- equirements.txt - Python dependencies
- .python-version - Python version specification

## Deployment Steps

### 1. Prerequisites
- Vercel Account (sign up at https://vercel.com)
- Vercel CLI (optional but recommended)

### 2. Quick Deploy via GitHub
1. Push your code to GitHub (already done!)
2. Go to https://vercel.com/new
3. Import your GitHub repository
4. Vercel will auto-detect the configuration
5. Click "Deploy"

### 3. Deploy via Vercel CLI (Advanced)
`ash
npm i -g vercel
vercel login
vercel --prod
`

### 4. Environment Setup
No special environment variables needed for basic deployment.

## File Descriptions

- **api/index.py**: Flask API that loads ML models and handles POST requests for predictions
- **public/index.html**: Interactive web form for users to input insurance details
- **vercel.json**: Configuration telling Vercel how to build and route requests

## API Endpoint

After deployment, you'll have an endpoint:
`
POST https://your-domain.vercel.app/api/predict
`

Request body:
`json
{
  "age": 25,
  "bmi": 22.0,
  "children": 0,
  "sex": "Male",
  "smoker": "No",
  "region": "northwest"
}
`

## Testing Locally (Optional)

`ash
# Install dependencies
pip install -r requirements.txt

# Run locally
python -m flask --app api/index.py run
`

Then visit http://localhost:5000

## Troubleshooting

- **Models not loading**: Ensure insurance_model.pkl and scaler.pkl are in the root directory
- **CORS errors**: Already configured in Flask with flask-cors
- **Python version issues**: Using Python 3.9 as specified in .python-version

## Support

Check Vercel docs: https://vercel.com/docs

Good luck with your deployment! 🚀
