from user import User


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
    print(f"Current user session. Current user: {user.getName()}. Current Time: {user.getTime()}")
    


    return


if __name__ == "__main__":
    main()