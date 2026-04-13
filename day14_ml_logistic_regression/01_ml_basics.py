"""Day 14, Lessons 1-3: Machine Learning & Logistic Regression"""
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

print("=== ML Fundamentals ===\n")

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

print(f"Dataset shape: {X.shape}")
print(f"Number of features: {X.shape[1]}")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of classes: {len(np.unique(y))}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")

print("\n=== Logistic Regression ===\n")

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
lr_model = LogisticRegression(max_iter=200)
lr_model.fit(X_train_scaled, y_train)

# Predict
y_pred_train = lr_model.predict(X_train_scaled)
y_pred_test = lr_model.predict(X_test_scaled)

print("Training Results:")
print(f"  Accuracy: {accuracy_score(y_train, y_pred_train):.4f}")

print("\nTest Results:")
print(f"  Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
print(f"  Precision (weighted): {precision_score(y_test, y_pred_test, average='weighted'):.4f}")
print(f"  Recall (weighted): {recall_score(y_test, y_pred_test, average='weighted'):.4f}")
print(f"  F1 Score (weighted): {f1_score(y_test, y_pred_test, average='weighted'):.4f}")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred_test)
print(cm)

print("\n=== Model Interpretation ===\n")

# Feature importance (coefficients)
feature_names = iris.feature_names
print("Feature importance (coefficients for class 0):")
for feature, coef in zip(feature_names, lr_model.coef_[0]):
    print(f"  {feature}: {coef:.4f}")

# Predictions on new data
new_sample = scaler.transform([[5.1, 3.5, 1.4, 0.2]])
prediction = lr_model.predict(new_sample)[0]
probabilities = lr_model.predict_proba(new_sample)[0]

class_names = iris.target_names
print(f"\nNew sample prediction: {class_names[prediction]}")
print(f"Probabilities: {dict(zip(class_names, probabilities.round(4)))}")

print("\n✅ Day 14 lessons complete!")
