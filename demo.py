from Utilities import LCP , Graph , gddl
import pandas as pd
import gddldiscovery as gd
import time

GL = gddl()
G = Graph()
omiga = []
filename = 'dataset/restaurant/fz.arff.csv'
title = gd.getAttrbutes(filename)
data = pd.read_csv(filename)
df = pd.DataFrame(data)
for i in range(data.shape[0]):
    row = data.loc[i]
    attr = []
    #G.addtitle(title[i])
    for j in range(0,len(title)):
        attr.append(row[title[j]])
    G.addNode(row['nodeid'],attr)
    G.add_edge(row['nodeid'],row['eid'])

temp1 = []
for i in range(len(title)):
    temp1.append(gd.attributes(filename,title[i]))
b = temp1
print(b)
#sigma = gd.addthresord(title)
level1 = []
sigma = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
#print("Please enter the minimum support：")
#thresord = int(input())
thresord = 200

for i in range(len(sigma)):
    for j in range(len(sigma[i])):
        level1.append(gd.additems(thresord,sigma[i][j],b[i]))
        print(2)
        GL.additems(title[i],sigma[i][j],gd.additems(thresord,sigma[i][j],b[i]))
    print(1)
G.add_pair()
RHS = gd.createRHS(G.pairs)  #Fun1 1
print(G.pairs)
time_start=time.time()

'''
detectitems of first level
'''

def detect(rhs:list,cond:list):
    '''

    :param rhs:RHS
    :param cond: The itemsets wait for detect
    :return: if whole the items are in the RHS then return
    '''
    c = cond.copy()
    for i in range(len(cond)):
        if cond[i] in rhs:
            c.remove(cond[i])
    if c == []:
        return c
    else:
        return cond


level_f = [] #(omiga,L(1))
for i in range(len(level1)):
    level_f.append(detect(RHS,GL.itemlists[i].item))

for i in range(len(level1)):
    if level1[i] != [] and level_f[i] == []:
        lcp = LCP(GL.itemlists[i].name+'<'+str(GL.itemlists[i].sigma),level1[i])
        omiga.append(lcp.name)

def ret(l1:list,l2:list):
    '''

    :param l1:
    :param l2:
    :return: Union of two sets
    '''
    k = len(l1)
    k2 = len(l2)
    ftemp = []
    if k >= k2:
        rtemp = l1
        r2temp = l2
    else:
        r2temp = l1
        rtemp = l2
    for i in range(len(r2temp)):
        if r2temp[i] in rtemp:
            ftemp.append(r2temp[i])
    return ftemp


def finddeps(lists,level:list):
    '''

    :param level:
    :return:
    '''
    temp = []
    for i in range(len(level)):
        for j in range(len(level)):
            if i < j:
                if lists[i].name != lists[j].name:
                    #print(ret(level[i],level[j]),i,j)
                    temp.append(ret(level[i],level[j]))
    return temp

def diff(item,l2:list):
    temp = []
    for i in range(len(l2)):
        if l2[i] == []:
            temp.append(item[i])
    return temp

candlevel = []

for i in range(len(level_f)):
        item = LCP(GL.itemlists[i].name+'<'+str(GL.itemlists[i].sigma),level_f[i])
        candlevel.append(item)

def findDEEP(items:LCP):
    temp = []
    if len(items) != 1:
        for i in range(len(items)):
            for j in range(len(items)):
                if i < j:
                    t1 = str(items[i].name).split('<')
                    t2 = str(items[j].name).split('<')
                    if t1[0] != t2[0]:
                        r1 = ret(items[i].items,items[j].items)
                        r2 = detect(RHS,r1)
                        if r1 != [] and r2 == []:
                            lcp = LCP(items[i].name + items[j].name, r1)
                            omiga.append(lcp.name)
                        if r2 != []:
                            item = LCP(items[i].name+items[j].name,r2)
                            temp.append(item.name)
    if len(items) != 1:
        return temp


f = findDEEP(candlevel)

print("The last items：")
print(f)
time_end=time.time()
print('time cost',time_end-time_start,'s')
print("The output of discovery：")
print(omiga)
time_end=time.time()
print('time cost',time_end-time_start,'s')