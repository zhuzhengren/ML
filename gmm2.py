# _*_ coding:utf-8 _*_
import numpy as np

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return np.array(dataMat),labelMat


#�����˹����
def Gaussian(data,mean,cov):
    dim = np.shape(cov)[0]   # ����ά��
    covdet = np.linalg.det(cov) # ����|cov|
    covinv = np.linalg.inv(cov) # ����cov����
    if covdet==0:              # �Է�����ʽΪ0
        covdet = np.linalg.det(cov+np.eye(dim)*0.01)
        covinv = np.linalg.inv(cov+np.eye(dim)*0.01)
    m = data - mean
    z = -0.5 * np.dot(np.dot(m, covinv),m)    # ����exp()���ֵ
    return 1.0/(np.power(np.power(2*np.pi,dim)*abs(covdet),0.5))*np.exp(z)  # ���ظ����ܶ�ֵ

# �����жϳ�ʼ������е�means�Ƿ������ñȽϽ�
def isdistance(means,criterion=0.03):
     K=len(means)
     for i in range(K):
         for j in range(i+1,K):
             if criterion>np.linalg.norm(means[i]-means[j]):
                 return False
     return True

# ��ȡ����ľ�������
def GetInitialMeans(data,K,criterion):
    dim = data.shape[1]  # ���ݵ�ά��
    means = [[] for k in range(K)] # �洢��ֵ
    minmax=[]
    for i in range(dim):
        minmax.append(np.array([min(data[:,i]),max(data[:,i])]))  # �洢ÿһά�������Сֵ
    minmax=np.array(minmax)
    while True:
        for i in range(K):
            means[i]=[]
            for j in range(dim):
                 means[i].append(np.random.random()*(minmax[i][1]-minmax[i][0])+minmax[i][0] ) #�������means
            means[i]=np.array(means[i])
        if isdistance(means,criterion):
            break
    return means

# K��ֵ�㷨�����ƴ�Լ������������һ��GMM
def Kmeans(data,K):
    N = data.shape[0]  # ��������
    dim = data.shape[1]  # ����ά��
    means = GetInitialMeans(data,K,15)
    means_old = [np.zeros(dim) for k in range(K)]
    # ��������
    while np.sum([np.linalg.norm(means_old[k] - means[k]) for k in range(K)]) > 0.01:
        means_old = cp.deepcopy(means)
        numlog = [0] * K  # �洢����ĳ��ĸ���
        sumlog = [np.zeros(dim) for k in range(K)]
        # E��
        for i in range(N):
            dislog = [np.linalg.norm(data[i]-means[k]) for k in range(K)]
            tok = dislog.index(np.min(dislog))
            numlog[tok]+=1         # ���ڸ��������������1
            sumlog[tok]+=data[i]   # �洢���ڸ��������ȡֵ

        # M��
        for k in range(K):
            means[k]=1.0 / numlog[k] * sumlog[k]
    return means

def GMM(data,K):
    N = data.shape[0]
	print "****n=",N
    dim = data.shape[1]
	print "****dim=",N
    means= Kmeans(data,K)
    convs=[0]*K
    # ��ʼ�����������data�ķ���
    for i in range(K):
        convs[i]=np.cov(data.T)
    pis = [1.0/K] * K
    gammas = [np.zeros(K) for i in range(N)]
    loglikelyhood = 0
    oldloglikelyhood = 1
    while np.abs(loglikelyhood - oldloglikelyhood) > 0.0001:
        oldloglikelyhood = loglikelyhood
        # E��
        for i in range(N):
            res = [pis[k] * Gaussian(data[i],means[k],convs[k]) for k in range(K)]
            sumres = np.sum(res)
            for k in range(K):           # gamma��ʾ��n���������ڵ�k����ϸ�˹�ĸ���
                gammas[i][k] = res[k] / sumres
        # M��
        for k in range(K):
            Nk = np.sum([gammas[n][k] for n in range(N)])  # N[k] ��ʾN���������ж������ڵ�k����˹
            pis[k] = 1.0 * Nk/N
            means[k] = (1.0/Nk)*np.sum([gammas[n][k] * data[n] for n in range(N)],axis=0)
            xdiffs = data - means[k]
            convs[k] = (1.0/ Nk)*np.sum([gammas[n][k]* xdiffs[n].reshape(dim,1) * xdiffs[n] for  n in range(N)],axis=0)
        # ���������Ȼ����
        loglikelyhood = np.sum(
            [np.log(np.sum([pis[k] * Gaussian(data[n], means[k], convs[k]) for k in range(K)])) for n in range(N)])
        print means
        print loglikelyhood