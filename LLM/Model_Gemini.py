import google.generativeai as genai

from .Model_Base import LLMClass, generate_role

class ClassGemini(LLMClass):
    """LLM class for Gemini"""
    def __init__(self, api_key):
        super().__init__(api_key)
        genai.configure(api_key=self.api_key)
        role = generate_role()
        self.model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=role)

    def send_request(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
