# 🎓 Placement Prediction App

A machine learning–powered web application that helps engineering students predict their chances of campus placement based on academic performance and other key factors.

👉 **Live App**: [https://bcrec-placement-prediction.streamlit.app/](https://bcrec-placement-prediction.streamlit.app/)

---

## 📌 Features

- 📊 Predicts placement chances using a trained ML model
- ✅ Rule-based filters: ensures realistic outcomes (e.g., CGPA, internships, backlogs)
- 🎨 Clean and responsive UI built with **Streamlit**
- 📁 One-click deployment via Streamlit Cloud

---

## 🧠 How It Works

The app takes the following input from users:

- 📘 Stream (Branch of Engineering)
- 📊 CGPA
- 💼 Internship count
- 📄 History of backlogs
- 👤 Gender

The app then:
- One-hot encodes the data
- Applies logical rules:
  - No internship → Not placed
  - CGPA < 6.0 → Not placed
  - Backlogs → Not placed
- Predicts placement using a **RandomForestClassifier** trained on real-world-like data

---

## ⚙️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

---

✨ Author
Gourav Kumar Chatterjee
B.Tech (IT)
LinkedIn:-https://www.linkedin.com/in/gourav-chatterjee-7a1484260/

