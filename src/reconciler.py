from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field

class TransactionItem(BaseModel):
    id: str
    amount: float
    timestamp: str
    status: str

class ReconciliationPayload(BaseModel):
    payment_processor_txns: List[TransactionItem] = Field(default_factory=list)
    ledger_txns: List[TransactionItem] = Field(default_factory=list)
    settlement_txns: List[TransactionItem] = Field(default_factory=list)

class ReconciliationIssue(BaseModel):
    issue_type: str
    severity: str
    description: str
    affected_systems: List[str]
    confidence: float
    remediation: str
    transaction_id: Optional[str] = None
    details: Optional[Dict[str, str]] = None

class ReconciliationResult(BaseModel):
    issues: List[ReconciliationIssue] = Field(default_factory=list)
    summary: Dict[str, int] = Field(default_factory=dict)


def _parse_timestamp(timestamp: str) -> datetime:
    if not isinstance(timestamp, str) or not timestamp:
        raise ValueError("Missing or invalid timestamp")
    normalized = timestamp.replace("Z", "+00:00")
    return datetime.fromisoformat(normalized)


def _issue(
    issue_type: str,
    transaction_id: Optional[str],
    description: str,
    affected_systems: List[str],
    remediation: str,
    confidence: float,
    details: Optional[Dict[str, str]] = None,
) -> ReconciliationIssue:
    return ReconciliationIssue(
        issue_type=issue_type,
        transaction_id=transaction_id,
        description=description,
        affected_systems=affected_systems,
        confidence=confidence,
        remediation=remediation,
        details=details,
        severity="high" if issue_type in {"missing_transaction", "amount_mismatch"} else "medium",
    )


def reconcile_transactions(payload: ReconciliationPayload) -> ReconciliationResult:
    systems = {
        "payment_processor": payload.payment_processor_txns,
        "ledger": payload.ledger_txns,
        "settlement": payload.settlement_txns,
    }

    id_map = {name: {} for name in systems}
    all_ids = set()

    for name, transactions in systems.items():
        for txn in transactions:
            all_ids.add(txn.id)
            id_map[name].setdefault(txn.id, []).append(txn)

    issues: List[ReconciliationIssue] = []

    for txn_id in sorted(all_ids):
        present_systems = [name for name, items in id_map.items() if txn_id in items]
        missing_systems = [name for name in systems if name not in present_systems]

        for system_name, items in id_map.items():
            duplicates = items.get(txn_id, [])
            if len(duplicates) > 1:
                issues.append(
                    _issue(
                        issue_type="duplicate_transaction",
                        transaction_id=txn_id,
                        description=(
                            f"Transaction {txn_id} appears {len(duplicates)} times in {system_name}."
                        ),
                        affected_systems=[system_name],
                        remediation=(
                            f"Review idempotency and duplicate suppression for {system_name} ingestion."
                        ),
                        confidence=0.92,
                        details={"system": system_name, "count": str(len(duplicates))},
                    )
                )

        if missing_systems and len(present_systems) >= 1:
            issues.append(
                _issue(
                    issue_type="missing_transaction",
                    transaction_id=txn_id,
                    description=(
                        f"Transaction {txn_id} is present in {present_systems} but missing from {missing_systems}."
                    ),
                    affected_systems=present_systems + missing_systems,
                    remediation=(
                        "Investigate the downstream pipeline and confirm whether the transaction was dropped or delayed."
                    ),
                    confidence=0.95,
                    details={"missing_systems": ", ".join(missing_systems)},
                )
            )

        system_amounts: Dict[str, float] = {}
        system_timestamps: Dict[str, str] = {}
        invalid_timestamp = False

        for system_name in present_systems:
            txn = id_map[system_name][txn_id][0]
            system_amounts[system_name] = txn.amount
            system_timestamps[system_name] = txn.timestamp
            try:
                _parse_timestamp(txn.timestamp)
            except ValueError:
                invalid_timestamp = True
                issues.append(
                    _issue(
                        issue_type="data_quality_issue",
                        transaction_id=txn_id,
                        description=(
                            f"Timestamp for transaction {txn_id} in {system_name} is invalid: {txn.timestamp}."
                        ),
                        affected_systems=[system_name],
                        remediation=(
                            "Validate input formatting and inspect the ingestion pipeline for malformed records."
                        ),
                        confidence=0.88,
                        details={"system": system_name, "timestamp": txn.timestamp},
                    )
                )

        if len(system_amounts) > 1:
            unique_amounts = set(system_amounts.values())
            if len(unique_amounts) > 1:
                issues.append(
                    _issue(
                        issue_type="amount_mismatch",
                        transaction_id=txn_id,
                        description=(
                            f"Transaction {txn_id} has inconsistent amounts across systems: {system_amounts}."
                        ),
                        affected_systems=list(system_amounts.keys()),
                        remediation=(
                            "Verify fee, rounding, or transformation logic between systems."
                        ),
                        confidence=0.90,
                        details={"amounts": ", ".join(f"{k}={v:.2f}" for k, v in system_amounts.items())},
                    )
                )

        if not invalid_timestamp and "payment_processor" in system_timestamps and "ledger" in system_timestamps:
            try:
                payment_ts = _parse_timestamp(system_timestamps["payment_processor"])
                ledger_ts = _parse_timestamp(system_timestamps["ledger"])
                if ledger_ts > payment_ts and (ledger_ts - payment_ts).total_seconds() >= 120:
                    issues.append(
                        _issue(
                            issue_type="timing_lag",
                            transaction_id=txn_id,
                            description=(
                                f"Ledger timestamp is {ledger_ts.isoformat()} while payment timestamp is {payment_ts.isoformat()} for {txn_id}."
                            ),
                            affected_systems=["payment_processor", "ledger"],
                            remediation=(
                                "Check asynchronous ingestion latency and queue backpressure."
                            ),
                            confidence=0.90,
                            details={
                                "payment_timestamp": system_timestamps["payment_processor"],
                                "ledger_timestamp": system_timestamps["ledger"],
                            },
                        )
                    )
            except ValueError:
                pass

    summary = {
        "transaction_count": len(all_ids),
        "issue_count": len(issues),
    }
    return ReconciliationResult(issues=issues, summary=summary)
