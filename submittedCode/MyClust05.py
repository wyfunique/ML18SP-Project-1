import scipy.io as sio
import numpy as np
from MyKmeans05 import MyKmeans05
from projectYF import MyGMM05
from projectYF import MySpectral05
import MyMartinIndex05 as martin
from MyFCM05 import MyFCM05
from MySOM05 import MySOM05

def MyClust05(Im, algStr, alg, imStr, imType, clusStr, numClusts):
    if algStr.lower() != "algorithm":
        print "Second parameter should be Algorithm"
    if imStr.lower() != "imtype":
        print "Third parameter should be ImType"
    if clusStr.lower() != "numclusts":
        print "Fifth parameter should be NumClusts"
    nrow = Im.shape[0]
    ncol = Im.shape[1]
    #print Im.shape, nrow, ncol
    if numClusts < 1:
        numClusts = int(round(0.05*nrow*ncol))
    if numClusts > 0.25*nrow*ncol:
        numClusts = int(round(0.25*nrow*ncol))
    #print "The number of clusts is: ", numClusts
    if imType.lower() == "rgb":
        if alg.lower() == "kmeans":
            [ClusterIm, CCIm] = MyKmeans05(Im, imType, numClusts)
        if alg.lower() == "som": 
            [ClusterIm, CCIm] = MySOM05(Im, imType, numClusts)   
        if alg.lower() == "fcm":
            [ClusterIm, CCIm] = MyFCM05(Im, imType, numClusts)
        if alg.lower() == "spectral":
            [ClusterIm, CCIm] = MySpectral05(Im, imType, numClusts)
        if alg.lower() == "gmm":
            [ClusterIm, CCIm] = MyGMM05(Im, imType, numClusts)
        return [ClusterIm, CCIm]

    if imType.lower() == "hyper":
        if alg.lower() == "kmeans":
            [ClusterIm, CCIm] = MyKmeans05(Im, imType, numClusts)
        if alg.lower() == "som": 
            [ClusterIm, CCIm] = MySOM05(Im, imType, numClusts)   
        if alg.lower() == "fcm":
            [ClusterIm, CCIm] = MyFCM05(Im, imType, numClusts)
        if alg.lower() == "spectral":
            [ClusterIm, CCIm] = MySpectral05(Im, imType, numClusts)
        if alg.lower() == "gmm":
            [ClusterIm, CCIm] = MyGMM05(Im, imType, numClusts)
        return ClusterIm
    
    