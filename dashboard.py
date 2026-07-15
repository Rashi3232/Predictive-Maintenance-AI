import streamlit as st
import joblib

st.title("Predictive Maintenance Dashboard")

# Load the trained model
model = joblib.load("predictive_model.pkl")

# Input sliders
temperature = st.slider("Temperature", 40, 70, 50)
vibration = st.slider("Vibration", 2.0, 6.0, 3.0)
pressure = st.slider("Pressure", 100, 140, 120)
humidity = st.slider("Humidity", 50, 80, 60)

# Predict button
if st.button("Predict"):

    sample = [[temperature, vibration, pressure, humidity]]

    result = model.predict(sample)[0]

    if result == 1:
        st.error("⚠ Equipment Failure Predicted")

        st.write("### Recommendation")
        st.write("- Perform Immediate Inspection")
        st.write("- Check Bearings")
        st.write("- Lubricate Moving Parts")
        st.write("- Replace Faulty Components")

    else:
        st.success("✅ Equipment is Healthy")

        st.write("### Recommendation")
        st.write("- Continue Regular Monitoring")
        st.write("- Perform Routine Maintenance")