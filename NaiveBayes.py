import json
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import math

def trainData(): #This function opens, organizes and closes our custom dataset
    f = open("data.json")
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
    
    priorProb = {intent: count / len(inputs) for intent, count in labelCounts.items()} #finds the probability of a word being one of the intents


    wordsPerCount = {intent: Counter() for intent in set(labels)}#Makes a dictonary showing how many times words repeat themselves per intent
    for i in range(len(inputs)):
        intent = labels[i]
        words = inputs[i].split()
        wordsPerCount[intent].update(words)
    uniqueWords = set()

    uniqueWords = set(word for sentence in inputs for word in sentence.split()) #makes a set of all unique words
    vocabSize = len(uniqueWords) #Gets the vocab size

    likelyhood = {}
    for intents, wordCount in wordsPerCount.items():#Finds the total sum of words per intent
         totalWords = sum(wordsPerCount[intents].values())
         likelyhood[intents] = {
             word : (wordCount[word] + 1) / (totalWords + vocabSize) for word in uniqueWords
         }
    
    return priorProb, likelyhood

def classify(sentence, priorProb, likelyhood):
    words = sentence.lower().translate(str.maketrans("","",string.punctuation))
    scores = {}
    for intent in priorProb:
        logProb = math.log(priorProb[intent])
        for word in words:
            if word in likelyhood:
                logProb += math.log(likelyhood[intent][word])
        scores[intent] = logProb
    return max(scores, key=scores.get)
   
def main():
    inputs, labels = trainData()
    inputs = processText(inputs)
    priorProb, likelyhood = naiveBayes(inputs, labels)
    testSentence = "Hey! how are you doing?"
    prediction = classify(testSentence, priorProb, likelyhood)
    print(f"Predicted intent for {testSentence}: {prediction}")


    return




if __name__ == "__main__":
    main()