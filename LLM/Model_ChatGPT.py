"""ChatGPT Module"""
from .Model_Base import LLMClass, generate_role

from openai import AzureOpenAI

class ClassChatGPT(LLMClass):
    """LLM class for ChatGPT"""
    def __init__(self, api_key, model, endpoint):
        if model == '':
            model = 'gpt-4o'
        super().__init__(api_key, model, endpoint)
        self.client = AzureOpenAI(
            api_key=self.api_key,
            api_version=self.model,
            azure_endpoint=self.endpoint
        )

    def send_request(self, prompt):
        self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": generate_role()},
                {"role": "user", "content": prompt}
            ]
        )
