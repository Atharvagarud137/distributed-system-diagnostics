from fastapi.testclient import TestClient

from src.api import app
from src.diagnostics import diagnostics_for_payload
from src.reconciler import ReconciliationPayload


def test_api_root() -> None:
    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"service": "distributed-system-diagnostics", "status": "ok"}


def test_api_diagnose_returns_issues() -> None:
    payload = {
        "payment_processor_txns": [
            {"id": "PAY-101", "amount": 75.0, "timestamp": "2026-07-03T12:00:00Z", "status": "completed"}
        ],
        "ledger_txns": [
            {"id": "PAY-101", "amount": 75.0, "timestamp": "2026-07-03T12:02:00Z", "status": "recorded"}
        ],
        "settlement_txns": [],
    }

    with TestClient(app) as client:
        response = client.post("/diagnose", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["transaction_count"] == 1
    assert body["summary"]["issue_count"] >= 1
    assert any(issue["issue_type"] == "timing_lag" for issue in body["diagnostics"])


def test_api_batch_diagnose_matches_diagnose() -> None:
    payload = {
        "payment_processor_txns": [
            {"id": "PAY-102", "amount": 125.0, "timestamp": "2026-07-03T13:00:00Z", "status": "completed"}
        ],
        "ledger_txns": [
            {"id": "PAY-102", "amount": 125.0, "timestamp": "2026-07-03T13:03:00Z", "status": "recorded"}
        ],
        "settlement_txns": [],
    }

    with TestClient(app) as client:
        response = client.post("/batch-diagnose", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["transaction_count"] == 1
    assert body["summary"]["issue_count"] >= 1
    assert any(issue["issue_type"] == "timing_lag" for issue in body["diagnostics"])
