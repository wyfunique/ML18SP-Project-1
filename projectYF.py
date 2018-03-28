import scipy.io as sio
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from skimage import morphology
from skimage.filters import rank, gaussian
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage.transform import rescale
from sklearn.cluster import SpectralClustering

kernel4Orig = morphology.square(width=25)

@adapt_rgb(each_channel)    
def meanRGB(image, kernel):
    return rank.mean(image, kernel)

@adapt_rgb(each_channel)    
def medianRGB(image, kernel):
    return rank.median(image, kernel)

def clustIndexShift(clustIm):
    shiftRet = np.uint8(np.zeros(clustIm.shape))
    for i in range(clustIm.shape[0]):
        for j in range(clustIm.shape[1]):
            shiftRet[i][j] = clustIm[i][j] + 1
    return shiftRet
    
def MyGMM(image, numClust, filterType=None): # Only support RGB now.
    # filterType: 'mean', 'median', or None
    gmm = GMM(n_components=numClust, covariance_type='tied')
    
    if filterType == 'mean':
        image = np.uint8(meanRGB(image, kernel4Orig))
    if filterType == 'median':
        image = np.uint8(medianRGB(image, kernel4Orig))
    
    height = image.shape[0]
    width = image.shape[1]
    n_features = image.shape[2]
    n_samples = height * width
    print 'Reshaping image...'
    data = np.reshape(image, (n_samples, n_features))
    print 'Fitting GMM...'
    gmm.fit(data)
    print 'GMM predicting...'
    clustLabels = gmm.predict(data)
    print 'Inverse reshaping...'
    clustIm = np.uint8(np.reshape(clustLabels, (height, width)))
    clustImOneBased = clustIndexShift(clustIm)
    return clustImOneBased

def MySpectral(image, numClust, scaleFactor=0.3, affinity='nearest_neighbors', n_neighbors=20, n_jobs=-1):
    """
    if filterType == 'mean':
        pass
    if filterType == 'median':
        pass
    """    
    #if numClust > 30:
    #    scaleFactor = scaleFactor / 1.5
    print 'Rescaling image to %f...'% (scaleFactor**2)
    image = np.uint8(rescale(image, scaleFactor, preserve_range=True))
    print 'New shape: %s'%str(image.shape)
    
    height = image.shape[0]
    width = image.shape[1]
    n_features = image.shape[2]
    n_samples = height * width
    print 'Reshaping image...'
    data = np.reshape(image, (n_samples, n_features))
    #graph = kneighbors_graph(X=data, n_neighbors=n_neighbors, mode='distance')
    sc = SpectralClustering(n_clusters=numClust, eigen_solver='arpack', affinity=affinity, n_neighbors=n_neighbors, n_jobs=n_jobs)
    print 'SpectralClustering...'
    clustLabels = sc.fit_predict(data)
    print 'Inverse reshaping...'
    clustIm = np.reshape(clustLabels, (height, width))
    print 'Inverse rescaling to %f'% (1.0/(scaleFactor**2))
    clustIm = np.uint8(rescale(clustIm, 1.0/scaleFactor, preserve_range=True))
    clustImOneBased = clustIndexShift(clustIm)
    return clustImOneBased
