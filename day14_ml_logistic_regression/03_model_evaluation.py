#!/usr/bin/env python3
"""Day 14, Lesson 3: Model Evaluation - Assessing ML Model Performance

Learn to evaluate your models properly:
- Multiple metrics (accuracy, precision, recall, F1)
- ROC-AUC curves
- Cross-validation
- Hyperparameter tuning
- Model comparison
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split, cross_val_score, GridSearchCV, learning_curve
)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, auc, confusion_matrix,
    precision_recall_curve, average_precision_score
)
import numpy as np
import matplotlib.pyplot as plt

print("=== Model Evaluation: Assessing Performance ===\n")

# Load data
cancer = load_breast_cancer()
X, y = cancer.data, cancer.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. MULTIPLE EVALUATION METRICS
print("1. Comprehensive Metrics:")
print("   (Don't just use accuracy!)\n")

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

metrics = {
    'Accuracy': accuracy_score(y_test, y_pred),
    'Precision': precision_score(y_test, y_pred),
    'Recall': recall_score(y_test, y_pred),
    'F1 Score': f1_score(y_test, y_pred),
    'ROC-AUC': roc_auc_score(y_test, y_proba),
    'Avg Precision': average_precision_score(y_test, y_proba)
}

print("Metric          | Value")
print("-" * 25)
for metric, value in metrics.items():
    print(f"{metric:15} | {value:.4f}")

# 2. CROSS-VALIDATION
print("\n2. Cross-Validation (K-Fold):")
print("   Test on different data splits to avoid overfitting\n")

cv_scores = cross_val_score(
    LogisticRegression(max_iter=1000),
    X_train_scaled, y_train,
    cv=5,
    scoring='accuracy'
)

print(f"5-Fold CV Scores: {[f'{s:.4f}' for s in cv_scores]}")
print(f"Mean: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# 3. HYPERPARAMETER TUNING
print("\n3. Hyperparameter Tuning (Grid Search):")
print("   Finding best parameters for the model\n")

param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10],
    'penalty': ['l2'],
    'solver': ['lbfgs']
}

grid_search = GridSearchCV(
    LogisticRegression(max_iter=1000),
    param_grid,
    cv=5,
    scoring='f1',
    n_jobs=-1
)

grid_search.fit(X_train_scaled, y_train)

print(f"Best Parameters: {grid_search.best_params_}")
print(f"Best CV F1 Score: {grid_search.best_score_:.4f}")

# Evaluate best model
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
print(f"Test F1 Score (Best Model): {f1_score(y_test, y_pred_best):.4f}")

# 4. MODEL COMPARISON
print("\n4. Comparing Models:")
print("   Which model performs best?\n")

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

print("Model                  | Accuracy | F1 Score | ROC-AUC | CV Mean")
print("-" * 65)

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1]
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    cv = cross_val_score(model, X_train_scaled, y_train, cv=5).mean()
    
    print(f"{name:22} | {acc:8.4f} | {f1:8.4f} | {auc:7.4f} | {cv:.4f}")

# 5. CONFUSION MATRIX ANALYSIS
print("\n5. Detailed Confusion Matrix:")

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

print(f"                 Predicted")
print(f"              Negative  Positive")
print(f"Actual Neg    {tn:7}    {fp:7}  (Specificity: {tn/(tn+fp):.4f})")
print(f"Actual Pos    {fn:7}    {tp:7}  (Sensitivity: {tp/(tp+fn):.4f})")

print("\nInterpretation:")
print(f"  • True Negatives: {tn} (correctly predicted negative)")
print(f"  • False Positives: {fp} (incorrectly predicted positive)")
print(f"  • False Negatives: {fn} (incorrectly predicted negative)")
print(f"  • True Positives: {tp} (correctly predicted positive)")

# 6. ROC-AUC EXPLANATION
print("\n6. ROC-AUC Curve Logic:")
print("   (Area Under the Receiver Operating Characteristic Curve)\n")

fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

print(f"ROC-AUC Score: {roc_auc:.4f}")
print("\nInterpretation:")
print(f"  • Perfect model: ROC-AUC = 1.0")
print(f"  • Random model: ROC-AUC = 0.5")
print(f"  • Your model: ROC-AUC = {roc_auc:.4f}")
print(f"  • Quality: {'Excellent' if roc_auc > 0.9 else 'Good' if roc_auc > 0.8 else 'Fair'}")

# 7. LEARNING CURVES
print("\n7. Learning Curves (does more data help?):")

train_sizes = np.linspace(0.1, 1.0, 10)
train_sizes_abs, train_scores, val_scores = learning_curve(
    LogisticRegression(max_iter=1000),
    X_train_scaled, y_train,
    cv=5,
    train_sizes=train_sizes,
    scoring='f1'
)

train_mean = np.mean(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)

print("\nSample Size | Train F1 | Validation F1 | Gap")
print("-" * 50)
for size, train_f1, val_f1 in zip(train_sizes_abs, train_mean, val_mean):
    gap = train_f1 - val_f1
    print(f"{int(size):11} | {train_f1:8.4f} | {val_f1:13.4f} | {gap:6.4f}")

if train_mean[-1] > val_mean[-1]:
    print("\n⚠️  Model shows signs of overfitting (training > validation)")
else:
    print("\n✓ Model generalizes well!")

# 8. PRACTICAL RECOMMENDATIONS
print("\n8. Model Selection Guide:")
print("\nUse accuracy when:")
print("  • Classes are balanced")
print("  • All errors have equal cost")

print("\nUse precision when:")
print("  • False positives are costly (spam detection)")
print("  • You want to minimize false alarms")

print("\nUse recall when:")
print("  • False negatives are costly (disease detection)")
print("  • You want to catch all positive cases")

print("\nUse F1 when:")
print("  • You need balance between precision and recall")
print("  • Classes are imbalanced")

print("\nUse ROC-AUC when:")
print("  • You're evaluating probability thresholds")
print("  • Classes are imbalanced")

print("\n✅ Model Evaluation lesson complete!")
print("\n🎯 Evaluation Checklist:")
print("  ✓ Use multiple metrics (not just accuracy)")
print("  ✓ Use cross-validation (don't just test/train split)")
print("  ✓ Compare against baseline models")
print("  ✓ Tune hyperparameters systematically")
print("  ✓ Check for overfitting (learning curves)")
print("  ✓ Understand your errors (confusion matrix)")
