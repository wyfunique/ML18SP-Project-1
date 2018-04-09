import numpy as np
from skimage.measure import label

def clustIndexShift(clustIm):
    shiftRet = np.uint8(np.zeros(clustIm.shape))
    for i in range(clustIm.shape[0]):
        for j in range(clustIm.shape[1]):
            shiftRet[i][j] = clustIm[i][j] + 1
    return shiftRet
    
def getCCIM(clustIm, connectNeighbors):
    # connectNeighbors: 4 or 8, means the 4-connectivity or 8-connectivity. Do not use other integer values.
    ccIm = np.uint8(label(clustIm, neighbors=connectNeighbors))
    ccImOneBased = clustIndexShift(ccIm)
    return ccImOneBased