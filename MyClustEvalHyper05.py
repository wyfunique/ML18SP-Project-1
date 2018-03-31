import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from DisplayImAngSegs import DisplayImAndSegs
from os import listdir
from os.path import isfile, join
import DisplayImAngSegs as Display
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust

def MyClustEvalHyper05(ClusterIm, gt):
    score = 1.0
    # print ClusterIm.shape
    # if True:
    maskMat = sio.loadmat("../PaviaGrTruthMask.mat")
    mask = maskMat.get("PaviaGrTruthMask")
    truth = gt * mask
    score = MyMartinIndex05(ClusterIm, truth)
    # else:
    #     print "This evaluation is only for Pavia hyper image"
    return score