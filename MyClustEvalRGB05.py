import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from DisplayImAngSegs import DisplayImAndSegs
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
import kmeans
import projectYF as yf
from MyMartinIndex05 import MyMartinIndex05
import fcm
import MyClust05 as Clust

def MyClustEvalRGB05(CCIm, gt):
    ''' 
      This function is used to evaluate the result got
      by the cluster function kmeans, som, fcm, spectral cluster,
      CMM
      CCIm: for connected component
      gt: ground truth
    '''
    return MyMartinIndex05(CCIm, gt)


#MyClustEvalRGB05()
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


