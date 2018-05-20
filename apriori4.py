# _*_ coding:utf-8 _*_

def loadDataSet():
    return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

"""
���ɵ�����Ʒ����б�
"""
def creatC1(dataSet):
    C1 = []
    for transation in dataSet:
        for item in transation:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    #frozensetһ�����������޸�
    return map(frozenset,C1)

"""
ɨ�轻�׼�¼
���������׼�¼D,����Ϊk������б���С֧�ֶ�
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
����k����Ʒ����б�
����������ΪK-1���������б��������б�Ԫ�صĳ���K
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
            if L1 == L2: #��ǰK-2��һ����ϲ�����һ����СΪK��������
                retList.append(Lk[i] | Lk[j])
    return retList
"""
ִ��Apriori�㷨
����:���ݼ�����С֧�ֶ�
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
���ɹ�������
������Ƶ����б�Ƶ���֧�����ݵ��ֵ䣬��С���Ŷ�
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
�������Ŀ��Ŷ��Լ��ҵ�������С���Ŷ�Ҫ��Ĺ���
������Ƶ��������й�������Ԫ���б�
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
�ӳ�ʼ����ɸ���Ĺ�������
������Ƶ��������й�������Ԫ���б�
"""
def rulesFromConseq(freqSet,H,supportData,br1,minConf = 0.7):
    m = len(H[0])
    if len(freqSet) > (m+1):
        Hmp1 = aprioriGen(H,m+1)
        Hmp1 = calcConf(freqSet,Hmp1,supportData,br1,minConf)
        if len(Hmp1) > 1:
            rulesFromConseq(freqSet,Hmp1,supportData,br1,minConf)