import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

def DisplayImAndSegs(fileName):
    imsAndSeg = sio.loadmat(fileName)
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax1.imshow(imsAndSeg.get('Im'))
    ax1 = fig.add_subplot(222)
    ax1.imshow(imsAndSeg.get('Seg1'))
    ax1 = fig.add_subplot(223)
    ax1.imshow(imsAndSeg.get('Seg2'))
    ax1 = fig.add_subplot(224)
    ax1.imshow(imsAndSeg.get('Seg3'))
    plt.show()
    return;

fileName = "ImsAndTruths8049.mat"
DisplayImAndSegs(fileName)