class ResearchRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, research: dict) -> dict:
        required = {"research_id", "title", "domain", "status"}
        missing = required - research.keys()
        if missing:
            raise ValueError(f"Missing fields: {missing}")

        self._registry[research["research_id"]] = research
        return {"status": "registered", "id": research["research_id"]}

    def get(self, research_id: str) -> dict:
        return self._registry.get(research_id, {})

