import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.environ.get("API_KEY")
USE_GPT = (os.environ.get("LLM") == 'GPT')
