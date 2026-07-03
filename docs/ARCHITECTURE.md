# Architecture & Design Decisions

## System Design Overview

┌────────────────────────────────────────────────────────────────────┐
│                         CLIENT LAYER                               │
│                    (Curl, Python SDK, UI)                          │
└────────────────────────────┬─────────────────────────────────────┘
│
┌────────────────────────────▼─────────────────────────────────────┐
│                    API LAYER (FastAPI)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │
│  │ POST/diagnose│  │GET /health   │  │POST/batch    │            │
│  └──────────────┘  └──────────────┘  └──────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
│
┌────────────────────────────▼─────────────────────────────────────┐
│              BUSINESS LOGIC LAYER                                 │
│  ┌─────────────────────┐      ┌──────────────────────┐            │
│  │ Reconciler Module   │      │ Diagnostics Module   │            │
│  ├─ Transaction Match  │      ├─ Root-Cause Engine  │            │
│  ├─ Mismatch Detection │      ├─ Confidence Score   │            │
│  └─ Gap Analysis       │      └─ Remediation Hints  │            │
│  └─────────────────────┘      └──────────────────────┘            │
└────────────────────────────┬─────────────────────────────────────┘
│
┌────────────────────────────▼─────────────────────────────────────┐
│                  DATA LAYER (SQLite)                              │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Transactions   │  │ Reconciliation │  │ Diagnostics    │      │
│  │ Table          │  │ Results        │  │ Cache          │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────┬─────────────────────────────────────┘
│
┌────────────────────────────▼─────────────────────────────────────┐
│              SIMULATOR LAYER (Mock Data)                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐      │
│  │ Payment Proc   │  │ Ledger System  │  │ Settlement Sys │      │
│  │ Simulator      │  │ Simulator      │  │ Simulator      │      │
│  └────────────────┘  └────────────────┘  └────────────────┘      │
└────────────────────────────────────────────────────────────────────┘

markdown

## Technology Choices

### 1. **Framework: FastAPI**

**Decision:** Use FastAPI for REST API.

**Why:**
- **Lightweight** — Minimal boilerplate, ~15 LOC for a working endpoint
- **Async-ready** — Built-in async/await support for concurrent requests
- **Auto-documentation** — Swagger UI at `/docs` (impresses recruiters)
- **Type hints** — Built-in validation via Pydantic models
- **Low overhead** — Deployable on 0.5 CPU free tier
- **FDE relevant** — Debugging async code is a real-world FDE skill

**Alternative considered:** Flask (simpler but less feature-rich); Django (overkill for this scope).

---

### 2. **Database: SQLite**

**Decision:** Use SQLite for data persistence.

**Why:**
- **Zero setup** — File-based, no external DB server required
- **Zero cost** — Included with Python
- **Sufficient for POC** — Perfect for reconciliation datasets (millions of rows still queryable)
- **Deployable** — Single `.db` file can ship with Docker container
- **FDE mindset** — Shows you can work without cloud infrastructure

**Schema trade-off:** No horizontal scaling (not needed for demo).

**Alternative considered:** PostgreSQL (overkill); MongoDB (unnecessary for structured txn data).

---

### 3. **Language: Python**

**Decision:** Build in Python.

**Why:**
- **Fast iteration** — Write logic in 10 lines vs 30 in Java
- **Data science libraries** — Pandas for transaction analysis if needed
- **FDE friendly** — Debugging is simpler; clear error messages
- **Broad ecosystem** — FastAPI, SQLAlchemy, pytest all battle-tested

---

### 4. **Containerization: Docker**

**Decision:** Containerize with Docker.

**Why:**
- **Portability** — Runs identically on Windows, Mac, Linux, cloud
- **Deployment** — Ship entire environment (code + dependencies)
- **Resume value** — Docker is FDE requirement at most companies
- **Free tier ready** — Render.com, Railway.app accept Docker images

---

## Core Modules

### **simulator.py**
Generates mock transaction data with realistic mismatches.

**Responsibilities:**
- Create 3 systems' transaction logs with synthetic divergences
- Simulate timing lags, duplicates, amount mismatches, missing transactions
- Return JSON-serializable transaction objects

**Design:**
```python
class TransactionSimulator:
    def generate_matching_transactions(count: int)
    def inject_timing_lag(txns, lag_ms)
    def inject_duplicate(txns, duplicate_id)
    def inject_amount_mismatch(txns, system_id, variance)
    def get_sample_scenario(scenario_name: str)
reconciler.py
Matches transactions across 3 systems and identifies divergences.

Responsibilities:

Match transactions by ID across systems
Detect missing transactions (System A has it, B doesn't)
Identify timing lag between systems
Flag amount mismatches
Design:

python
class TransactionReconciler:
    def match_transactions(payment_txns, ledger_txns, settlement_txns)
    def find_mismatches() -> List[Mismatch]
    def calculate_match_confidence(txn1, txn2) -> float
Matching logic:

Primary: Match by transaction_id
Secondary: Match by (amount, timestamp_window, status) if ID missing
Confidence scoring: How certain is the match?
diagnostics.py
Analyzes mismatches and suggests root causes.

Responsibilities:

Categorize mismatch type (timing lag, duplicate, amount, missing)
Suggest root cause with confidence score
Recommend remediation steps
Provide actionable debugging hints
Design:

python
class DiagnosticEngine:
    def diagnose_mismatch(mismatch: Mismatch) -> Diagnosis
    def suggest_root_cause(mismatch) -> (cause, confidence)
    def recommend_remediation(cause) -> str
Diagnosis categories:

Timing Lag — Transaction exists in all systems but at different times

Confidence: High if lag is consistent, medium if irregular
Remediation: "Check async processing queue" or "Network latency?"
Missing Transaction — Exists in System A but not in B/C

Confidence: High if APIs are healthy
Remediation: "Check settlement batch job logs"
Duplicate Transaction — Same ID appears twice in one system

Confidence: High
Remediation: "Idempotency key missing? Check API retry logic"
Amount Mismatch — Same transaction, different amounts

Confidence: Medium (could be rounding, fees, or corruption)
Remediation: "Investigate exchange rate or fee calculation"
Data Corruption — Amount/timestamp invalid in one system

Confidence: High if data fails validation
Remediation: "Check data pipeline; possible DB corruption"
api.py
FastAPI application exposing reconciliation as REST endpoints.

Endpoints:

GET /health
Response: {"status": "healthy", "timestamp": "2026-07-03T10:00:00Z"}
Purpose: Liveness check for deployment monitoring
POST /diagnose
Input: JSON with transaction arrays (payment_processor_txns, ledger_txns, settlement_txns)
Output: JSON with matches, mismatches, detailed diagnostics
Logic: Calls reconciler → diagnostics engine → formats response
POST /batch-diagnose
Input: CSV file with transaction data
Output: JSON diagnostics for entire batch
Purpose: Handle large datasets
Data Flow Example
Request:

bash
Client sends 3 transaction lists to /diagnose
Step 1: Reconciler matches

vbnet
Payment: PAY-001 (\$100, 10:00)
Ledger:  LED-001 (\$100, 10:05)  → Match found, 5min lag detected
Settlement: SET-001 (\$99.50, 10:10)  → Amount mismatch
Step 2: Diagnostics analyzes

yaml
Mismatch 1: Payment vs Ledger timing lag
  → Root cause: "Async ledger processing"
  → Confidence: 0.92
  → Remediation: "Check queue depth"

Mismatch 2: Ledger vs Settlement amount
  → Root cause: "Rounding in settlement conversion"
  → Confidence: 0.88
  → Remediation: "Verify exchange rate"
Step 3: API returns

json
{
  "matches": 1,
  "mismatches": 2,
  "diagnostics": [...]
}
Deployment Architecture
Local Development
bash
Developer laptop
  ├─ venv (Python env)
  ├─ SQLite (local DB)
  ├─ FastAPI server
  └─ Test suite
Docker Container
css
Docker image
  ├─ Python 3.9
  ├─ FastAPI + dependencies
  ├─ SQLite
  └─ App code
Cloud (Free Tier)
scss
Render.com / Railway.app
  ├─ Container deployment
  ├─ Auto-scaling (if needed)
  ├─ HTTPS endpoint
  └─ Logs + monitoring
Design Patterns Used
1. Separation of Concerns
Simulator ≠ Reconciler ≠ Diagnostics ≠ API
Each module has one clear responsibility
Easy to test, debug, extend
2. Confidence Scoring
Don't just say "mismatch found"—say "95% confident it's a timing lag"
Shows probabilistic thinking (FDE skill)
Helps teams prioritize remediation
3. Scenario-Based Testing
Real cases (timing lag, duplicates, etc.) drive development
Easy to validate against production patterns
Proves you understand fintech reconciliation
4. Structured Logging
JSON logs (not plain text)
Includes context: request_id, system_affected, confidence
Deployable to ELK/Splunk
Trade-offs & Constraints
Aspect	Choice	Trade-off
Database	SQLite	No horizontal scaling (acceptable for POC)
API	Stateless	No session management (not needed)
Matching	ID-first, then heuristic	May miss obscure matches (acceptable)
Diagnostics	Rule-based	No ML (not justified for 5 scenarios)
Deployment	Free tier	Low performance (acceptable for demo)
Extensibility Roadmap
Future enhancements (not in Week 1-2 scope):

Add ML-based mismatch classification
Support more than 3 systems
Real-time streaming diagnostics
Historical trend analysis
API rate limiting & authentication
FDE Skills Demonstrated
✅ System Integration — Matching across 3 disparate systems

✅ Debugging — Root-cause analysis with confidence scoring

✅ Constraints — Zero budget, mock data only

✅ Scalability thinking — Designed for large datasets

✅ Production-ready — Docker, logging, health checks

✅ Documentation — API specs, decision records, deployment guides

