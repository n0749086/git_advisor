import google.generativeai as genai

from .Model_Base import LLMClass, generate_role

class ClassGemini(LLMClass):
    """LLM class for Gemini"""
    def __init__(self, api_key, model):
        if model == '':
            model = 'gemini-1.5-flash'
        super().__init__(api_key, model)
        genai.configure(api_key=self.api_key)
        role = generate_role()
        self.model = genai.GenerativeModel(self.model, system_instruction=role)

    def send_request(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
