#!/usr/bin/env python3
"""Day 14, Lesson 2: Logistic Regression - Binary & Multi-class Classification

Master logistic regression:
- Binary classification (yes/no)
- Multi-class classification
- Probability predictions
- Decision boundaries
- Feature importance
"""

from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import numpy as np
import matplotlib.pyplot as plt

print("=== Logistic Regression: Classification ===\n")

# 1. BINARY CLASSIFICATION (Breast Cancer Detection)
print("1. Binary Classification - Medical Diagnosis:")
print("   Predicting: Benign or Malignant cancer?\n")

# Load data
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features")
print(f"Classes: {np.unique(y)} (0=Benign, 1=Malignant)")
print(f"Class distribution: {np.bincount(y)}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features (important for logistic regression!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train binary classifier
logreg_binary = LogisticRegression(max_iter=1000, random_state=42)
logreg_binary.fit(X_train_scaled, y_train)

# Predictions
y_pred_train = logreg_binary.predict(X_train_scaled)
y_pred_test = logreg_binary.predict(X_test_scaled)
y_proba_test = logreg_binary.predict_proba(X_test_scaled)[:, 1]

print("\n2. Binary Classification Results:")
print(f"Training Accuracy: {accuracy_score(y_train, y_pred_train):.4f}")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
print(f"Precision: {precision_score(y_test, y_pred_test):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_test):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred_test):.4f}")
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba_test):.4f}")

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred_test)
print(cm)
print(f"True Negatives: {cm[0,0]}, False Positives: {cm[0,1]}")
print(f"False Negatives: {cm[1,0]}, True Positives: {cm[1,1]}")

# Feature importance (coefficients)
print("\n3. Feature Importance (Top 5):")
feature_importance = list(zip(cancer.feature_names, logreg_binary.coef_[0]))
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)

for i, (feature, coef) in enumerate(feature_importance[:5], 1):
    direction = "↑ increases risk" if coef > 0 else "↓ decreases risk"
    print(f"{i}. {feature}: {abs(coef):.4f} {direction}")

# Probability output
print("\n4. Probability Predictions (first 5 test samples):")
print("Sample | Prob (Benign) | Prob (Malignant) | Prediction")
print("-------|---------------|------------------|------------")
for i in range(5):
    prob_benign = 1 - y_proba_test[i]
    prob_malignant = y_proba_test[i]
    pred = "Benign" if y_pred_test[i] == 0 else "Malignant"
    print(f"{i+1:6} | {prob_benign:13.4f} | {prob_malignant:16.4f} | {pred}")

# Decision threshold experimentation
print("\n5. Decision Threshold Impact:")
print("Changing threshold from 0.5 affects precision/recall tradeoff\n")

thresholds = [0.3, 0.5, 0.7]
print("Threshold | Precision | Recall | F1 Score")
print("----------|-----------|--------|----------")
for threshold in thresholds:
    y_pred_thresh = (y_proba_test >= threshold).astype(int)
    precision = precision_score(y_test, y_pred_thresh, zero_division=0)
    recall = recall_score(y_test, y_pred_thresh, zero_division=0)
    f1 = f1_score(y_test, y_pred_thresh, zero_division=0)
    print(f"{threshold:9.1f} | {precision:9.4f} | {recall:6.4f} | {f1:8.4f}")

# MULTI-CLASS CLASSIFICATION
print("\n\n6. Multi-Class Classification - Iris Flowers:")
print("   Predicting: What species of iris flower?\n")

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

scaler_i = StandardScaler()
X_train_i_scaled = scaler_i.fit_transform(X_train_i)
X_test_i_scaled = scaler_i.transform(X_test_i)

# Multi-class logistic regression
logreg_multi = LogisticRegression(max_iter=200, multi_class='multinomial', random_state=42)
logreg_multi.fit(X_train_i_scaled, y_train_i)

y_pred_i = logreg_multi.predict(X_test_i_scaled)

print("Multi-Class Results:")
print(f"Accuracy: {accuracy_score(y_test_i, y_pred_i):.4f}")

print("\nClassification Report:")
print(classification_report(y_test_i, y_pred_i, target_names=iris.target_names))

cm_multi = confusion_matrix(y_test_i, y_pred_i)
print("Confusion Matrix:")
print(cm_multi)

print("\n✅ Logistic Regression lesson complete!")
print("\n🎯 Key Concepts Learned:")
print("  ✓ Binary classification setup and evaluation")
print("  ✓ Multi-class classification with softmax")
print("  ✓ Probability predictions (not just classes)")
print("  ✓ Feature importance from coefficients")
print("  ✓ Confusion matrix and threshold tuning")
