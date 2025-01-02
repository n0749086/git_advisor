class BaseClass:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def __str__(self):
        return f"<{type(self).__name__}(API_KEY={self.API_KEY})>"

class Class_ChatGPT(BaseClass):
	pass

class Class_Gemni(BaseClass):
	pass
 
def create_instance(use_GPT, API_KEY):
 	if use_GPT:
 		instance = Class_ChatGPT(API_KEY)
 	else:
 		instance = Class_Gemni(API_KEY)
 	return instance
