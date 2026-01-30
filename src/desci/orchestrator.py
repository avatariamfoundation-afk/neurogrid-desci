class DeSciOrchestrator:
<<<<<<< HEAD
    REQUIRED_FIELDS = {"study_id", "researcher", "protocol", "ethics"}

    def submit_study(self, payload: dict) -> dict:
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")

=======
    """
    DeSci submission orchestrator.
    Enforces ethics, protocol completeness, and research boundaries.
    """

    REQUIRED_FIELDS = {"study_id", "researcher", "protocol", "ethics"}

    def submit_study(self, payload: dict) -> dict:
        # ---- Type enforcement ----
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")

        # ---- Required field enforcement ----
>>>>>>> 3918530 (DeSci baseline: ethics, registry, governance green)
        missing = self.REQUIRED_FIELDS - payload.keys()
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

