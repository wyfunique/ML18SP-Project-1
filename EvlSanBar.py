import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust


mypath = "C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1"
onefile = "SanBarHyperIm.mat"
fileName = mypath+ '/' + onefile
imsAndSeg = sio.loadmat(fileName)
im = imsAndSeg.get("SanBarIm88x400")
#print imsAndSeg

rgbfile = mypath + '/' + "SanBarRGB.mat"
rgbMat = sio.loadmat(rgbfile)
rgbGt = rgbMat.get("SanBarRGB")
#print rgbMat

numClust = 6
ClusterIm_kmeans = Clust.MyClust05(im, "Algorithm", "kmeans", "ImType", "Hyper", "NumClusts", numClust)
ClusterIm_som = Clust.MyClust05(im, "Algorithm", "som", "ImType", "Hyper", "NumClusts", numClust)
ClusterIm_fcm = Clust.MyClust05(im, "Algorithm", "fcm", "ImType", "Hyper", "NumClusts", numClust)
ClusterIm_spectral = Clust.MyClust05(im, "Algorithm", "spectral", "ImType", "Hyper", "NumClusts", numClust)
ClusterIm_gmm = Clust.MyClust05(im, "Algorithm", "gmm", "ImType", "Hyper", "NumClusts", numClust)

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax1.imshow(rgbGt)
ax1 = fig.add_subplot(322)
ax1.imshow(ClusterIm_kmeans)
ax1 = fig.add_subplot(323)
ax1.imshow(ClusterIm_som)
ax1 = fig.add_subplot(324)
ax1.imshow(ClusterIm_fcm)
ax1 = fig.add_subplot(325)
ax1.imshow(ClusterIm_spectral)
ax1 = fig.add_subplot(326)
ax1.imshow(ClusterIm_gmm)
plt.show()