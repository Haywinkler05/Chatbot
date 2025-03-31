class User: #This is a user class to store information about the user for the bot to use
    def __init__(self, name, time, lat, long):
        self.name = name
        self.time = time
        self.lat = lat
        self.long = long


    def setName(self, name):
        self.name = name

        
    def setTime(self, time):
        self.time = time


    def getName(self):
        return self.name
    

    def getTime(self):
        return self.time 
    
    def getLocation(self):
        return self.lat, self.long