import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#From sckit wiki
def regFit():
    data = pd.read_csv('DatasetRegression.csv')
    livingArea = list(map(float,data['Living Area']))
    livingArea = np.reshape(livingArea,(-1,1))
    price = list(map(float,data['Price']))
    price = np.reshape(livingArea,(-1,1))

    print(livingArea)
    print(price)

    reg = linear_model.LinearRegression()
    reg.fit(livingArea,price)
    pricePredict = reg.predict(livingArea)

    plt.scatter(livingArea,price)
    plt.plot(livingArea,pricePredict,color='red')
    plt.show()


regFit()

