# ✅ Day 14: Machine Learning - Logistic Regression - SOLUTIONS

## Solution 1: Iris Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.4f}")
```

## Solution 2: Binary Classification

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

## Solution 3: Feature Scaling

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Without scaling
model1 = LogisticRegression()
model1.fit(X_train, y_train)
acc1 = accuracy_score(y_test, model1.predict(X_test))
print(f"Without scaling: {acc1:.4f}")

# With scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model2 = LogisticRegression()
model2.fit(X_train_scaled, y_train)
acc2 = accuracy_score(y_test, model2.predict(X_test_scaled))
print(f"With scaling: {acc2:.4f}")
```

## Solution 4: ROC Curve

```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

y_pred_proba = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred_proba)

fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig('roc_curve.png')
plt.show()
```

## Solution 5: Complete ML Pipeline

```python
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# EDA
print(f"Dataset shape: {X.shape}")
print(f"Classes: {len(set(y))}")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=10000)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True')
plt.xlabel('Predicted')
plt.savefig('confusion_matrix.png')

# Save model
with open('logistic_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\n✅ Model saved to logistic_model.pkl")
```

---

## Key Concepts Summary

1. **Train-Test Split**: Always split data (80/20 or 70/30)
2. **Feature Scaling**: Essential for distance-based algorithms
3. **Logistic Regression**: Used for binary/multiclass classification
4. **Evaluation Metrics**: Accuracy, Precision, Recall, F1, ROC-AUC
5. **Model Persistence**: Save with pickle for reuse
6. **Confusion Matrix**: Visualize true/false positives and negatives

## Common Mistakes to Avoid

❌ Not scaling features  
❌ Using all data for training (no test set)  
❌ Ignoring class imbalance  
❌ Not comparing multiple metrics  
❌ Overfitting to small datasets  
❌ Not saving the scaler with the model  

## Next Steps

- Explore other algorithms (SVM, Random Forest, Neural Networks)
- Learn about hyperparameter tuning
- Study ensemble methods
- Try deep learning frameworks (TensorFlow, PyTorch)
