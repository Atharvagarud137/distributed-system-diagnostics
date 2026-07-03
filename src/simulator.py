from fastapi.testclient import TestClient

from src.api import app
from src.reconciler import ReconciliationPayload, TransactionItem


def build_test_payload() -> dict:
    return {
        "payment_processor_txns": [
            {
                "id": "PAY-900",
                "amount": 99.99,
                "timestamp": "2026-07-03T15:00:00Z",
                "status": "completed",
            }
        ],
        "ledger_txns": [
            {
                "id": "PAY-900",
                "amount": 99.99,
                "timestamp": "2026-07-03T15:02:30Z",
                "status": "recorded",
            }
        ],
        "settlement_txns": [],
    }


def run_local_diagnostic() -> dict:
    with TestClient(app) as client:
        response = client.post("/diagnose", json=build_test_payload())
        response.raise_for_status()
        return response.json()
