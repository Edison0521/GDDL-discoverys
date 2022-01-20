from Utilities import LCP , Graph , gddl
import pandas as pd
import gddldiscovery as gd
import time


GL = gddl()
G = Graph()
omiga = []
filename = 'dataset/test/1.csv'
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
sigma = gd.addthresord(title)
level1 = []
#sigma = [[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]
#print("Please enter the minimum support：")
#thresord = int(input())
thresord = 200
def singleitems(H,k:int,sigma:list):
    m = 0

for i in range(len(sigma)):
    for j in range(len(sigma[i])):
        level1.append(gd.additems(thresord,sigma[i][j],b[i]))
        GL.additems(title[i],sigma[i][j],gd.additems(thresord,sigma[i][j],b[i]))
print(1)
G.add_pair()
RHS = gd.createRHS(G.pairs)  #Fun1 1
print(G.pairs)