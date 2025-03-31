import ruleBased
import NaiveBayes

class Chatbot:
    def __init__(self, user):
        self.userInput = ""
        self.response = ""
        self.user = user

    

    def ruleBased(self):
       self.userInput = ruleBased.UserQuestion()
       self.response = ruleBased.ChatbotResponse(self.userInput)

    def naiveBayes(self):
        self.userInput = NaiveBayes.UserQuestion()
        NaiveBayes.run(self.userInput, self.user)

    def setUserInput(self, userInput):
        self.userInput = userInput

    def setResponse(self, response):
        self.response = response
    
    def getUserInput(self):
        return self.userInput
    
    def getResponse(self):
        return self.response 
    
