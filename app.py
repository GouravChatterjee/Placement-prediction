import streamlit as st
import pandas as pd
import joblib

# Load model and column names
model = joblib.load('model.pkl')
columns = joblib.load('model_columns.pkl')

# Page config
st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="centered")

# Custom CSS for UI styling
st.markdown("""
    <style>
        body {
            background-image: url('https://img.freepik.com/free-vector/young-people-workplace_52683-28608.jpg'); 
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0);
        }
        .custom-card {
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            max-width: 420px;
            margin: auto;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            color: #1e1e1e;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h5, label, p {
            color: #1e1e1e !important;
            text-align: center;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 6px;
            padding: 10px 16px;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #388e3c;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Welcome to Placement Prediction App</h1>", unsafe_allow_html=True)

# Card container
st.markdown("<div class='custom-card'>", unsafe_allow_html=True)

# Form inputs
stream = st.selectbox("📘 Select Stream", [
    "Electronics And Communication", "Computer Science", "Information Technology",
    "Mechanical", "Electrical", "Civil"
])
cgpa = st.number_input("📊 Enter CGPA", 0.0, 10.0, 7.0, step=0.1)
internships = st.number_input("💼 Previous Internships", 0, 10, 0)
backlogs = st.selectbox("📄 History of Backlogs", ["Yes", "No"])
gender = st.selectbox("👤 Gender", ["Male", "Female"])

# Input data prep
input_df = pd.DataFrame({
    'Age': [21],  # Default value
    'Internships': [internships],
    'CGPA': [cgpa],
    'Gender': [gender],
    'Stream': [stream],
    'Hostel': ['No'],
    'HistoryOfBacklogs': [backlogs]
})
input_encoded = pd.get_dummies(input_df)
input_encoded = input_encoded.reindex(columns=columns, fill_value=0)

# Submit Button
if st.button("Submit"):
    prediction = model.predict(input_encoded)[0]
    reason = None

    # Business Rule Overrides
    if internships == 0:
        prediction = 0
        reason = "no internship experience"
    elif backlogs == "Yes":
        prediction = 0
        reason = "history of backlogs"
    elif cgpa < 6.0:
        prediction = 0
        reason = "CGPA less than 6.0"

    # Show result
    if prediction == 1:
        st.success("🎉 Congratulations! You are likely to be Placed.")
        st.balloons()
    else:
        if reason:
            st.error(f"❌ Sorry! You might not get Placed due to **{reason}**.")
        else:
            st.error("😥 Sorry! You might not get Placed. Keep learning and improving!")

# Close card
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='color: yellow; text-align: center;'>Empowering engineering students with predictive tools for better placement readiness.</p>", unsafe_allow_html=True)
