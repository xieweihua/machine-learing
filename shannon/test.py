# -*- coding: utf-8 -*-
import shannon
import tree


def createDataSet():
    dataSet = [
       [1, 1, 'yes'],
       [1, 1, 'yes'],
       [1, 0, 'no'],
       [0, 1, 'no'],
       [0, 1, 'no'],
    ]
    label = ['no', 'yes']
    return dataSet, label

if __name__ == '__main__':
    data, label = createDataSet()
    #print shannon.calcShannonEnt(data)
    print tree.splitDataSet(data, 0, 0)
