# Distributed System Health Monitor & Diagnostic Toolkit

A lightweight diagnostics toolkit that identifies transaction mismatches across payment, ledger, and settlement systems. This repository is built as a forward-deployed engineering portfolio project to demonstrate system integration, root-cause analysis, and deployable diagnostics with zero external infrastructure.

## Problem Statement

You're a forward deployed engineer at a fintech company. Three critical systems—**payment processor**, **ledger**, and **settlement**—occasionally diverge. Teams lack real-time visibility into *why* or *where* failures occur. They need a tool that:

- Identifies mismatches across distributed transaction systems
- Diagnoses root causes such as timing lag, duplicates, data corruption, and rounding issues
- Provides actionable remediation guidance
- Works in constrained, low-cost environments without backend dependencies

This project simulates production reconciliation workflows and returns diagnostic insights that help teams fix system mismatches faster.

## What This Solves

- **Mismatch detection** across multiple systems
- **Root-cause analysis** with severity and confidence scoring
- **Batch diagnosis** for large transaction sets
- **Deployability** using Docker and lightweight Python tooling
- **Observability** through structured outputs and clear remediation hints
- **FDE skills demonstration**: integration, debugging, documentation, and deployment

## Quick Start

### Prerequisites

- Python 3.9+
- Git
- Optional: Docker

### Local Setup

```bash
git clone https://github.com/YOUR_USERNAME/distributed-system-diagnostics.git
cd distributed-system-diagnostics
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
python -m uvicorn src.api:app --reload
```

The API server should start at `http://localhost:8000`.

### Verify the Server

```bash
curl http://localhost:8000/health
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
      {"id": "LED-001", "amount": 100.00, "timestamp": "2026-07-03T10:05:00Z", "status": "recorded"}
    ],
    "settlement_txns": [
      {"id": "SET-001", "amount": 99.50, "timestamp": "2026-07-03T10:10:00Z", "status": "settled"}
    ]
  }'
```

### Expected Response

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

## Architecture Overview

```text
Client -> FastAPI API -> Reconciler -> Diagnostic Engine -> Output
                           │
                           └── Simulator / SQLite data layer
```

- **API Layer**: FastAPI endpoints for `/health`, `/diagnose`, and `/batch-diagnose`
- **Reconciliation Engine**: matches transactions across systems and identifies mismatches
- **Diagnostics Engine**: categorizes causes, scores confidence, and recommends remediation
- **Simulator Layer**: generates mock transaction data for testing and scenario validation

## Repository Structure

```text
distributed-system-diagnostics/
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
│   └── test_reconciler.py
├── docker-compose.yml
├── LICENSE
├── README.md
└── requirements.txt
```

## Documentation

- `docs/ARCHITECTURE.md` — design decisions and system architecture
- `docs/API_REFERENCE.md` — API endpoint details and payload schemas
- `docs/DEPLOYMENT.md` — Docker and deployment instructions
- `docs/SCENARIOS.md` — reconciliation scenarios and expected outcomes

## Why This Project

This repository is designed to showcase skills that matter for a forward deployed engineer:

- system debugging under uncertainty
- cross-system reconciliation
- root-cause analysis and remediation guidance
- rapid prototyping with Python and FastAPI
- documentation and deployment readiness

## License

MIT License — see `LICENSE` for details.
