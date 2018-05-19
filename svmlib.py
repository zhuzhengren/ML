# coding:utf-8 
from sklearn import svm

X = [[2,0], [1,1], [2,3]] 
y = [0,0,1] 

clf = svm.SVC(kernel ='linear')
clf.fit(X,y)  #ͨ通过 .fit 函数已经可以算出支持向量机的所有参数并保存在 clf 中   
print("clf      ",clf) 

# get support vectors 
print("support vector      ",clf.support_vectors_) 

#get index of support vectors
print("get index of support vectors     ",clf.support_)

#get number of support vectors for each class
print("get number of support vectors for each class    ",clf.n_support_)

#predict data , 参数是二维数组 
print("predict data**********",clf.predict([[2, 0], [10,10],[0,0],[1,3]])) 