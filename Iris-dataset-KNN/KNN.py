import numpy as np

#def max_type(lt):
#    temp = 0
#    for i in lt:
#        if lt.count(i) > temp:
#            temp = lt.count(i)
#            max_type = i
#   return max_type
    
def KNN_Classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]                       #读dataSet的行数
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet     #将test_list拓展成与dataSet相同大小    
    sqDiffMat = diffMat ** 2                             #差值求平方
    sqDistances = np.sum(sqDiffMat, axis = 1)            #每行差值平方相加
    distances = sqDistances ** 0.5                       #开方
    
    Sorted_distances = np.argsort(distances)             #从小到大排序
    
#    unconfirm_labels=[]
#    for i in range(k):
#        unconfirm_label=labels[Sorted_distances[i]]
#       unconfirm_labels.append(unconfirm_label)
#    Type=max_type(unconfirm_labels)
    
 #   return Type
    classCount={}
    for i in range(k):
        voteLabel=labels[Sorted_distances[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1
    maxCount=0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount=value
            maxIndex=key
    return maxIndex