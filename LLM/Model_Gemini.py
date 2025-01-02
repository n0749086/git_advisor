from .Model_Base import BaseClass

class Class_Gemni(BaseClass):
	def __init__(self, API_KEY):
		super().__init__(API_KEY)
		import google.generativeai as genai
		genai.configure(api_key=self.API_KEY)
		self.model = genai.GenerativeModel("gemini-1.5-flash")

	def send_request(self, role, prompt):
		response = self.model.generate_content(prompt)
		return response.text