import json
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

def trainData():
    f = open("data.json")
    dataset = json.load(f)
    inputs = []
    labels = []
    for i in dataset:
        for ex in i["examples"]:
            inputs.append(ex)
            labels.append(i["intent"])
    
    

    return inputs, labels


def processText(inputs):
    for i in range(len(inputs)):
        modify = inputs[i]
        modify = modify.lower()
        modify = modify.translate(str.maketrans("","", string.punctuation))
        inputs[i] = modify
    return inputs


def featureExtract(inputs, labels):
    vectorizor = TfidfVectorizer()

    X = vectorizor.fit_transform(inputs)

    

    return X, inputs, labels

def naiveBayes(X, inputs, labels):
    labelCounts = Counter(labels)
    
    priorProb = {intent: count / len(inputs) for intent, count in labelCounts.items()}

    for intent, prob in priorProb.items():
        print(f"Prior prob for {intent}: {prob}")

    return 


def main():
    inputs, labels = trainData()
    inputs = processText(inputs)
    X, inputs, labels = featureExtract(inputs, labels)
    naiveBayes(X, inputs, labels)


    return




if __name__ == "__main__":
    main()