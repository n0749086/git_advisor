"""ChatGPT Module"""
from .Model_Base import LLMClass

from openai import AzureOpenAI

class ClassChatGPT(LLMClass):
    """LLM class for ChatGPT"""
    def __init__(self, api_key, model):
        if model == '':
            model = 'gpt-4o'
        super().__init__(api_key, model)

    def send_request(self, prompt):
        pass
