from .Model_ChatGPT import Class_ChatGPT
from .Model_Gemini import Class_Gemni

def create_instance(use_GPT, API_KEY):
	if use_GPT:
		instance = Class_ChatGPT(API_KEY)
	else:
		instance = Class_Gemni(API_KEY)
	return instance
