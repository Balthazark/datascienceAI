# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

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

writeToCSV(getLatest(),'outputLatest.csv')