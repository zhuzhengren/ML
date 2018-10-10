import string
import types
import numpy as np
from numpy import *
from numpy.linalg import svd
def main():
        A=np.array([
        [1.,0.,0.,1.,1.],
        [1.,0.,1.,0.,1.],
        [0.,1.,0.,0.,0.]
       ])
        print 'A',A
        T,S,D = svd(A)
        print 'T',T
        print 'S',S
        print 'D',D
        print 'T'
        for x in T:
            print around(x,decimals=2)
        print 'S'
        for x in S:
            print around(x,decimals=2)
        print 'D'
        for x in D:
            print around(x,decimals=2)
        print '*'*100
        k=2
        S1=np.zeros(shape=(k,k))
        S1[:k,:k]=diag(S[:k])
        T=delete(T,s_[k:],axis=1)
        D=delete(D,s_[k:],axis=0)
        print 'T'
        for x in T:
            print around(x,decimals=2)
        print 'S1',S1
        print 'D'
        for x in D:
            print around(x,decimals=2)
        B=np.dot(T,np.dot(S1,D))
        print 'B',B
        for x in B:
            print around(x,decimals=2)
if __name__=='__main__':
        main()