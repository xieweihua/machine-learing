# -*- coding: utf-8 -*-
from math import log


def calcShannonEnt(dataSet):
    numEnt = len(dataSet)
    labelCounts = {}

    for item in dataSet:
        currentLabel = item[-1]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key])/numEnt
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt
