from datetime import datetime, timezone
from typing import Dict, List, Optional

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

from .diagnostics import diagnostics_for_payload
from .reconciler import ReconciliationPayload

app = FastAPI(
    title="Distributed System Diagnostics",
    description="A lightweight reconciliation and diagnostics engine for multi-system transaction flows.",
    version="0.1.0",
)
router = APIRouter()


class DiagnosticResponse(BaseModel):
    issue_type: str
    transaction_id: Optional[str]
    description: str
    affected_systems: List[str]
    confidence: float
    remediation: str
    details: Optional[Dict[str, str]]


class DiagnoseResponse(BaseModel):
    diagnostics: List[DiagnosticResponse]
    summary: Dict[str, int]


@router.post("/diagnose", response_model=DiagnoseResponse)
def diagnose(payload: ReconciliationPayload) -> DiagnoseResponse:
    diagnostics = diagnostics_for_payload(payload)
    summary = {
        "transaction_count": len({
            txn.id
            for txn in payload.payment_processor_txns + payload.ledger_txns + payload.settlement_txns
        }),
        "issue_count": len(diagnostics),
    }
    return {
        "diagnostics": [issue.model_dump() for issue in diagnostics],
        "summary": summary,
    }


@app.get("/health")
def health() -> Dict[str, str]:
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/")
def root() -> Dict[str, str]:
    return {"service": "distributed-system-diagnostics", "status": "ok"}


app.include_router(router)
