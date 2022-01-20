from Utilities import Pair, Graph
import pandas as pd
import difflib
import numpy as np

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
    if type(l1) and type(l2) == float:
        m = abs(l1 - l2)
        if m <= sigma:
            return True
    if type(t) and type(l2) == str:
        temp0 = list(set(l1))
        temp1 = list(set(l2))
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
                if is_nan(l[i]) or is_nan(l[j])  ==False:
                    #if is_nan(l[j]) ==False:
                        if similars(sigma, l[i], l[j]):
                            templ = []
                            templ.append(i+1)
                            templ.append(j+1)
                            temp.append(templ)

    if len(temp) < k:
        return []
    return temp
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
def decar(l1:list,l2:list):
    decar = []
    '''
    for i in range(len(l1)):
        for j in range(len(l1)):
            if j > i:
                decar.append(Pair(l1[i],l1[j]))
    for i in range(len(l2)):
        for j in range(len(l2)):
            if j > i:
                decar.append(Pair(l2[i],l2[j]))
    '''
    for i in range(len(l1)):
        for j in range(len(l2)):
            decar.append(Pair(l1[i], l2[j]))
    return decar
def disdecar(l1:list):
    decar = []
    for i in range(len(l1)):
        for j in range(len(l1)):
            if j > i:
                decar.append(Pair(l1[i],l1[j]))

    return decar
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res
def diff(item,l2:list):
    temp = []
    for i in range(len(l2)):
        if l2[i] == []:
            temp.append(item[i])
    return temp
def detect(rhs:list,cond:list):
    '''

    :param rhs:RHS
    :param cond: The itemsets wait for detect
    :return: if whole the items are in the RHS then return
    '''
    print(type(rhs[0]))


    return cond