"""
app.py
Student Marks Prediction - Flask Application
Routes: / (home), /health, /predict, /api/predict (REST)
"""

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# ── Load model ────────────────────────────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

FEATURES = [
    "hours_studied",
    "previous_scores",
    "extracurricular",
    "sleep_hours",
    "practice_papers",
]

# ── Validation helpers ────────────────────────────────────────────────────────
def validate_input(data: dict):
    """Return (values_dict, error_message). error_message is None on success."""
    errors = []
    values = {}

    # hours_studied: 0 – 24
    try:
        v = float(data["hours_studied"])
        if not (0 <= v <= 24):
            errors.append("hours_studied must be between 0 and 24.")
        values["hours_studied"] = v
    except (KeyError, ValueError, TypeError):
        errors.append("hours_studied is required and must be a number.")

    # previous_scores: 0 – 100
    try:
        v = float(data["previous_scores"])
        if not (0 <= v <= 100):
            errors.append("previous_scores must be between 0 and 100.")
        values["previous_scores"] = v
    except (KeyError, ValueError, TypeError):
        errors.append("previous_scores is required and must be a number.")

    # extracurricular: 0 or 1
    try:
        v = int(data["extracurricular"])
        if v not in (0, 1):
            errors.append("extracurricular must be 0 (No) or 1 (Yes).")
        values["extracurricular"] = v
    except (KeyError, ValueError, TypeError):
        errors.append("extracurricular is required and must be 0 or 1.")

    # sleep_hours: 0 – 24
    try:
        v = float(data["sleep_hours"])
        if not (0 <= v <= 24):
            errors.append("sleep_hours must be between 0 and 24.")
        values["sleep_hours"] = v
    except (KeyError, ValueError, TypeError):
        errors.append("sleep_hours is required and must be a number.")

    # practice_papers: 0 – 10
    try:
        v = int(data["practice_papers"])
        if not (0 <= v <= 10):
            errors.append("practice_papers must be between 0 and 10.")
        values["practice_papers"] = v
    except (KeyError, ValueError, TypeError):
        errors.append("practice_papers is required and must be a number.")

    if errors:
        return None, "; ".join(errors)
    return values, None


def run_prediction(values: dict) -> float:
    X = np.array([[values[f] for f in FEATURES]])
    pred = model.predict(X)[0]
    return float(np.clip(pred, 0, 100))


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    """Home page with input form."""
    return render_template("index.html")


@app.route("/health")
def health():
    """Health-check endpoint."""
    return jsonify({
        "status": "healthy",
        "model": "Student Marks Predictor",
        "algorithm": "Linear Regression",
        "version": "1.0.0",
    }), 200


@app.route("/predict", methods=["POST"])
def predict():
    """Form-based prediction – returns rendered page with result."""
    values, error = validate_input(request.form)
    if error:
        return render_template("index.html", error=error)
    prediction = run_prediction(values)
    grade = (
        "A+" if prediction >= 90 else
        "A"  if prediction >= 80 else
        "B"  if prediction >= 70 else
        "C"  if prediction >= 60 else
        "D"  if prediction >= 50 else "F"
    )
    return render_template(
        "index.html",
        prediction=round(prediction, 2),
        grade=grade,
        inputs=values,
    )


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """REST API endpoint – accepts JSON, returns JSON."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415

    values, error = validate_input(request.get_json())
    if error:
        return jsonify({"error": error}), 400

    prediction = run_prediction(values)
    grade = (
        "A+" if prediction >= 90 else
        "A"  if prediction >= 80 else
        "B"  if prediction >= 70 else
        "C"  if prediction >= 60 else
        "D"  if prediction >= 50 else "F"
    )
    return jsonify({
        "predicted_marks": round(prediction, 2),
        "grade": grade,
        "inputs": values,
    }), 200


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
