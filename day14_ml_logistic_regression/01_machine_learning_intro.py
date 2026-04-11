# Day 14: Machine Learning Introduction

## Learning Outcomes

- Understand ML fundamentals
- Supervised vs Unsupervised learning
- Build predictive models with scikit-learn
- Evaluate model performance
- Logistic regression for classification

---

## Part 1: ML Fundamentals

### What is Machine Learning?

```
Traditional Programming:
  Input (data) + Rules → Output

Machine Learning:
  Input (data) + Output (labels) → Rules
```

### Types of Learning

| Type | Purpose | Example |
|------|---------|---------|
| **Supervised** | Predict output | Email spam detection |
| **Unsupervised** | Find patterns | Customer grouping |
| **Reinforcement** | Learn from rewards | Game AI |

---

## Part 2: Logistic Regression (Binary Classification)

### The Problem
Predict if a student will pass (1) or fail (0) based on study hours.

### The Solution
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

# Data
X = np.array([[1], [2], [3], [4], [5], [6]])  # Study hours
y = np.array([0, 0, 0, 1, 1, 1])  # Pass/Fail

# Split into train and test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Predict new value
prob = model.predict_proba([[4]])
print(f"Probability of pass with 4 hours: {prob[0][1]:.2f}")
```

---

## Part 3: Complete Example with Real Data

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

# Features and target
X = df[["study_hours", "attendance", "gpa"]]
y = df["passed"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(f"Train accuracy: {train_acc:.2f}")
print(f"Test accuracy: {test_acc:.2f}")

# Feature importance (coefficients)
for feature, coef in zip(X.columns, model.coef_[0]):
    print(f"{feature}: {coef:.3f}")

# Predict on new student
new_student = [[5, 0.9, 3.5]]  # 5 hours, 90% attendance, 3.5 GPA
probability = model.predict_proba(new_student)[0]
print(f"\nProbability of passing: {probability[1]:.2f}")
```

---

## Part 4: More Algorithms

### Decision Tree
```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.2f}")
```

### Random Forest
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
print(f"Accuracy: {model.score(X_test, y_test):.2f}")
```

### K-Means Clustering (Unsupervised)
```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
clusters = model.fit_predict(X)
print(f"Cluster assignments: {clusters}")
```

---

## Part 5: Model Evaluation

### Metrics
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1: {f1:.2f}")
```

### Confusion Matrix
```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
# [[TN  FP]
#  [FN  TP]]
```

### ROC Curve
```python
from sklearn.metrics import roc_curve, roc_auc_score

fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])

plt.plot(fpr, tpr, label=f"ROC (AUC={auc:.2f})")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
```

---

## Part 6: ML Workflow

```
1. Load Data
   ↓
2. Explore & Clean
   ↓
3. Feature Engineering
   ↓
4. Train/Test Split (80/20)
   ↓
5. Choose Model
   ↓
6. Train
   ↓
7. Evaluate
   ↓
8. Tune Hyperparameters
   ↓
9. Final Test
   ↓
10. Deploy
```

---

## Key Concepts

| Concept | Meaning |
|---------|---------|
| **Feature** | Input variable (X) |
| **Target** | Output variable (y) |
| **Training** | Learning from data |
| **Test Set** | Unseen data for evaluation |
| **Overfitting** | Memorized data, poor generalization |
| **Underfitting** | Too simple, poor performance |
| **Hyperparameter** | Setting for algorithm (not learned) |

---

## Common Mistakes

❌ **Train on entire dataset** - No evaluation
✅ **Use train/test split** - Honest evaluation

❌ **Pick first model** - May not be best
✅ **Try multiple models** - Compare performance

❌ **Ignore class imbalance** - Random guessing wins
✅ **Use stratified split** - Preserve ratio

---

## Next Steps

- [ ] Complete all 14 days
- [ ] Review your progress
- [ ] Choose a project combining multiple days
- [ ] Deploy a real application
- [ ] Continue learning advanced topics

---

## Project Ideas

1. **Student Performance Predictor** (Days 2, 6, 14)
   - Predict pass/fail with logistic regression

2. **Sentiment Analyzer** (Days 1-14)
   - Classify reviews as positive/negative

3. **Stock Price Predictor** (Days 9, 13, 14)
   - Analyze historical data, predict future

4. **Todo Web App** (Days 1-6, 10-11)
   - Flask backend + Tkinter/React frontend

5. **Job Recommender** (Days 7, 13, 14)
   - OOP design + ML clustering

---

## Learning Resources

- Kaggle Datasets: https://www.kaggle.com
- Scikit-learn Docs: https://scikit-learn.org
- Machine Learning Course: Andrew Ng's Coursera
- Fast.ai: https://www.fast.ai
