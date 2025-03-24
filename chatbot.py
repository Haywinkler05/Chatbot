import ruleBased


class chatbot:
    def __init__(self):
        self.userInput = ""
        self.response = ""

    

    def ruleBased(self):
       self.userInput = ruleBased.UserQuestion()
       self.response = ruleBased.ChatbotResponse(self.userInput)

    def setUserInput(self, userInput):
        self.userInput = userInput

    def setResponse(self, response):
        self.response = response
    
    def getUserInput(self):
        return self.userInput
    
    def getResponse(self):
        return self.response