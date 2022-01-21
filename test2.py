import numpy as np
import pandas as pd
from Utilities import LCPs, Item, Pair
import gddldiscovery as gd
import time
filename = 'dataset/test/1.csv'
arr = np.loadtxt(filename,dtype=np.str, delimiter=',')
#arr = pd.DataFrame(pd.read_csv(filename))
# print(arr)
title = arr[0]
sigma = [[0.0], [0.0], [0.0, 0.2], [10.0], [], [0.0], [0.0]]
#sigma = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
# print("Please enter the minimum support：")
# thresord = int(input())
thresord = 1

omiga = []

x = len(arr)
y = len(title)
ti = title[1:len(title) - 1]

eid = np.transpose(arr)[len(np.transpose(arr)) - 1][1:]
RHS = []

for i in range(len(eid)):
    for j in range(len(eid)):
        if j > i:
            if eid[i] == eid[j]:
                # Pair(i,j)
                RHS.append(Pair(i + 1, j + 1))


# print(arr[1:x-1:,1:y-1])
def buildinedx(l: list, k, sigma):
    items = []
    rindex = []
    l2 = list(set(l))
    for i in range(len(l2)):
        temp = []
        for j in range(len(l)):
            if l2[i] == l[j]:
                temp.append(j + 1)
        if len(temp) >= k:
            items.append(temp)
    for i in range(len(items)):
        if l2[i] != '':
            rindex.append(LCPs(l2[i], items[i]))
    '''        
    for i in range(len(l2)):
        for j in range(len(l2)):
            if j > i:
                if l2[i] != '':
                    if gd.similars(sigma,l2[i],l2[j]):
                        print(l2[i],l2[j])
    '''
    return rindex


def createlevel1(array, sigma, thresord):
    level1 = []
    k = thresord
    Het = np.transpose(array)
    print(Het)
    '''
    for i in range(len(sigma)):
        for j in range(len(sigma[i])):
            level1.append(Item(ti[i], sigma[i][j], buildinedx(Het[i], k ,sigma[i][j])))
    print(level1)
    
    buildinedx(Het[2], k, sigma[2][1])
    '''
    time_start = time.time()
    for i in range(len(sigma)):
        for j in range(len(sigma[i])):
            b = buildinedx(Het[i], k ,sigma[i][j])
            #print(b)
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
    return level1


createlevel1(arr[1:x:, 1:y - 1], sigma, thresord)
