from Utilities import Node, Graph
import pandas as pd
from gddldiscovery import getAttrbutes
import gddldiscovery as gd


'''

G = Graph()
title = getAttrbutes('dataset/test/1.csv')
data = pd.read_csv('dataset/test/1.csv')
df = pd.DataFrame(data)
for i in range(data.shape[0]):
    row = data.loc[i]
    attr = []
    #G.addtitle(title[i])
    for j in range(0,len(title)):
        attr.append(row[title[j]])
    G.addNode(row['nodeid'],attr)
    G.add_edge(row['nodeid'],row['eid'])

G.add_pair()
#finddep(G)
#gd.addthresord(title)
RHS = gd.createRHS(G.pairs)
print(RHS)
'''
G = Graph()
title = gd.getAttrbutes('dataset/test/1.csv')
data = pd.read_csv('dataset/test/1.csv')
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
    temp1.append(gd.attributes(title[i]))
b = temp1
#sigma = addthresord(title)
level1 = []
sigma = [[0.0], [0.0], [0.0, 0.2], [10.0], [], [0.0], [0.0]]
print("请输入最小支持度：")
thresord = int(input())
for i in range(len(sigma)):
    for j in range(len(sigma[i])):
        level1.append(gd.additems(thresord,sigma[i][j],b[i]))

G.add_pair()
RHS = gd.createRHS(G.pairs)
'''
对第一层进行去冗余
'''

def detect(rhs:list,cond:list):
    c = cond.copy()
    for i in range(len(cond)):
        if cond[i] in rhs:
            c.remove(cond[i])
    if c == []:
        return c
    else:
        return cond


level_f = []
for i in range(len(level1)):
    level_f.append(detect(RHS,level1[i]))
for i in range(len(level_f)):
    for j in range(len(level_f)):
        if i < j:
            new_list = []
