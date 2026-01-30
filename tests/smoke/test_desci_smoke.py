from src.desci.orchestrator import DeSciOrchestrator

def test_desci_submission_success():
    orchestrator = DeSciOrchestrator()

    payload = {
        "study_id": "STUDY-001",
        "researcher": "Researcher A",
        "protocol": "EEG-analysis",
        "ethics": True
    }

    result = orchestrator.submit_study(payload)

    assert result["status"] == "accepted"
    assert result["study_id"] == "STUDY-001"
