# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv

def readfile():
    #
    with open('life-expectancy.csv') as file:
        tmp = [""]
        result = []
        reader = csv.reader(file)
        for row in reader: 
            if row[0] != tmp[0]:
                result.append(row)
            else:
                tmp = row
        print(result) 
readfile()

# %%
