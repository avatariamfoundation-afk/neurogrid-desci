class EthicsValidator:
    def validate(self, payload: dict) -> bool:
        metadata = payload.get("metadata", {})
        summary = metadata.get("summary", "").lower()

        if "ai diagnosis" in summary:
            raise PermissionError("Clinical AI research requires ethics approval")

        return True
