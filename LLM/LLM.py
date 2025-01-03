from .Model_ChatGPT import ClassChatGPT
from .Model_Gemini import ClassGemini

def create_instance(use_gpt, api_key):
    """factory method for LLM Class"""
    if use_gpt:
        instance = ClassChatGPT(api_key)
    else:
        instance = ClassGemini(api_key)
    return instance
