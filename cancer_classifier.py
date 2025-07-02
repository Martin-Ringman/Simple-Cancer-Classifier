# Breast Cancer Classifier

# List of attribute names used as dictionary keys throughout the program
attributeList = [
    "ID", "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave", "symmetry", "fractal", "class"
]

def makeTrainingSet(filename):
    """
    Reads training data from a file and returns a list of patient records.
    Each record is a dictionary with keys from attributeList.
    """
    trainingSet = []
    for line in open(filename, 'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        record = {}
        for i in range(len(attributeList)):
            if i == 11:  # class label (M or B)
                record[attributeList[i]] = linelist[31].strip()
            else:
                record[attributeList[i]] = float(linelist[i])
        trainingSet.append(record)
    return trainingSet

def makeTestSet(filename):
    """
    Reads test data from a file and returns a list of patient records.
    Each record includes an additional 'prediction' key initialized to 'none'.
    """
    testset = makeTrainingSet(filename)
    for record in testset:
        record["prediction"] = "none"
    return testset

def trainClassifier(trainingSet):
    """
    Trains a simple classifier using the training set.
    Returns a dictionary of threshold values for each attribute, calculated as
    the midpoint between the average values for benign and malignant tumors.
    """
    localClassifier = {}
    benignDict = {}
    maligDict = {}
    maligCount = 0
    benignCount = 0

    for item in attributeList:
        if item != "ID" and item != "class":
            localClassifier[item] = 0
            maligDict[item] = 0
            benignDict[item] = 0

    for record in trainingSet:
        if record["class"] == "M":
            for attribute in maligDict:
                maligDict[attribute] += record[attribute]
            maligCount += 1
        else:
            for attribute in benignDict:
                benignDict[attribute] += record[attribute]
            benignCount += 1

    for attribute in benignDict:
        benignDict[attribute] = benignDict[attribute] / benignCount
    for attribute in maligDict:
        maligDict[attribute] = maligDict[attribute] / maligCount

    for attribute in localClassifier:
        localClassifier[attribute] = (benignDict[attribute] + maligDict[attribute]) / 2

    return localClassifier

def classifyTestRecords(testSet, classifier):
    """
    Classifies each record in the test set using the trained classifier.
    Sets the 'prediction' key to 'M' if 5 or more attributes are above the
    threshold, otherwise sets it to 'B'.
    """
    for record in testSet:
        maligVote = 0
        for attribute in classifier:
            if record[attribute] >= classifier[attribute]:
                maligVote += 1
        if maligVote >= 5:
            record["prediction"] = "M"
        else:
            record["prediction"] = "B"

def reportAccuracy(testSet):
    """
    Prints the accuracy of the classifier based on the test set.
    """
    correct = 0
    checked = 0
    for record in testSet:
        checked += 1
        if record["class"] == record["prediction"]:
            correct += 1
    accuracy = correct / checked
    print("The accuracy of the classifier is", accuracy, "percent")

# Main
print("Reading in training data...")
trainingFile = "cancerTrainingData.txt"
trainingSet = makeTrainingSet(trainingFile)
print("Done reading training data.\n")

print("Training classifier...")
classifier = trainClassifier(trainingSet)
print(classifier)
print("Done training classifier.\n")

print("Reading in test data...")
testFile = "cancerTestingData.txt"
testSet = makeTestSet(testFile)
print("Done reading test data.\n")

print("Making predictions and reporting accuracy...")
classifyTestRecords(testSet, classifier)
reportAccuracy(testSet)
print("Done.\n")
