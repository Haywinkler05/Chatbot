import json
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

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


def featureExtract(inputs, labels): #This is vectorizing all our words
    vectorizor = TfidfVectorizer()

    X = vectorizor.fit_transform(inputs)

    

    return X, inputs, labels

def naiveBayes(X, inputs, labels):
    labelCounts = Counter(labels) #This counts our labels
    
    priorProb = {intent: count / len(inputs) for intent, count in labelCounts.items()} #finds the probability of a word being one of the intents


    wordsPerCount = {intent: Counter() for intent in set(labels)}#Makes a dictonary showing how many times words repeat themselves per intent
    for i in range(len(inputs)):
        intent = labels[i]
        words = inputs[i].split()
        wordsPerCount[intent].update(words)
    uniqueWords = set()

    for j in wordsPerCount.keys():#Finds the total sum of words per intent
         totalWords = sum(wordsPerCount[j].values())
         print(f"{j} : {totalWords}")
    
    for sentence in range(len(inputs)): #Loops through and gets all unique words
        unique = inputs[sentence].split()
        for word in unique:
            uniqueWords.add(word)
    print(uniqueWords)
    return 


def main():
    inputs, labels = trainData()
    inputs = processText(inputs)
    X, inputs, labels = featureExtract(inputs, labels)
    naiveBayes(X, inputs, labels)


    return




if __name__ == "__main__":
    main()