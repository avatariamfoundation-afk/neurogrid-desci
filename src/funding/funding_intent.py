class FundingIntentLedger:
    def __init__(self):
        self.intents = []

    def declare(self, research_id: str, amount: int):
        self.intents.append({
            "research_id": research_id,
            "amount": amount
        })

