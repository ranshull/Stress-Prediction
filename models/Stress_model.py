import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('D:\pre final Project --001\data\prediction\SaYoPillow.csv')

# Drop the 'sr' (snoring range) column if not already removed
if 'sr' in data.columns:
    data = data.drop(columns=['sr'])

# Split data into features and target
X = data.drop(columns=['sl'])  # Features (excluding stress level)
y = data['sl']  # Target variable (stress level)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, '2_stress_model.joblib')
