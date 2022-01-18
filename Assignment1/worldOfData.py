# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

def readfile(f):
    #
    with open(f) as file:
        result = []
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
    return result

    
lifeExp = readfile('life-expectancy.csv')
gdp = readfile('gdp-per-capita-worldbank.csv')
result = []


rowtmp = [""]
for rows in reversed(lifeExp):
    for row in reversed(gdp):
        if rows[0] == row[0] and rows[2] == row[2] and rowtmp[0] != rows[0]:
            tmp  = [rows[0],rows[3],row[3]] 
            result.append(tmp)
            rowtmp = rows
            break
print(result)
