import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
api_key = os.environ.get("API_KEY")
use_gpt = (os.environ.get("LLM") == 'GPT')
