from app.services.ai_provider import AIProvider


class FakeAIProvider(AIProvider):
    def __init__(self, response: str):
        self.response = response
        self.last_prompt = ""

    def generate(self, prompt: str) -> str:
        self.last_prompt = prompt
        return self.response
