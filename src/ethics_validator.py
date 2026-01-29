class EthicsValidator:
    FORBIDDEN = {"diagnosis", "treatment", "prescription"}

    def validate(self, research: dict) -> bool:
        summary = research.get("metadata", {}).get("summary", "").lower()
        for word in self.FORBIDDEN:
            if word in summary:
                raise PermissionError("Ethics violation detected")
        return True

