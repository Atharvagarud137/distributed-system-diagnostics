from src.reconciler import ReconciliationPayload, TransactionItem, reconcile_transactions
from src.diagnostics import diagnostics_for_payload


def create_transaction(id: str, amount: float, timestamp: str, status: str) -> TransactionItem:
    return TransactionItem(id=id, amount=amount, timestamp=timestamp, status=status)


def test_reconcile_detects_missing_and_timing_lag():
    payload = ReconciliationPayload(
        payment_processor_txns=[create_transaction("PAY-100", 150.0, "2026-07-03T10:00:00Z", "completed")],
        ledger_txns=[create_transaction("PAY-100", 150.0, "2026-07-03T10:05:00Z", "recorded")],
        settlement_txns=[],
    )
    result = reconcile_transactions(payload)
    assert result.summary["transaction_count"] == 1
    assert any(issue.issue_type == "timing_lag" for issue in result.issues)
    assert any(issue.issue_type == "missing_transaction" for issue in result.issues)


def test_diagnostics_wrapper_returns_issues():
    payload = ReconciliationPayload(
        payment_processor_txns=[create_transaction("PAY-102", 60.0, "2026-07-03T14:00:00Z", "completed")],
        ledger_txns=[create_transaction("PAY-102", 60.0, "2026-07-03T14:02:05Z", "recorded")],
        settlement_txns=[],
    )
    issues = diagnostics_for_payload(payload)
    assert any(issue.issue_type == "timing_lag" for issue in issues)
