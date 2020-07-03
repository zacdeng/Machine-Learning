import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
Y = iris.target

for i in Y:
    if i==0:
        x=X[Y==0,0]
        y=X[Y==0,1]
        plt.scatter(x,y,color='b')
    if i==1:
        x=X[Y==1,0]
        y=X[Y==1,1]
        plt.scatter(x,y,color='r')
    if i==2:
        x=X[Y==2,0]
        y=X[Y==2,1]
        plt.scatter(x,y,color='k')
plt.show()

for i in Y:
    if i==0:
        e1=X[Y==0,0]*X[Y==0,1]
        b1=X[Y==0,2]*X[Y==0,3]
    if i==1:
        e2=X[Y==1,0]*X[Y==0,1]
        b2=X[Y==1,2]*X[Y==0,3]
    if i==2:
        e3=X[Y==2,0]*X[Y==0,1]
        b3=X[Y==2,2]*X[Y==0,3]

plt.scatter(e3,b3,color='k',label='Virginica')
plt.scatter(e2,b2,color='r',label='Versicolour')
plt.scatter(e1,b1,color='b',label='Setosa')
plt.xlabel('花萼')
plt.ylabel('花瓣')
plt.legend()
plt.title('1702班 邓志豪20173878')
plt.show()