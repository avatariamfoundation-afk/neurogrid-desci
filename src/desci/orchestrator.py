class DeSciOrchestrator:
    REQUIRED_FIELDS = {"study_id", "researcher", "protocol", "ethics"}

    def submit_study(self, payload: dict) -> dict:
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")

        missing = self.REQUIRED_FIELDS - payload.keys()
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

        if payload.get("ethics") is not True:
            raise PermissionError("Ethics approval required")

        return {
            "status": "accepted",
            "study_id": payload["study_id"]
        }

