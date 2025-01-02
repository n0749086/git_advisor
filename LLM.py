from abc import ABCMeta, abstractmethod
from enum import auto, StrEnum

class Mode(StrEnum):
	COMMIT = auto()
	REVIEW = auto()

def generate_commit_message():
    """generate commit message with LLM"""
    return (
        "あなたはプログラムコードレビューの専門家です。",			# LLM:role
        "git commitメッセージをplaintext形式の日本語で作成して。メッセージは、要約、修正内容、修正によりどのように変わるのかを回答して。要約は体現止め、修正内容は特に簡潔に回答して。回答がmax_tokensを超えてしまう場合は文字数が収まるように要約してください。"			# LLM:prompt
     )

def generate_codereview():
    """code review wdith LLM"""
    return (
        "あなたはプログラムコードレビューの専門家です。",			#LLM:role
        "codeのdiffをもとに以下の観点で日本語でコードレビューして。指摘があれば改善するサンプルコードも提示して"		# LLM:prompt
        "+ バグがないかチェック"
        "+ よりコード量が少なくなる効率が良いcodeの提案"
        "+ 無駄な処理を追加していないか"
        "+ 変数やメソッドパラメーターの値がNULLや0やマイナス値でも問題がないか"
        "+ 脆弱性につながるコードがないか"
        "+ パフォーマンス改善につながる提案があるか"
        "+ 修正の目的を推測して、目的を満たしているか、より良い実現方法があれば提案して"
        "+ 回答がmax_tokensを超えてしまう場合は文字数が収まるように要約して"
        )


class BaseClass():
	def __init__(self, API_KEY):
		self.API_KEY = API_KEY

	def __str__(self):
		return f"<{type(self).__name__}(API_KEY={self.API_KEY})>"

	@abstractmethod
	def send_request(self, role, prompt):
		pass

	def run_model(self, mode, diff):
		if mode == Mode.COMMIT:
			role, prompt = generate_commit_message()
		else:
			role, prompt = generate_codereview()
		prompt = prompt + f"#diff: {diff}"
		return self.send_request(role, prompt)


class Class_ChatGPT(BaseClass):
	pass


class Class_Gemni(BaseClass):
	def __init__(self, API_KEY):
		super().__init__(API_KEY)
		import google.generativeai as genai
		genai.configure(api_key=self.API_KEY)
		self.model = genai.GenerativeModel("gemini-1.5-flash")

	def send_request(self, role, prompt):
		response = self.model.generate_content(prompt)
		return response.text

def create_instance(use_GPT, API_KEY):
	if use_GPT:
		instance = Class_ChatGPT(API_KEY)
	else:
		instance = Class_Gemni(API_KEY)
	return instance
