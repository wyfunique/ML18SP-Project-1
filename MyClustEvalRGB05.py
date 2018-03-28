import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from DisplayImAngSegs import DisplayImAndSegs

def MyClustEvalRGB(ImEvl, ImGt):
    ''' 
      This function is used to evaluate the result got
      by the cluster function
      ImEvl: image that to be evaluated
      ImGt: image of ground truth 
    '''
    print "evaluating RGB images"

    return;


fileName = "ImsAndTruths2092.mat"
imsAndSeg = sio.loadmat(fileName)
print type(imsAndSeg.get('Seg1'))
print imsAndSeg.get('Seg1').shape
print imsAndSeg.get('Seg1')

#DisplayImAndSegs(fileName)