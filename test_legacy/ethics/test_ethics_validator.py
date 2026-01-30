import pytest
from src.desci.ethics.ethics_validator import EthicsValidator

def test_ethics_rejection():
    validator = EthicsValidator()
    bad_research = {
        "metadata": {"summary": "AI diagnosis of heart disease"}
    }
    with pytest.raises(PermissionError):
        validator.validate(bad_research)

