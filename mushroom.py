__author__ = 'bigship'

import Apriori

def split(str,cha):
    retList = []
    for x in str:
        if x != cha[0] and x!= cha[1]:
            retList.append(x)
    return retList
mushDataSet = []
data = open('mushroom.txt')
cha = [',','\n']
for line in data.readlines():
    mushDataSet.append(split(line,cha))
data.close()
smallDataSet = mushDataSet[:10]
print smallDataSet
L , supportData = Apriori.apriori(smallDataSet,0.7)
for item in L[4]:
    if item.intersection('e'):
        print item
result = Apriori.generateRules(L,supportData,0.85)