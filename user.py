class User: #This is a user class to store information about the user for the bot to use
    def __init__(self, name, time):
        self.name = name
        self.time = time


    def setName(self, name):
        self.name = name

        
    def setTime(self, time):
        self.time = time


    def getName(self):
        return self.name
    

    def getTime(self):
        return self.time