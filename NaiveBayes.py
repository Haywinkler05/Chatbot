import json
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import math
import random


def responseData():
    f = open("responses.json")
    dataset = json.load(f)
    f.close()
    return dataset["intents"]
def trainData(): #This function opens, organizes and closes our custom dataset
    f = open("intents.json")
    dataset = json.load(f)
    inputs = []
    labels = []
    for i in dataset:
        for ex in i["examples"]:
            inputs.append(ex)
            labels.append(i["intent"])
    
    f.close()

    return inputs, labels 


def processText(inputs): #This cleans up the words from the text by making it all lower case and removing punctuation
    for i in range(len(inputs)):
        modify = inputs[i]
        modify = modify.lower()
        modify = modify.translate(str.maketrans("","", string.punctuation))
        inputs[i] = modify
    return inputs




def naiveBayes( inputs, labels):
    labelCounts = Counter(labels) #This counts our labels
    
    priorProb = {intent: labelCounts[intent] / len(labels) for intent in labelCounts} #finds the probability of a word being one of the intents


    wordsPerCount = {intent: Counter() for intent in set(labels)}#Makes a dictonary showing how many times words repeat themselves per intent
    for i in range(len(inputs)):
        intent = labels[i]
        words = inputs[i].split()
        wordsPerCount[intent].update(words)
    uniqueWords = set()

    uniqueWords = set(word for sentence in inputs for word in sentence.split()) #makes a set of all unique words
    vocabSize = len(uniqueWords) #Gets the vocab size

    likelyhood = {}
    for intents, wordCount in wordsPerCount.items():#Finds the total sum of words per intent and does lapace smoothing to handle words not accounted for
         totalWords = sum(wordsPerCount[intents].values())
         likelyhood[intents] = {
             word : (wordCount[word] + 1) / (totalWords + vocabSize) for word in uniqueWords
         }
    
    return priorProb, likelyhood

def classify(sentence, priorProb, likelyhood):
    wordLog = 0
    words = sentence.lower().translate(str.maketrans("","",string.punctuation)).split() #Adjusts user words
    scores = {} #Creates score dictonary
    all_unique_words = set()
    for intent_likelihood in likelyhood.values():
        all_unique_words.update(intent_likelihood.keys())
    vocab_size = len(all_unique_words)

    for intent in priorProb: #Loops through the prior probability
        logProb = math.log(priorProb[intent])
        intent_word_counts = sum(list(likelyhood.get(intent, {}).values())) + vocab_size # For Laplace smoothing denominator

        for word in words:
            word_likelihood = likelyhood.get(intent, {}).get(word, 1 / intent_word_counts if intent_word_counts > 0 else 0) # Laplace smoothing for unseen words
            wordLog = math.log(word_likelihood) if word_likelihood > 0 else 0
            logProb += wordLog
        scores[intent] = logProb #Sets the intent with the probability of the word being that intent
    return max(scores, key=scores.get) #Finds the highest score and the intent with it


def generateResponses(dataset, prediction):
    for item in dataset:
        if(item["intent"] == prediction):
            responses = item.get("responses", [])
            if responses:
                return random.choice(responses)
    return
def UserQuestion():
    userInput = input("You: ").lower()
    return userInput

def run(userInput):
    inputs, labels = trainData() #Loads data
    inputs = processText(inputs)#Processes it 
    priorProb, likelyhood = naiveBayes(inputs, labels) #Calculates
    prediction = classify(userInput, priorProb, likelyhood) #Predicts
    dataset = responseData()
    print(generateResponses(dataset, prediction))

