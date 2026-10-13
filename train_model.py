"""
train_model.py
Student Marks Prediction - Linear Regression
Trains the model and serializes it to model.pkl
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# ── 1. Generate / load dataset ──────────────────────────────────────────────
np.random.seed(42)
n = 200

hours_studied          = np.random.uniform(1, 9, n)
previous_scores        = np.random.uniform(40, 99, n)
extracurricular        = np.random.randint(0, 2, n)   # 0 = No, 1 = Yes
sleep_hours            = np.random.uniform(4, 9, n)
practice_papers        = np.random.randint(0, 10, n)

# Target: weighted combination + noise
marks = (
    6  * hours_studied
    + 0.5 * previous_scores
    + 2  * extracurricular
    + 1.5 * sleep_hours
    + 1.2 * practice_papers
    + np.random.normal(0, 3, n)
)
marks = np.clip(marks, 0, 100)

df = pd.DataFrame({
    "hours_studied":       hours_studied,
    "previous_scores":     previous_scores,
    "extracurricular":     extracurricular,
    "sleep_hours":         sleep_hours,
    "practice_papers":     practice_papers,
    "marks":               marks,
})

print("=" * 50)
print("  Student Marks Prediction - Model Training")
print("=" * 50)
print(f"\nDataset shape : {df.shape}")
print(f"Target range  : {marks.min():.2f} – {marks.max():.2f}")
print(f"\nSample data:\n{df.head(5).to_string(index=False)}")

# ── 2. Split ─────────────────────────────────────────────────────────────────
FEATURES = ["hours_studied", "previous_scores", "extracurricular",
            "sleep_hours", "practice_papers"]

X = df[FEATURES]
y = df["marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTrain size : {len(X_train)} | Test size : {len(X_test)}")

# ── 3. Build pipeline ────────────────────────────────────────────────────────
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model",  LinearRegression()),
])

pipeline.fit(X_train, y_train)

# ── 4. Evaluate ───────────────────────────────────────────────────────────────
y_pred = pipeline.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n" + "=" * 50)
print("  Evaluation Metrics")
print("=" * 50)
print(f"  MAE  : {mae:.4f}")
print(f"  MSE  : {mse:.4f}")
print(f"  RMSE : {rmse:.4f}")
print(f"  R²   : {r2:.4f}")

coef = pipeline.named_steps["model"].coef_
print("\n  Feature Coefficients:")
for feat, c in zip(FEATURES, coef):
    print(f"    {feat:<22} : {c:.4f}")

# ── 5. Serialize ─────────────────────────────────────────────────────────────
joblib.dump(pipeline, "model.pkl")
print("\n  model.pkl saved successfully [OK]")
print("=" * 50)
