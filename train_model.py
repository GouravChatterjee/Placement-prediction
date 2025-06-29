import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("bcrec.csv")
X = df[['Age', 'Gender', 'Stream', 'Internships', 'CGPA', 'Hostel', 'HistoryOfBacklogs']]
y = df['PlacedOrNot']

# Encode categorical columns
X = pd.get_dummies(X, columns=['Gender', 'Stream', 'Hostel', 'HistoryOfBacklogs'], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model and columns
joblib.dump(model, 'model.pkl')
joblib.dump(X.columns.tolist(), 'model_columns.pkl')
print("✅ Model training complete. Files saved!")
