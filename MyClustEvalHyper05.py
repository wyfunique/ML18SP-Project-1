import scipy.io as sio
import numpy as np
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust

def MyClustEvalHyper05(ClusterIm, gt):
    score = 1.0
    # print ClusterIm.shape
    # if True:
    maskMat = sio.loadmat("C:\Users\zhaikeke\Documents\Spring2018\MachineLearning\Project1\PaviaGrTruthMask.mat")
    mask = maskMat.get("PaviaGrTruthMask")
    ClusterIm_2 = ClusterIm * mask
    #print "truth: ", truth.max()
    score = MyMartinIndex05(ClusterIm_2, gt)
    # else:
    #     print "This evaluation is only for Pavia hyper image"
    return score