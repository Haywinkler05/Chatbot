responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm doing well! How about you?",
    "goodbye": "Goodbye! Have a wonderful day!",
    "bye": "See you later! Take care!",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "thank you": "No problem! I'm here to help.",
    "what's your name": "I'm your friendly chatbot. I don't have a name, but you can call me whatever you like!",
    "how old are you": "I'm a program, so I don't have an age, but I'm always learning!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what is your purpose": "My purpose is to help answer your questions and have fun conversations!",
    "what is the weather like": "I'm not sure about the weather right now, but you can check a weather website for the latest updates!",
    "who are you": "I'm your chatbot assistant, created to help you out with anything you need!",
    "help": "I'm here to help! You can ask me about my purpose, jokes, or just have a chat with me.",
    "sorry": "No need to apologize! What can I do for you?",
    "default": "Sorry, I didn't quite understand that. Could you rephrase?"
}



def UserQuestion():
    userInput = input("You: ").lower()
    return userInput



def ChatbotResponse(userInput):
    for pattern, response in responses.items():
        if pattern in userInput:
            return response
    return responses["default"]