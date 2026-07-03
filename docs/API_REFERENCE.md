# API Reference

This document describes the public API endpoints for the Distributed System Health Monitor & Diagnostic Toolkit.

## Overview

The service exposes three endpoints:

- `GET /health` — service health check
- `POST /diagnose` — diagnose a single transaction payload across payment, ledger, and settlement systems
- `POST /batch-diagnose` — process a batch of transactions or CSV-style payloads

All request and response payloads use JSON. The service is designed for lightweight local use and containerized deployment.

---

## GET /health

### Description

Returns a simple health check response to confirm that the API is running.

### Request

- Method: `GET`
- Path: `/health`

### Response

- Status: `200 OK`
- Content-Type: `application/json`

```json
{
  "status": "healthy",
  "timestamp": "2026-07-03T10:00:00Z"
}
```

### Notes

- Use this endpoint for readiness checks in Docker, Kubernetes, or deployment monitoring.
- It does not execute reconciliation logic.

---

## POST /diagnose

### Description

Diagnoses transaction mismatches across the payment processor, ledger, and settlement data sets.

### Request

- Method: `POST`
- Path: `/diagnose`
- Content-Type: `application/json`

### Request Payload

```json
{
  "payment_processor_txns": [
    {
      "id": "PAY-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:00:00Z",
      "status": "completed"
    }
  ],
  "ledger_txns": [
    {
      "id": "LED-001",
      "amount": 100.00,
      "timestamp": "2026-07-03T10:05:00Z",
      "status": "recorded"
    }
  ],
  "settlement_txns": [
    {
      "id": "SET-001",
      "amount": 99.50,
      "timestamp": "2026-07-03T10:10:00Z",
      "status": "settled"
    }
  ]
}
```

### Request Fields

- `payment_processor_txns`: array of transaction objects from the payment processor
- `ledger_txns`: array of transaction objects from the ledger
- `settlement_txns`: array of transaction objects from the settlement system

Each transaction object should include:

- `id` (string): transaction identifier
- `amount` (number): transaction amount
- `timestamp` (string): ISO 8601 timestamp
- `status` (string): transaction status

### Response

- Status: `200 OK`
- Content-Type: `application/json`

```json
{
  "matches": 1,
  "mismatches": 2,
  "total_transactions": 3,
  "diagnostics": [
    {
      "type": "timing_lag",
      "severity": "medium",
      "description": "Payment processed at 10:00 but recorded in ledger at 10:05 (5 min lag)",
      "confidence": 0.92,
      "affected_systems": ["payment_processor", "ledger"],
      "remediation": "Check network latency or ledger async processing queue"
    },
    {
      "type": "amount_mismatch",
      "severity": "high",
      "description": "Settlement shows $99.50, ledger shows $100.00 (0.50 difference)",
      "confidence": 0.88,
      "affected_systems": ["ledger", "settlement"],
      "remediation": "Investigate rounding logic or exchange rate applied in settlement"
    }
  ]
}
```

### Response Fields

- `matches` (integer): number of successfully matched transactions
- `mismatches` (integer): number of detected mismatches
- `total_transactions` (integer): total count of transaction records processed
- `diagnostics` (array): list of diagnostic results for mismatches

Each diagnostic object includes:

- `type` (string): mismatch category, such as `timing_lag`, `amount_mismatch`, `missing_transaction`, `duplicate_transaction`, or `data_quality_issue`
- `severity` (string): `low`, `medium`, or `high`
- `description` (string): human-readable explanation of the mismatch
- `confidence` (number): estimated confidence score from `0.0` to `1.0`
- `affected_systems` (array): systems involved in the mismatch
- `remediation` (string): suggested next step for operations or engineering teams

### Validation

- The endpoint validates required arrays and basic transaction fields.
- Requests missing one or more transaction sets should still be accepted, but may produce lower-confidence diagnostics.
- Invalid timestamps or malformed records should be flagged as `data_quality_issue` if detected.

---

## POST /batch-diagnose

### Description

Processes a larger batch of transactions for high-volume reconciliation use cases.

### Request

- Method: `POST`
- Path: `/batch-diagnose`
- Content-Type: `application/json`

### Request Payload

The payload structure is the same as `/diagnose`, but it is intended for larger payloads and may support CSV-style ingestion in future versions.

```json
{
  "payment_processor_txns": [...],
  "ledger_txns": [...],
  "settlement_txns": [...]
}
```

### Response

- Status: `200 OK`
- Content-Type: `application/json`

```json
{
  "matches": 225,
  "mismatches": 15,
  "total_transactions": 240,
  "diagnostics": [
    {
      "type": "missing_transaction",
      "severity": "high",
      "description": "Transaction PAY-230 is present in payment and ledger but missing in settlement",
      "confidence": 0.95,
      "affected_systems": ["payment_processor", "ledger", "settlement"],
      "remediation": "Check the settlement ingestion pipeline for dropped records"
    }
  ]
}
```

### Notes

- This endpoint is optimized for bulk processing and is a good fit for offline reconciliation jobs.
- Use it when inspecting entire batches of transaction data or processing sample CSV payloads.

---

## Errors

### Validation Error

If the request body is invalid or missing required fields, the service returns:

- Status: `422 Unprocessable Entity`
- Content-Type: `application/json`

```json
{
  "detail": [
    {
      "loc": ["body", "payment_processor_txns"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Internal Server Error

If an unexpected error occurs during processing, the service returns:

- Status: `500 Internal Server Error`
- Content-Type: `application/json`

```json
{
  "detail": "Internal server error"
}
```

## Example Usage

### Curl Example

```bash
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{
    "payment_processor_txns": [
      {"id": "PAY-001", "amount": 100.00, "timestamp": "2026-07-03T10:00:00Z", "status": "completed"}
    ],
    "ledger_txns": [
      {"id": "LED-001", "amount": 100.00, "timestamp": "2026-07-03T10:05:00Z", "status": "recorded"}
    ],
    "settlement_txns": [
      {"id": "SET-001", "amount": 99.50, "timestamp": "2026-07-03T10:10:00Z", "status": "settled"}
    ]
  }'
```

### Python Example

```python
import requests

payload = {
    "payment_processor_txns": [
        {"id": "PAY-001", "amount": 100.00, "timestamp": "2026-07-03T10:00:00Z", "status": "completed"}
    ],
    "ledger_txns": [
        {"id": "LED-001", "amount": 100.00, "timestamp": "2026-07-03T10:05:00Z", "status": "recorded"}
    ],
    "settlement_txns": [
        {"id": "SET-001", "amount": 99.50, "timestamp": "2026-07-03T10:10:00Z", "status": "settled"}
    ]
}

response = requests.post('http://localhost:8000/diagnose', json=payload)
print(response.status_code)
print(response.json())
```
