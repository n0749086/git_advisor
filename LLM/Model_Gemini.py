import google.generativeai as genai

from .Model_Base import LLMClass

class ClassGemini(LLMClass):
    """LLM class for Gemini"""
    def __init__(self, api_key):
        super().__init__(api_key)
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def send_request(self, role, prompt):
        response = self.model.generate_content(prompt)
        return response.text
