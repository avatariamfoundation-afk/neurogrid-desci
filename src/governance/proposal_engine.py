class ProposalEngine:
    def __init__(self):
        self.proposals = {}

    def submit(self, proposal_id: str, description: str):
        self.proposals[proposal_id] = {
            "description": description,
            "votes": 0,
            "status": "open"
        }

    def vote(self, proposal_id: str, weight: int = 1):
        self.proposals[proposal_id]["votes"] += weight

    def finalize(self, proposal_id: str):
        p = self.proposals[proposal_id]
        p["status"] = "approved" if p["votes"] > 0 else "rejected"
        return p

