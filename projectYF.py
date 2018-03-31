import scipy.io as sio
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from skimage import morphology
from skimage.filters import rank, gaussian
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage.transform import rescale
from skimage.transform import resize
from sklearn.cluster import SpectralClustering
from skimage.measure import label
from sklearn.decomposition import PCA

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

def validateNumClust(numClust):
    assert numClust < 256, 'Error: The number of clusters must be less than 256'
    
def MyGMM05(image, numClust, connectNeighbors=4, imageType='RGB', filterType=None): 
    # filterType: 'mean', 'median', or None
    # connectNeighbors: 4 or 8, means 4-connectivity or 8-connectivity
    # imageType: 'RGB' or 'Hyper'
    
    validateNumClust(numClust)
    
    gmm = GMM(n_components=numClust, covariance_type='tied')
    
    height = image.shape[0]
    width = image.shape[1]
    n_features = image.shape[2]
    n_samples = height * width
    
    if imageType == 'Hyper': # Normalized image ranging [0, 1]
        pca = PCA(3)
        print 'Reshaping image...'
        dataTmp = np.reshape(image, (n_samples, n_features))
        data = pca.fit_transform(dataTmp)
        #image = np.reshape(dataPCA, (height, width, 3))
        
    if imageType == 'RGB': # Unnormalized image ranging [0, 255]
        if filterType == 'mean':
            image = np.uint8(meanRGB(image, kernel4Orig))
        if filterType == 'median':
            image = np.uint8(medianRGB(image, kernel4Orig))
     
        print 'Reshaping image...'
        data = np.reshape(image, (n_samples, n_features))
        
    print 'Fitting GMM...'
    gmm.fit(data)
    print 'GMM predicting...'
    clustLabels = gmm.predict(data)        
    print 'Inverse reshaping...'
    clustIm = np.uint8(np.reshape(clustLabels, (height, width)))
    ccIm = np.uint8(label(clustIm, neighbors=connectNeighbors))
    clustImOneBased = clustIndexShift(clustIm)
    ccImOneBased = clustIndexShift(ccIm)
    return clustImOneBased, ccImOneBased

def MySpectral05(image, numClust, connectNeighbors=4, imageType='RGB', scaleFactor=0.3, affinity='nearest_neighbors', n_neighbors=20, n_jobs=-1):
    # imageType: 'RGB' or 'Hyper'
    validateNumClust(numClust)
    """
    if filterType == 'mean':
        pass
    if filterType == 'median':
        pass
    """    
    #if numClust > 30:
    #    scaleFactor = scaleFactor / 1.5
    height = image.shape[0]
    width = image.shape[1]
    n_features = image.shape[2]
    n_samples = height * width
    origShape = image.shape[:2]
        
    if imageType == 'Hyper':# Normalized image ranging [0, 1]
        print 'Rescaling image to %f...'% (scaleFactor**2)
        image = rescale(image, scaleFactor, preserve_range=True)
        print 'New shape: %s'%str(image.shape)
        pca = PCA(3)
        dataTmp = np.reshape(image, (n_samples, n_features))
        data = pca.fit_transform(dataTmp)
        #image = np.reshape(dataPCA, (height, width, 3))
        
    if imageType == 'RGB': # Unnormalized image ranging [0, 255]
        print 'Rescaling image to %f...'% (scaleFactor**2)
        image = np.uint8(rescale(image, scaleFactor, preserve_range=True))
        print 'New shape: %s'%str(image.shape)
        print 'Reshaping image...'
        data = np.reshape(image, (n_samples, n_features))
        #graph = kneighbors_graph(X=data, n_neighbors=n_neighbors, mode='distance')
        
    sc = SpectralClustering(n_clusters=numClust, eigen_solver='arpack', affinity=affinity, n_neighbors=n_neighbors, n_jobs=n_jobs)
    print 'SpectralClustering...'
    clustLabels = sc.fit_predict(data)
        
    print 'Inverse reshaping...'
    clustIm = np.uint8(np.reshape(clustLabels, (height, width)))
    print 'Inverse rescaling to %f'% (1.0/(scaleFactor**2))
    clustIm = np.uint8(resize(clustIm, output_shape=origShape, preserve_range=True))
    ccIm = np.uint8(label(clustIm, neighbors=connectNeighbors))
    clustImOneBased = clustIndexShift(clustIm)
    ccImOneBased = clustIndexShift(ccIm)
    return clustImOneBased, ccImOneBased
