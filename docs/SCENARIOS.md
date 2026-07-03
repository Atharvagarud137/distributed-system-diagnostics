# Reconciliation Scenarios

This document captures realistic transaction mismatch scenarios that the diagnostics toolkit is designed to detect and explain. Each scenario includes the problem, the expected diagnostic output, and remediation guidance.

## Scenario 1: Timing Lag between Payment and Ledger

### Problem
A payment is accepted by the payment processor but recorded in the ledger several minutes later. This type of mismatch is common when asynchronous processing queues or batch jobs are involved.

### Input Example
```json
{
  "payment_processor_txns": [
    {"id": "PAY-100", "amount": 150.00, "timestamp": "2026-07-03T10:00:00Z", "status": "completed"}
  ],
  "ledger_txns": [
    {"id": "PAY-100", "amount": 150.00, "timestamp": "2026-07-03T10:05:00Z", "status": "recorded"}
  ],
  "settlement_txns": []
}
```

### Expected Diagnostic Output
- type: `timing_lag`
- severity: `medium`
- description: `Payment recorded at 10:00 but ledger entry appears at 10:05 (5 min lag)`
- confidence: `0.90`
- affected_systems: `["payment_processor", "ledger"]`
- remediation: `Check the ledger ingestion queue and review async processing latency`

### Why it matters
A consistent timing lag can indicate operational delays, downstream backpressure, or batch window configuration issues.

---

## Scenario 2: Missing Transaction in Settlement

### Problem
A transaction exists in the payment processor and ledger, but settlement never receives the corresponding record. This indicates a gap in the downstream settlement pipeline.

### Input Example
```json
{
  "payment_processor_txns": [
    {"id": "PAY-200", "amount": 220.00, "timestamp": "2026-07-03T11:00:00Z", "status": "completed"}
  ],
  "ledger_txns": [
    {"id": "PAY-200", "amount": 220.00, "timestamp": "2026-07-03T11:01:00Z", "status": "recorded"}
  ],
  "settlement_txns": []
}
```

### Expected Diagnostic Output
- type: `missing_transaction`
- severity: `high`
- description: `Transaction PAY-200 is present in payment and ledger systems but missing from settlement`
- confidence: `0.95`
- affected_systems: `["payment_processor", "ledger", "settlement"]`
- remediation: `Investigate the settlement ingestion pipeline and confirm whether the transaction was dropped or delayed`

### Why it matters
Missing settlement records create funding gaps and increase reconciliation effort during settlement cycles.

---

## Scenario 3: Duplicate Transaction in Ledger

### Problem
A payment appears once in the payment processor but twice in the ledger, indicating a duplicate or idempotency failure in the ledger ingestion process.

### Input Example
```json
{
  "payment_processor_txns": [
    {"id": "PAY-300", "amount": 75.00, "timestamp": "2026-07-03T12:00:00Z", "status": "completed"}
  ],
  "ledger_txns": [
    {"id": "PAY-300", "amount": 75.00, "timestamp": "2026-07-03T12:01:00Z", "status": "recorded"},
    {"id": "PAY-300", "amount": 75.00, "timestamp": "2026-07-03T12:01:05Z", "status": "recorded"}
  ],
  "settlement_txns": [
    {"id": "PAY-300", "amount": 75.00, "timestamp": "2026-07-03T12:10:00Z", "status": "settled"}
  ]
}
```

### Expected Diagnostic Output
- type: `duplicate_transaction`
- severity: `medium`
- description: `Transaction PAY-300 appears twice in ledger records but only once in payment and settlement systems`
- confidence: `0.92`
- affected_systems: `["ledger"]`
- remediation: `Review ledger ingestion idempotency controls and duplicate suppression logic`

### Why it matters
Duplicate ledger entries can cause incorrect balances and force manual investigation or write-off workflows.

---

## Scenario 4: Amount Mismatch between Ledger and Settlement

### Problem
A transaction has the same ID across systems, but the settlement amount differs from the ledger amount. This can indicate rounding rules, fee application, or corruption in one path.

### Input Example
```json
{
  "payment_processor_txns": [
    {"id": "PAY-400", "amount": 500.00, "timestamp": "2026-07-03T13:00:00Z", "status": "completed"}
  ],
  "ledger_txns": [
    {"id": "PAY-400", "amount": 500.00, "timestamp": "2026-07-03T13:01:00Z", "status": "recorded"}
  ],
  "settlement_txns": [
    {"id": "PAY-400", "amount": 499.50, "timestamp": "2026-07-03T13:10:00Z", "status": "settled"}
  ]
}
```

### Expected Diagnostic Output
- type: `amount_mismatch`
- severity: `high`
- description: `Ledger amount is 500.00 but settlement amount is 499.50 for transaction PAY-400` 
- confidence: `0.90`
- affected_systems: `["ledger", "settlement"]`
- remediation: `Verify fee or rounding logic applied during settlement processing`

### Why it matters
Amount mismatches may signal financial loss, fee miscalculation, or settlement rules being applied incorrectly.

---

## Scenario 5: Corrupted Timestamp or Invalid Data

### Problem
A transaction record includes an invalid timestamp or malformed field, causing downstream matching errors. This scenario tests robustness against data quality issues.

### Input Example
```json
{
  "payment_processor_txns": [
    {"id": "PAY-500", "amount": 300.00, "timestamp": "2026-07-03T14:00:00Z", "status": "completed"}
  ],
  "ledger_txns": [
    {"id": "PAY-500", "amount": 300.00, "timestamp": "INVALID_TIMESTAMP", "status": "recorded"}
  ],
  "settlement_txns": [
    {"id": "PAY-500", "amount": 300.00, "timestamp": "2026-07-03T14:15:00Z", "status": "settled"}
  ]
}
```

### Expected Diagnostic Output
- type: `data_quality_issue`
- severity: `medium`
- description: `Ledger timestamp for PAY-500 is invalid and cannot be used for timing comparison` 
- confidence: `0.88`
- affected_systems: `["ledger"]`
- remediation: `Validate input formatting and inspect the ledger ingestion pipeline for malformed records`

### Why it matters
Detecting bad input early reduces reconciliation noise and improves confidence in automated matching.

---

## How to Use These Scenarios

- Use them as test cases for unit tests and integration tests.
- Reference them when building simulator scenario generators.
- Include the sample inputs in documentation or sample request payloads.
- Extend the list with new cases such as currency mismatches, partial settlement, or delayed retries.
