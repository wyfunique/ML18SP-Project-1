import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust
from MyClustEvalHyper05 import MyClustEvalHyper05
import logging

logging.basicConfig(filename="hyperScore.txt", level=logging.DEBUG)

logging.info("evaluating Hyper spectral images using kmeans")
print "evaluating Hyper spectral images using kmeans"
mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1"
onefile = "PaviaHyperIm.mat"
fileName = mypath+ '/' + onefile
imsAndSeg = sio.loadmat(fileName)
im = imsAndSeg.get("PaviaHyperIm")
truthfile = mypath + '/' + "PaviaGrTruth.mat"
gtMat = sio.loadmat(truthfile)
gt1 = gtMat.get("PaviaGrTruth")
minScore = 2.0
scoreList = []
for numClust in range(2, 5):
    ClusterIm = Clust.MyClust05(im, "Algorithm", "Kmeans", "ImType", "Hyper", "NumClusts", numClust)
    score = MyClustEvalHyper05(ClusterIm, gt1)
    minScore = min(score, minScore)
    logging.info(onefile+" score: "+str(score)+" clust: "+str(numClust))
    print onefile, " score: ", score, " clust: ", str(numClust)
scoreList.append(minScore)
    
print scoreList 
arr = np.array(scoreList)
print "mean: ", np.mean(arr), "std dev: ", np.std(arr)
logging.info("mean: "+ str(np.mean(arr))+"std dev: "+ str(np.std(arr)))