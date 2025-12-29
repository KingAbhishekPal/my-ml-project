import streamlit as st 
import pandas as pd
import joblib 

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

# Title and description
st.title("Fraud Detection Prediction App")
st.markdown("Please enter the transaction details and click on **Predict**")

st.divider()

# Input fields
transaction_type = st.selectbox("Transaction type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrg = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

# Prediction button
if st.button("Predict"):
    # Prepare input data
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount, 
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrg,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest, 
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show prediction result
    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ This transaction can be fraud")
    else:
        st.success("✅ This transaction looks like it is not a fraud")
