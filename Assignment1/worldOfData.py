import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

def readFile(f):
    #
    with open(f) as file:
        result = []
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
    return result


def dataCollector():
    gdp = readFile('gdp-per-capita-worldbank.csv')
    lifeExp = readFile('life-expectancy.csv')
    gdp = makeDict(gdp)
    lifeExp = makeDict(lifeExp)

    result = []
    for key in gdp:
        if key in lifeExp:
            result.append([key,gdp[key],lifeExp[key]])
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
        header =['Country','GDP per capita','Life expectancy']
        writer.writerow(header)
                
        for row in l:
            writer.writerow(row)

#writeToCSV(dataCollector(),'outputAll.csv')


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

#writeToCSV(getLatest(),'outputLatest.csv')
def getStandardDiv():
    data = getLatest()

    n = len(data)
    lifeexp = [float(x[2]) for x in data]
    meanLife = sum(lifeexp)/n
    print('meanLife:',meanLife)

    #Found how to calculate this online 
    #https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/
    deviationsLife = [(x - meanLife) ** 2 for x in lifeexp]
    varianceLife = sum(deviationsLife)/n
    oneStandLife = np.sqrt(varianceLife)

    aboveMeanLife = []
    for i in range(len(data)):
        if lifeexp[i] > (meanLife + oneStandLife):
            aboveMeanLife.append(data[i][0])
    print(aboveMeanLife)

    gdp = [float(x[1]) for x in data]
    meanGdp = sum(gdp) / n
    print('meanGDP:',meanGdp)

    aboveLifeBelowGDP = []
    for i in range(len(data)):
        if lifeexp[i] > meanLife and gdp[i] < meanGdp:
            aboveLifeBelowGDP.append(data[i][0])
    
    #print('div:',deviations)
    #print('var:',variance)

getStandardDiv()