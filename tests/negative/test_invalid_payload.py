import pytest
from src.desci.orchestrator import DeSciOrchestrator

def test_missing_required_fields():
    orchestrator = DeSciOrchestrator()

    payload = {
        "study_id": "STUDY-003"
    }

    with pytest.raises(ValueError):
        orchestrator.submit_study(payload)
