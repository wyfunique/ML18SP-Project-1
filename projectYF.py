import scipy.io as sio
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from skimage import morphology
from skimage.filters import rank, gaussian
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value

kernel4Orig = morphology.square(width=25)

@adapt_rgb(each_channel)    
def meanRGB(image, kernel):
    return rank.mean(image, kernel)

@adapt_rgb(each_channel)    
def medianRGB(image, kernel):
    return rank.median(image, kernel)
    
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
    clustIm = np.reshape(clustLabels, (height, width))
    return clustIm


