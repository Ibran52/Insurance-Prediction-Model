import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# 🎯 Load model & scaler (FIXED)
model = pickle.load(open("insurance_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.set_page_config(page_title="Insurance Cost Predictor", layout="centered")

st.title("💰 Insurance Cost Prediction App")
st.write("Enter your details to estimate insurance cost")

# 🔹 User Inputs
age = st.slider("Age", 18, 100, 25)
bmi = st.slider("BMI", 10.0, 50.0, 22.0)
children = int(st.slider("Number of Children", 0, 5, 0))

sex = st.selectbox("Gender", ["Male", "Female"])
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

# 🔹 Convert Inputs to Model Format
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# ⚠️ Must match training columns
input_data = pd.DataFrame([[
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

# 🔹 Scale Input
input_scaled = scaler.transform(input_data.values)

# 🔹 Prediction Button
if st.button("Predict Insurance Cost"):
    try:
        prediction = model.predict(input_scaled)

        st.success(f"💰 Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")

        # Extra Insight
        if smoker == "Yes":
            st.warning("⚠️ Smoking increases insurance cost significantly!")

    except Exception as e:
        st.error(f"Error: {e}")