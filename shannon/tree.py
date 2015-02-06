# -*- coding: utf-8 -*-
import shannon

# dataSet: 待划分的数据集
# axis: 数据集特征
# value: 特征的返回值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for vec in dataSet:
        if vec[axis] == value:
            reduceVec = vec[:axis]
            reduceVec.extend(vec[axis+1:])
            retDataSet.append(reduceVec)
    return retDataSet

def chooseBestFeature(dataSet):
    newFeature = len(dataSet[0]) - 1
    baseEntroy = shannon.calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    
