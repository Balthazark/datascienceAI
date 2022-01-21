import numpy as np
import csv
import pandas as pd

def readFile(f):
    with open(f) as file:
        result = []
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
    return result


def dataCollector():
    curr = readFile('corruption-perception-index.csv')
    gini = readFile('gini-index.csv')
    gini = makeDict(gini)
    curr = makeDict(curr)

    result = []
    for key in curr:
        if key in gini:
            result.append([key,curr[key],gini[key]])
    return result

def makeDict(l):
    l.pop(0)
    result = {}
    for rows in l:
        result[rows[0] + rows[2]] = rows[3]
    return result

def writeToCSV(l,fileName):
    with open(fileName,'w') as file:
        writer = csv.writer(file)
        header =['Country','Curruption','Gini']
        writer.writerow(header)
                
        for row in l:
            writer.writerow(row)

#writeToCSV(dataCollector(),'currGiniAll.csv')


def getLatest():
    rows = dataCollector()
    result = []
    tmp=[""]
    slicer = slice(-4)
    for row in reversed(rows):
        if row[0][slicer] != tmp:
            result.insert(0,row)
            tmp = row[0][slicer]
    return result

writeToCSV(getLatest(),'currGiniLatest.csv')