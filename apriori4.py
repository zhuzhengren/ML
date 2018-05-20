# _*_ coding:utf-8 _*_

def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

"""
生成单个物品的项集列表
"""
def creatC1(dataSet):
    C1 = []
    for transation in dataSet:
        for item in transation:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #frozenset一旦建立不可修改
    return map(frozenset,C1)

"""
扫描交易记录
参数：交易记录D,长度为k的项集的列表，最小支持度
"""
def ScanD(D,Ck,minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] +=1
    numItems = float(len(D))
    retList =[]
    supportData ={}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key]=support
    return retList,supportData
"""
创建k个物品的项集列表
参数：长度为K-1的数据项列表，新数据列表元素的长度K
"""
def aprioriGen(Lk,k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1,lenLk):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2: #若前K-2项一样则合并生成一个大小为K的数据项
                retList.append(Lk[i] | Lk[j])
    return retList
"""
执行Apriori算法
参数:数据集，最小支持度
"""
def apriori(dataSet,minSupport = 0.5):
    C1 = creatC1(dataSet)
    D = map(set,dataSet)
    L1 ,supportData = ScanD(D,C1,minSupport)
    L = [L1]
    k = 2
    while len(L[k-2]) > 0:
        Ck = aprioriGen(L[k-2],k)
        Lk , supk = ScanD(dataSet,Ck,minSupport)
        supportData.update(supk)
        L.append(Lk)
        k += 1
    return L,supportData
"""
生成关联规则
参数：频繁项集列表，频繁项集支持数据的字典，最小可信度
"""
def generateRules(L,supportData,minConf=0.7):
    bigRuleList =[]
    for i in range(1,len(L)):
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if i > 1:
                rulesFromConseq(freqSet,H1,supportData,bigRuleList,minConf)
            else:
                calcConf(freqSet,H1,supportData,bigRuleList,minConf)
    return bigRuleList

"""
计算规则的可信度以及找到满足最小可信度要求的规则
参数：频繁项集，现有规则后件的元素列表
"""
def calcConf(freqSet,H,supportData,br1,minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq]
        if conf >= minConf:
            print freqSet-conseq,'-->',conseq,'conf: ',conf
            br1.append((freqSet-conseq,conseq,conf))
            prunedH.append(conseq)
    return prunedH

"""
从初始项集生成更多的关联规则
参数：频繁项集，现有规则后件的元素列表
"""
def rulesFromConseq(freqSet,H,supportData,br1,minConf = 0.7):
    m = len(H[0])
    if len(freqSet) > (m+1):
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,br1,minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)