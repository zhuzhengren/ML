__author__ = 'bigship'

import Apriori4
#test load
dataSet = Apriori4.loadDataSet()
print dataSet
#test CreatC1
C1 = Apriori4.creatC1(dataSet)
D = map(set,dataSet)
#test ScanD
L1,supportData0 = Apriori4.ScanD(D,C1,0.5)
print L1
print supportData0
#test apriori
L,supportData = Apriori4.apriori(dataSet,0.5)
print L
#test generateRules
rules = Apriori4.generateRules(L,supportData,0.7)
print rules