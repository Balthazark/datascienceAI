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
    pov = readFile('poverty-gap-index-at-190-int-per-day-povcal.csv')
    alc = readFile('total-alcohol-consumption-per-capita-litres-of-pure-alcohol.csv')
    pov = makeDict(pov)
    alc = makeDict(alc)

    result = []
    for key in alc:
        if key in pov:
            result.append([key,pov[key],alc[key]])
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
        header =['Country','Poverty','Alcohol consumption']
        writer.writerow(header)
                
        for row in l:
            writer.writerow(row)

#writeToCSV(dataCollector(),'povVSAlcAll.csv')


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

writeToCSV(getLatest(),'povVsAlcLatest.csv')
