from user import User
from chatbot import Chatbot

def GetTime():
    import datetime
    currentTime = datetime.datetime.now().strftime("%I:%M %p")
    return currentTime

def setUserClass():
    name = input("Hello! Welcome to my chatbot. Would you please input your name: ")
    user = User(name, GetTime())
    return user


def main():
    user = setUserClass()
    chat = Chatbot()
    mode = int(input("Please type 1 for rule based and 2 for Naive bayes: "))
    if(mode == 1):
        print("You choose rule based mode. Type rules for a list of commands the chatbot can make")
        while(1):
            chat.ruleBased()
            if("bye" in chat.getUserInput()):
                print("Chatbot: goodbye!")
                break
            print(chat.getResponse())
    
    


    return


if __name__ == "__main__":
    main()