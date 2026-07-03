from fastapi.testclient import TestClient

from src.api import app
from src.diagnostics import diagnostics_for_payload
from src.reconciler import ReconciliationPayload, TransactionItem, reconcile_transactions


def create_transaction(id: str, amount: float, timestamp: str, status: str) -> TransactionItem:
    return TransactionItem(id=id, amount=amount, timestamp=timestamp, status=status)


def test_reconcile_missing_and_timing_lag() -> None:
    payload = ReconciliationPayload(
        payment_processor_txns=[create_transaction("PAY-100", 150.0, "2026-07-03T10:00:00Z", "completed")],
        ledger_txns=[create_transaction("PAY-100", 150.0, "2026-07-03T10:05:00Z", "recorded")],
        settlement_txns=[],
    )
    result = reconcile_transactions(payload)
    assert result.summary["transaction_count"] == 1
    assert result.summary["issue_count"] >= 2


def test_api_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        response = client.post("/diagnose", json={
            "payment_processor_txns": [
                {"id": "PAY-101", "amount": 75.0, "timestamp": "2026-07-03T12:00:00Z", "status": "completed"}
            ],
            "ledger_txns": [
                {"id": "PAY-101", "amount": 75.0, "timestamp": "2026-07-03T12:02:00Z", "status": "recorded"}
            ],
            "settlement_txns": [],
        })
        assert response.status_code == 200


def test_diagnostics_wrapper() -> None:
    payload = ReconciliationPayload(
        payment_processor_txns=[create_transaction("PAY-102", 60.0, "2026-07-03T14:00:00Z", "completed")],
        ledger_txns=[create_transaction("PAY-102", 60.0, "2026-07-03T14:02:05Z", "recorded")],
        settlement_txns=[],
    )
    issues = diagnostics_for_payload(payload)
    assert any(issue.issue_type == "timing_lag" for issue in issues)
