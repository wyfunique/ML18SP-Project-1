import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from DisplayImAngSegs import DisplayImAndSegs
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
import kmeans
import projectYF as yf
import MyMartinIndex05 as martin
import fcm

def MyClust05(Im, algStr, alg, imStr, imType, clusStr, numClusts):
    if algStr != "Algorithm":
        print "Second parameter should be Algorithm"
    if imStr != "ImType":
        print "Third parameter should be ImType"
    if clusStr != "NumClusts":
        print "Fifth parameter should be NumClusts"

    if alg.lower() == "kmeans" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = kmeans.MyKmeans5(Im, imType, numClusts)
    #if alg.lower() == "som" and imType.lower() == "rgb": 
        #[ClusterIm, CCIm] = kmeans.MyKmeans5(Im, imType, numClusts)   
    if alg.lower() == "fcm" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = fcm.MyFCM(Im, imType, numClusts)
    if alg.lower() == "spectral" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = yf.MySpectral(Im, numClusts, 4)
    if alg.lower() == "gmm" and imType.lower() == "rgb":
        [ClusterIm, CCIm] = yf.MyGMM(Im, numClusts, 4)

    ## TODO: not implement hyper image yet
    return [ClusterIm, CCIm]