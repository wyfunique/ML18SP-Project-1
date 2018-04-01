import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust
from MyClustEvalRGB05 import MyClustEvalRGB05
import logging

logging.basicConfig(filename="RGBScore.txt", level=logging.DEBUG)


logging.info("evaluating RGB images using gmm")
print "evaluating RGB images using gmm"
mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1\ImsAndSegs"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".mat")]
scoreList = []
read_dictionary = np.load('numClusters.npy').item()
for onefile in onlyfiles:
    fileName = mypath+ '/' + onefile
    #fileName = "ImsAndTruths12003.mat"
    print "processing "+ fileName
    imsAndSeg = sio.loadmat(fileName)
    im = imsAndSeg.get("Im")
    gt1 = imsAndSeg.get("Seg1")
    gt2 = imsAndSeg.get("Seg2")
    gt3 = imsAndSeg.get("Seg3")
    minScore = 2.0
    numC = read_dictionary[onefile]
    print onefile, " max cluster: ", numC
    logging.info(onefile+ " max cluster: "+ str(numC))
    for numClust in range(2, numC+1):
        [ClusterIm, CCIm] = Clust.MyClust05(im, "Algorithm", "gmm", "ImType", "RGB", "NumClusts", numClust)
        score = min(MyClustEvalRGB05(CCIm, gt1), MyClustEvalRGB05(CCIm, gt2), MyClustEvalRGB05(CCIm, gt3))
        minScore = min(score, minScore)
        logging.info(onefile+" score: "+ str(score)+" clust: "+str(numClust))
        print onefile, " score: ", score, " clust: ", str(numClust)
    scoreList.append(minScore)
    
print scoreList 
arr = np.array(scoreList)
print "mean: ", np.mean(arr), "std dev: ", np.std(arr)
logging.info("mean: "+ str(np.mean(arr))+ "std dev: "+ str(np.std(arr)))


# fileName = "ImsAndTruths2092.mat"
# imsAndSeg = sio.loadmat(fileName)
# print type(imsAndSeg.get('Seg1'))
# print imsAndSeg.get('Seg1').shape
# print imsAndSeg.get('Seg1')

#DisplayImAndSegs(fileName)
# mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1\ImsAndSegs"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#fileName = mypath+ "\/" + onlyfiles[1]

#numClust = 5
#[ClusterIm, CCIm] = yf.MyGMM(im, numClust, 4)


# fig = plt.figure()
# ax1 = fig.add_subplot(221)
# ax1.imshow(im)
# ax1 = fig.add_subplot(222)
# ax1.imshow(ClusterIm)
# ax1 = fig.add_subplot(223)
# ax1.imshow(CCIm)
# ax1 = fig.add_subplot(224)
# ax1.imshow(gt1)
# plt.show()
#print CCIm.max()
#score = min(martin.calOCE(CCIm, gt1), martin.calOCE(CCIm, gt2), martin.calOCE(CCIm, gt3))
#print martin.calOCE(CCIm, gt1)
#print martin.calOCE(CCIm, gt2)
#print martin.calOCE(CCIm, gt3)

#print score


