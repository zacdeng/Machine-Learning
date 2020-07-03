import matplotlib.pyplot as plt
import numpy as np
import KNN

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
Y = iris.target

test_list=[]
train_list=[]
train_list_labels=[]
test_list_labels=[]

for i in range(0,len(X)):
    if i % 2 == 0:
        test_list.append(X[i])
        test_list_labels.append(Y[i])
    else:
        train_list.append(X[i])
        train_list_labels.append(Y[i])

test_list=np.array(test_list)
train_list=np.array(train_list)
num=0
for i in range(0,len(test_list)): 
    test=test_list[i]
    output=KNN.KNN_Classify(test,train_list,train_list_labels,3)
    print('Your input is: ',test ,' ,the type is: ',test_list_labels[i],' ,and the result is: ',output)
    if output==test_list_labels[i]:
        num+=1
print('The correct rate is: ' + str(num/75))