import pytest
from src.desci.orchestrator import DeSciOrchestrator

def test_ethics_rejection():
    orchestrator = DeSciOrchestrator()

    payload = {
        "study_id": "STUDY-002",
        "researcher": "Researcher B",
        "protocol": "fMRI",
        "ethics": False
    }

    with pytest.raises(PermissionError):
        orchestrator.submit_study(payload)
