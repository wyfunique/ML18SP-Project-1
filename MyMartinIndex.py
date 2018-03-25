
# coding: utf-8

# In[99]:


import scipy.io as spio
mat = spio.loadmat("ImsAndSegs/ImsAndTruths2092.mat")


# In[100]:


A = mat.get('Seg1')
B = mat.get('Seg2')


# In[101]:


def getW1(a, length, width):
    total = length * width
    return len(a) * 1.0 / total


# In[102]:


def intersection(a, b):
    return a.intersection(b)


# In[103]:


def union(a, b):
    return a.union(b)


# In[104]:


def deltaFunction(a):
    if (len(a) == 0):
        return 1
    else:
        return 0


# In[105]:


def deltaBar(a):
    return 1 - deltaFunction(a)


# In[106]:


def getW2(ASets, BSets):
    W2 = []
    for a in ASets:
        W = []
        sum = 0
        for b in BSets:
            sum += deltaBar(intersection(a, b)) * len(b)
        for b in BSets:
            W.append(deltaBar(intersection(a, b)) * len(b) * 1.0 / sum)
        W2.append(W)
    return W2


# In[119]:


def getMartinIndex(A, B):
    NumClustsOfA = 0
    NumClustsOfB = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (A[i][j] > NumClustsOfA):
                NumClustsOfA = A[i][j]
    for i in range(len(B)):
        for j in range(len(B[0])):
            if (B[i][j] > NumClustsOfB):
                NumClustsOfB = B[i][j]
    ASets = []
    BSets = []
    for i in range(NumClustsOfA):
        ASets.append(set())
    for i in range(NumClustsOfB):
        BSets.append(set())
    for i in range(len(A)):
        for j in range(len(A[0])):
            ASets[A[i][j] - 1].add(str(i) + ',' + str(j))
    for i in range(len(B)):
        for j in range(len(B[0])):
            BSets[B[i][j] - 1].add(str(i) + ',' + str(j))
    W1 = []
    for a in ASets:
        W1.append(getW1(a, len(A), len(A[0])))
    W2 = []
    W2 = getW2(ASets, BSets)
    sum0 = 0
    for i in range(len(ASets)):
        sum1 = 0
        for j in range(len(BSets)):
            interLength = len(intersection(ASets[i], BSets[j]))
            unionLength = len(union(ASets[i], BSets[j]))
            sum1 += interLength * 1.0 / unionLength * W2[i][j]
        sum0 += (1 - sum1) * W1[i]
    return sum0


# In[120]:


def getOCE(A, B):
    res = getMartinIndex(A, B)
    res = min(getMartinIndex(B, A), res)
    return res


# In[ ]:


getOCE(A, B)


# In[116]:




