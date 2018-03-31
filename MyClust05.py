import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from DisplayImAngSegs import DisplayImAndSegs
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyKmeans05 import MyKmeans05
from projectYF import MyGMM05
from projectYF import MySpectral05
import MyMartinIndex05 as martin
from MyFCM05 import MyFCM05
from MySOM05 import MySOM05

def MyClust05(Im, algStr, alg, imStr, imType, clusStr, numClusts):
    if algStr != "Algorithm":
        print "Second parameter should be Algorithm"
    if imStr != "ImType":
        print "Third parameter should be ImType"
    if clusStr != "NumClusts":
        print "Fifth parameter should be NumClusts"

    if alg.lower() == "kmeans" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = MyKmeans05(Im, imType, numClusts)
    if alg.lower() == "som" and imType.lower() == "rgb": 
        [ClusterIm, CCIm] = MySOM05(Im, imType, numClusts)   
    if alg.lower() == "fcm" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = MyFCM05(Im, imType, numClusts)
    if alg.lower() == "spectral" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = MySpectral05(Im, numClusts, 4)
    if alg.lower() == "gmm" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = MyGMM05(Im, numClusts, 4)

    ## TODO: not implement hyper image yet
    return [ClusterIm, CCIm]