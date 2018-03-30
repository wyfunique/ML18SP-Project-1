import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

def matInterAndUnionNum(mat1, i, mat2, j): 
    #return the number of intersection in mat1 equal to i and mat2 equal to j
    mat1i = np.isin(mat1, i)
    mat2j= np.isin(mat2, j)
    #print np.count_nonzero(mat1i == True), np.count_nonzero(mat2j == True)
    matInter = np.logical_and(mat1i, mat2j)
    matUnion = np.logical_or(mat1i, mat2j)
    nInter = np.count_nonzero(matInter == True)
    nUnion = np.count_nonzero(matUnion == True)
    #print matInter == True
    return [nInter, nUnion]

def numContainInMat(mat, num):
    return np.count_nonzero(mat == num)

def delta(num):
    if num==0:
        return 1
    else:
        return 0

def getMatInterAndUnion(mat1, mat2):
    ncluster1 = mat1.max()
    ncluster2 = mat2.max()

    mat1Inter2 = np.zeros(shape=(ncluster1, ncluster2))
    mat1Union2 = np.zeros(shape=(ncluster1, ncluster2))
    for i in range(0, ncluster1):
        for j in range(0, ncluster2):
            #print "in loop ", i, j
            [nInter, nUnion] = matInterAndUnionNum(mat1, i+1, mat2, j+1)
            mat1Inter2[i][j] = nInter
            mat1Union2[i][j] = nUnion

    return [mat1Inter2, mat1Union2]  

def calculateWeight(nrow, ncol, interMat, mat2):
    weightMat = np.zeros(shape=(nrow, ncol))
    for i in range(0, nrow):
        lower = 0
        for m in range(0, ncol):
            lower += (1-delta(interMat[i][m]))*numContainInMat(mat2, m+1)
        for j in range(0, ncol):
            upper = (1-delta(interMat[i][j]))*numContainInMat(mat2, j+1)
            if lower == 0:
                weightMat[i][j] = 0
            else:
                weightMat[i][j] = upper*1.0/lower

    return weightMat

def calOutWeight(mat1):
    ncluster1 = mat1.max()
    weightArray = np.zeros(ncluster1)
    numArray = np.zeros(ncluster1)
    totalNum = 0
    for i in range(0, ncluster1):
        numArray[i] = numContainInMat(mat1, i+1)
        totalNum += numArray[i]

    for i in range(0, ncluster1):
        weightArray[i] = numArray[i]*1.0/totalNum

    return weightArray

def martinIndex(mat1, mat2):
    ncluster1 = mat1.max()
    ncluster2 = mat2.max()
    #print ncluster1, ncluster2
    [mat1Inter2, mat1Union2] = getMatInterAndUnion(mat1, mat2)
    weight = calculateWeight(ncluster1, ncluster2, mat1Inter2, mat2)
    outWeight = calOutWeight(mat1)

    # begin to calculate the score
    score = 0.0
    for i in range(0, ncluster1):
        innerScore = 0.0
        for j in range(0, ncluster2):
            innerScore += mat1Inter2[i][j]/mat1Union2[i][j]*weight[i][j]

        innerScore = 1 - innerScore
        score += innerScore*outWeight[i]

    #print score
    return score

def MyMartinIndex05(mat1, mat2):
    score1 = martinIndex(mat1, mat2)
    score2 = martinIndex(mat2, mat1)
    if score1> score2:
        return score2
    else:
        return score1


#fileName = "ImsAndTruths2092.mat"
#imsAndSeg = sio.loadmat(fileName)
#score = calOCE(imsAndSeg.get('Seg1'), imsAndSeg.get('Seg3'))
#print score
