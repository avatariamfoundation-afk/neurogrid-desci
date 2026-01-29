from src.registry.research_registry import ResearchRegistry

def test_research_registration():
    registry = ResearchRegistry()
    research = {
        "research_id": "NG-R-001",
        "title": "Synthetic ECG Signal Analysis",
        "domain": "biomedical",
        "status": "submitted"
    }
    result = registry.register(research)
    assert result["status"] == "registered"

