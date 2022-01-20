import math
from Utilities import LCPs, Item, Pair
from Utilities import LCP , Graph , gddl
import pandas as pd
import gddldiscovery as gd
import time

#arr = np.loadtxt(filename,dtype=np.str, delimiter=',')
#arr = pd.DataFrame(pd.read_csv(filename))
#print(arr.loc[0])
'''
title = arr[0]
sigma = [[0.0], [0.0], [0.0, 0.2], [10.0], [], [0.0], [0.0]]
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
    for i in range(len(l2)):
        for j in range(len(l2)):
            if j > i:
                if l2[i] != '':
                    if gd.similars(sigma,l2[i],l2[j]):
                        print(l2[i],l2[j])
    print(type(l2[0]))
    return rindex


def createlevel1(array, sigma, thresord):
    level1 = []
    k = thresord
    Het = np.transpose(array)

    for i in range(len(sigma)):
        for j in range(len(sigma[i])):
            level1.append(Item(ti[i], sigma[i][j], buildinedx(Het[i], k ,sigma[i][j])))
    print(level1)

    buildinedx(Het[2], k, sigma[2][1])


    return level1
    '''
'''
createlevel1(arr[1:x:, 1:y - 1], sigma, thresord)
'''


GL = gddl()
G = Graph()
omiga = []
filename = 'dataset/test/1.csv'
title = gd.getAttrbutes(filename)
data = pd.read_csv(filename)
df = pd.DataFrame(data)
arr = df.drop(columns = ['nodeid','eid']).T.values.tolist()

sigma = [[0.0], [0.0], [0.0, 0.2], [10.0], [], [0.0], [0.0]]
#sigma = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
# print("Please enter the minimum support：")
# thresord = int(input())
thresord = 1
eid = df['eid']

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
    preallitems = []
    allitems = []
    l2 = list(set(l))
    l2 = [x for x in l2 if gd.is_nan(x) == False]
    for i in range(len(l2)):
        temp = []
        for j in range(len(l)):
            if l2[i] == l[j]:
                if gd.is_nan(l2[i]) == False:
                    #print(l2[i])
                    temp.append(j + 1)
        if len(temp) >= k:
            items.append(temp)
        if gd.is_nan(l2[i]) == False:
            rindex.append(LCPs(l2[i], items[i]))
    for i in range(len(l2)):
        for j in range(len(l2)):
            if j > i:
                if gd.is_nan(l2[i]) == False:
                    if gd.similars(sigma, l2[i], l2[j]):
                        preallitems.append(gd.decar(items[i], items[j]))
                        k = 0
    for i in range(len(items)):
        preallitems.append(gd.disdecar(items[i]))
    allitems = gd.flat(preallitems)
    #print(allitems)

    return allitems


def createlevel1(array, sigma, thresord):
    #time_start = time.time()
    level1 = []
    k = thresord
    Het = array

    for i in range(len(sigma)):
        for j in range(len(sigma[i])):
            b = buildinedx(Het[i], k ,sigma[i][j])
            #print(b)
            level1.append(Item(title[i],sigma[i][j],b))

    #print(level1)
    #buildinedx(Het[0],k,sigma=0)
    #time_end = time.time()
    #print('time cost', time_end - time_start, 's')
    return level1


level1 = createlevel1(arr, sigma, thresord)
level_f = [] #(omiga,L(1))
ll = level1[0].item

gd.detect(RHS,ll)


