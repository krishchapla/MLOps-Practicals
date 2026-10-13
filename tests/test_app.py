"""
tests/test_app.py
Unit and integration tests for the Student Marks Prediction Flask app.
Run with: pytest tests/ -v
"""

import json
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app, validate_input, run_prediction


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# ── Route tests ──────────────────────────────────────────────────────────────

def test_home_status(client):
    """GET / should return 200 and contain form."""
    r = client.get("/")
    assert r.status_code == 200
    assert b"Predict" in r.data


def test_health_endpoint(client):
    """GET /health should return JSON with status healthy."""
    r = client.get("/health")
    assert r.status_code == 200
    data = json.loads(r.data)
    assert data["status"] == "healthy"
    assert "model" in data
    assert "version" in data


def test_api_predict_valid(client):
    """POST /api/predict with valid JSON should return 200 and a prediction."""
    payload = {
        "hours_studied":   6,
        "previous_scores": 78,
        "extracurricular": 1,
        "sleep_hours":     7,
        "practice_papers": 5,
    }
    r = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert r.status_code == 200
    data = json.loads(r.data)
    assert "predicted_marks" in data
    assert 0 <= data["predicted_marks"] <= 100
    assert "grade" in data


def test_api_predict_missing_field(client):
    """POST /api/predict with a missing field should return 400."""
    payload = {
        "hours_studied":   6,
        "previous_scores": 78,
        # extracurricular missing
        "sleep_hours":     7,
        "practice_papers": 5,
    }
    r = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert r.status_code == 400
    data = json.loads(r.data)
    assert "error" in data


def test_api_predict_out_of_range(client):
    """POST /api/predict with out-of-range values should return 400."""
    payload = {
        "hours_studied":   999,   # Invalid
        "previous_scores": 78,
        "extracurricular": 1,
        "sleep_hours":     7,
        "practice_papers": 5,
    }
    r = client.post(
        "/api/predict",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert r.status_code == 400


def test_api_predict_wrong_content_type(client):
    """POST /api/predict without JSON content type should return 415."""
    r = client.post("/api/predict", data="not json")
    assert r.status_code == 415


# ── Validation unit tests ────────────────────────────────────────────────────

def test_validate_input_valid():
    data = {
        "hours_studied":   "6",
        "previous_scores": "78",
        "extracurricular": "1",
        "sleep_hours":     "7",
        "practice_papers": "5",
    }
    values, error = validate_input(data)
    assert error is None
    assert values["hours_studied"] == 6.0
    assert values["extracurricular"] == 1


def test_validate_input_bad_hours():
    data = {
        "hours_studied":   "30",   # >24
        "previous_scores": "78",
        "extracurricular": "1",
        "sleep_hours":     "7",
        "practice_papers": "5",
    }
    values, error = validate_input(data)
    assert values is None
    assert "hours_studied" in error


# ── Prediction unit test ─────────────────────────────────────────────────────

def test_run_prediction_range():
    values = {
        "hours_studied":   6,
        "previous_scores": 78,
        "extracurricular": 1,
        "sleep_hours":     7,
        "practice_papers": 5,
    }
    pred = run_prediction(values)
    assert isinstance(pred, float)
    assert 0 <= pred <= 100
