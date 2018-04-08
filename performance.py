import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust
from MyClustEvalRGB05 import MyClustEvalRGB05
import time
print "evaluating RGB images using spectral"
mypath = "C:\S\ML\Gader_Project_1\Project_1\ImsAndSegs"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".mat")]
read_dictionary = np.load('numClusters.npy').item()
i=0
total=0.
start=0.
end=0.
for onefile in onlyfiles:
    if i==0:
        start=time.time()
    if i==10:
        end=time.time()
        total=end-start
        break
    i+=1
    fileName = mypath + '/' + onefile
    # fileName = "ImsAndTruths12003.mat"
    print "processing " + fileName
    imsAndSeg = sio.loadmat(fileName)
    im = imsAndSeg.get("Im")
    [ClusterIm, CCIm] = Clust.MyClust05(im, "Algorithm", "kmeans", "ImType", "RGB", "NumClusts", 5)

print total




# fileName = "ImsAndTruths2092.mat"
# imsAndSeg = sio.loadmat(fileName)
# print type(imsAndSeg.get('Seg1'))
# print imsAndSeg.get('Seg1').shape
# print imsAndSeg.get('Seg1')

# DisplayImAndSegs(fileName)
# mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1\ImsAndSegs"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# fileName = mypath+ "\/" + onlyfiles[1]

# numClust = 5
# [ClusterIm, CCIm] = yf.MyGMM(im, numClust, 4)


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
# print CCIm.max()
# score = min(martin.calOCE(CCIm, gt1), martin.calOCE(CCIm, gt2), martin.calOCE(CCIm, gt3))
# print martin.calOCE(CCIm, gt1)
# print martin.calOCE(CCIm, gt2)
# print martin.calOCE(CCIm, gt3)

# print score


