from src.governance.proposal_engine import ProposalEngine

def test_proposal_flow():
    engine = ProposalEngine()
    engine.submit("P-001", "Approve synthetic ECG study")
    engine.vote("P-001", 3)
    result = engine.finalize("P-001")
    assert result["status"] == "approved"

