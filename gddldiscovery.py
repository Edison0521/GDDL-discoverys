from Utilities import Pair, Graph
import pandas as pd
import difflib
import numpy

def is_nan(nan):
    return nan != nan

def attributes(filename,n):
    datas = pd.read_csv(filename,usecols=[n])
    return datas[n].tolist()

def splitstr(s: str):
    temp1 = []
    for litter in s:
        temp1.append(litter)
    return temp1


def similars(sigma : float,l1,l2):
    t = l1
    #print(l1,l2)
    if type(l1) and type(l2) == float :
        m = abs(l1 - l2)
        if m <= sigma:
            return True
    if type(t) and type(l2) == str:
        temp0 = splitstr(l1)
        temp1 = splitstr(l2)
        if len(temp0) > len(temp1):
            tempA = temp0
            tempB = temp1
        else:
            tempA = temp1
            tempB = temp0

        for i in range(len(tempB)):
            if tempB[i] in tempA:
                tempA.remove(tempB[i])

        if len(tempA) <= sigma:
            return True

'''
def appro(l: list):
    L = []
    P = []
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and i < j:
                if l[i] == l[j]:  
                    temp = []
                    temp.append(i)
                    temp.append(j)
                    L.append(temp)
    return L

'''


def createRHS(pairlist: list):
    l = []
    for i in range(len(pairlist)):
        l.append(pairlist[i].pairlist)
    return l

def getAttrbutes(filename: str):
    attrs = pd.read_csv(filename, header=None)
    sx = []
    df = pd.DataFrame(attrs)
    for i in range(1, len(df.loc[0]) - 1):
        sx.append(df.loc[0][i])
    return sx
'''

def finddep(graph: Graph):
    tempL = []
    tempL4 = []

    G = graph
   
    k = 0
    for i in range(len(G.nodes)):
        for j in range(len(G.node_attributes[0])):
             print(G.nodes[i].attribute[j])
    
    ss = string_similar(G.nodes[0].attribute[0],G.nodes[1].attribute[0])
    print(G.nodes[1].attribute[0],G.nodes[2].attribute[0])
    print(ss)
   
    b = list(zip(*G.node_attributes))
    for i in range(len(b)):
        for j in range(len(b[i])):
            for n in range(len(b[i])):
                if n > j:
                    if is_nan(b[i][j])== False:
                        if is_nan(b[i][n]) == False:
                            if similars(0.0, b[i][j], b[i][n]):
                                tempL3 = []
                                tempL3.append(j+1)
                                tempL3.append(n+1)
                                tempL4.append(tempL3)
                                print(tempL4,i,j,n)



    #print(tempL)
'''
def addthresord(title: list):
    list = []
    for i in range(len(title)):
        temp = []
        print("Please enter how many segments you want to divide the " + title[i] + " into:")
        m = int(input())
        for j in range(0, m):
            print("Please enter the allowed range：")
            sigma = float(input())
            temp.append(sigma)
        list.append(temp)
    print(list)
    return list


def additems(k:int,sigma,l:list):
    temp = []
    #k = 1
    for i in range(len(l)):
        for j in range(len(l)):
            if i < j:
                if is_nan(l[i]) ==False:
                    if is_nan(l[j]) ==False:
                        if similars(sigma, l[i], l[j]):
                            templ = []
                            templ.append(i+1)
                            templ.append(j+1)
                            temp.append(templ)

    if len(temp) < k:
        return []
    return temp
