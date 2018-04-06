import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust
from MyClustEvalRGB05 import MyClustEvalRGB05
from random import randint
import logging

logging.basicConfig(filename="clusterScores.txt", level=logging.DEBUG)

mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1\ImsAngSegs_part"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".mat")]
dict = {}
for onefile in onlyfiles:
    fileName = mypath+ '/' + onefile
    print "processing "+ fileName
    logging.info("processing "+ fileName)
    imsAndSeg = sio.loadmat(fileName)
    im = imsAndSeg.get("Im")
    gt1 = imsAndSeg.get("Seg1")
    gt2 = imsAndSeg.get("Seg2")
    gt3 = imsAndSeg.get("Seg3")
    minScore = []
    clustList = []
    for numClust in range(2,30):
        [ClusterIm, CCIm] = Clust.MyClust05(im, "Algorithm", "kmeans", "ImType", "RGB", "NumClusts", numClust)
        score = min(MyClustEvalRGB05(CCIm, gt1), MyClustEvalRGB05(CCIm, gt2), MyClustEvalRGB05(CCIm, gt3))
        #score = randint(0,100)
        minScore.append(score)
        clustList.append(numClust)
        print onefile, ": ", numClust, " ", score
        logging.info(onefile+": "+str(numClust) +" "+ str(score))
    scoreClust = sorted(zip(minScore, clustList))[:3]
    clusters = list(zip(*scoreClust)[1])
    print "best 3 clusters: ", clusters
    logging.info("best 3 clusters: "+ str(clusters)+ " "  )
    dict[onefile] = clusters

np.save('best3Clusters.npy',dict) #save dictionary to 
print len(dict)
#dict1 = np.load('best3Clusters.npy').item() #read the stored dictionary
#print dict1#["ImsAndTruths24004.mat"][0], dict1["ImsAndTruths24004.mat"][1], dict1["ImsAndTruths24004.mat"][2]



