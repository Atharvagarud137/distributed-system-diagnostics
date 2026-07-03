from typing import List

from .reconciler import ReconciliationPayload, ReconciliationIssue, reconcile_transactions


def diagnostics_for_payload(payload: ReconciliationPayload) -> List[ReconciliationIssue]:
    result = reconcile_transactions(payload)
    return result.issues
