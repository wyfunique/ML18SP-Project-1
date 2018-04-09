import scipy.io as sio
import numpy as np
from MyMartinIndex05 import MyMartinIndex05
import MyClust05 as Clust

def MyClustEvalHyper05(ClusterIm, gt, mask):
    #ClusterIM: type-- np arrays
    #gt: type-- np arrays
    #mask:type -- np arrays
    score = 1.0
    ClusterIm_2 = ClusterIm * mask
    score = MyMartinIndex05(ClusterIm_2, gt)
    return score