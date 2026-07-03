# Distributed System Health Monitor & Diagnostic Toolkit

![Python CI](https://github.com/Atharvagarud137/distributed-system-diagnostics/actions/workflows/python-ci.yml/badge.svg)

A lightweight diagnostics toolkit that identifies transaction mismatches across payment processor, ledger, and settlement systems. This repository is built as a forward-deployed engineering portfolio project to demonstrate system integration, root-cause analysis, and deployable diagnostics with minimal infrastructure.

## Problem Statement

You're a forward deployed engineer at a fintech company. Three critical systems—**payment processor**, **ledger**, and **settlement**—occasionally diverge. Teams lack real-time visibility into *why* or *where* failures occur. They need a tool that:

- Identifies mismatches across distributed transaction systems
- Diagnoses root causes such as timing lag, duplicates, data corruption, and rounding issues
- Provides actionable remediation guidance
- Works in constrained, low-cost environments without backend dependencies

## What This Solves

- **Mismatch detection** across multiple systems
- **Root-cause analysis** with severity and confidence scoring
- **Batch diagnosis** for transaction workflows
- **Deployability** using Docker and lightweight Python tooling
- **Observability** through structured output and remediation guidance
- **Portfolio showcase** for FDE skills: integration, debugging, documentation, and deployment

## Quick Start

### Prerequisites

- Python 3.11+
- Git
- Optional: Docker

### Local Setup

```bash
git clone https://github.com/Atharvagarud137/distributed-system-diagnostics.git
cd distributed-system-diagnostics
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
python -m uvicorn src.api:app --reload
```

The API server will start at `http://localhost:8000`.

### Verify the Server

```bash
curl http://localhost:8000/
```

### Example Diagnosis Request

```bash
curl -X POST http://localhost:8000/diagnose \
  -H "Content-Type: application/json" \
  -d '{
    "payment_processor_txns": [
      {"id": "PAY-001", "amount": 100.00, "timestamp": "2026-07-03T10:00:00Z", "status": "completed"}
    ],
    "ledger_txns": [
      {"id": "PAY-001", "amount": 100.00, "timestamp": "2026-07-03T10:05:00Z", "status": "recorded"}
    ],
    "settlement_txns": [
      {"id": "PAY-001", "amount": 100.00, "timestamp": "2026-07-03T10:10:00Z", "status": "settled"}
    ]
  }'
```

### Expected Response

```json
{
  "diagnostics": [
    {
      "issue_type": "timing_lag",
      "transaction_id": "PAY-001",
      "description": "Ledger recorded the transaction 5 minutes after payment processor.",
      "affected_systems": ["payment_processor", "ledger"],
      "confidence": 0.90,
      "remediation": "Review asynchronous ingestion latency and queue backpressure."
    }
  ],
  "summary": {
    "transaction_count": 1,
    "issue_count": 1
  }
}
```

## Run Tests

```bash
python -m pytest -q
```

## Architecture Overview

```text
Client -> FastAPI API -> Reconciler -> Diagnostic Engine -> Output
                           │
                           └── Simulator / Optional data layer
```

## Repository Structure

```text
distributed-system-diagnostics/
├── README.md
├── Roadmap.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   ├── DEPLOYMENT.md
│   └── SCENARIOS.md
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── diagnostics.py
│   ├── reconciler.py
│   └── simulator.py
├── tests/
│   ├── test_diagnostics.py
│   ├── test_reconciler.py
│   └── test_simulator.py
├── docker-compose.yml
├── Dockerfile
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── requirements.txt
└── LICENSE
```

## Documentation

- `docs/ARCHITECTURE.md` — design decisions and architecture
- `docs/API_REFERENCE.md` — request/response schema and endpoint details
- `docs/DEPLOYMENT.md` — Docker and deployment guidance
- `docs/SCENARIOS.md` — reconciliation scenarios and expected outputs

## License

MIT License — see `LICENSE` for details.
