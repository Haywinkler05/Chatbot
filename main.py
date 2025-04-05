from user import User
from chatbot import Chatbot
import specialResponses as sr


def setUserClass():
    name = input("Hello! Welcome to my chatbot. Would you please input your name: ")
    lat, long = sr.get_location()
    user = User(name, sr.GetTime(), lat, long)
    return user


def main():
    user = setUserClass()
    chat = Chatbot(user)
    mode = int(input("Please type 1 for rule based and 2 for Naive bayes or 3 for both options: "))
    if(mode == 1):
        print("You choose rule based mode. Type rules for a list of commands the chatbot can make")
        while(1):
            chat.ruleBased()
            if("bye" in chat.getUserInput()):
                print("Chatbot: goodbye!")
                break
            print(chat.getResponse())
    elif(mode == 2):
        print("You choose Naive Bayes mode")
        while(1):
            chat.naiveBayes()
            if("bye" in chat.getUserInput()):
                break 
    else:
        from ruleBased import responses
        while(1):
            chat.ruleBased()
            chatbotResponse = chat.getResponse()
            if("bye" in chat.getUserInput()):
                print("Chatbot: goodbye!")
                break
            if(chatbotResponse == responses["default"]):
                print("Chatbot does not understand, switching to naive bayes mode. Please retype your input")
                chat.naiveBayes()
                print("Switching back to rule based mode")
            else:
                print(chatbotResponse)
    return


if __name__ == "__main__":
    main()