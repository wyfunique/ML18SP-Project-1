import numpy as np
import math
import scipy.io as scipy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from sklearn.decomposition import PCA

def MyFCM05(img1,ImageType,numClust):
    #normalizing image data
    img2 = img1.astype(float)
    img = img2 / 255

    #diff constants for use
    num_features = img.shape[2]
    num_samples=img.shape[0]*img.shape[1]
    img_height = img.shape[0]
    img_width = img.shape[1]

    #reshape img
    img_vector = np.reshape(img,(num_samples,num_features))
    img_vector_T = img_vector.T
    #for hyper simply change the img_vector after pca with 3 dimensions
    if(ImageType=='Hyper'):
        pca = PCA(3)
        principalComponents = pca.fit_transform(img_vector)
        img_vector = principalComponents
    cntr,u,u0,d,jm,p,fpc = fuzz.cmeans(img_vector_T,numClust,2.,error=0.05,maxiter=20)
    uT = u.T
    output = np.zeros(num_samples)
    for i in xrange(0, num_samples):
        max_val = 0.
        max_cluster = 0
        for j in xrange(0,numClust):
            if uT[i][j]>max_val:
                max_val=uT[i][j]
                max_cluster=j+1
        output[i] = max_cluster
    ClusterIm = np.reshape(output, (img_height, img_width))
    imgplot = plt.imshow(img)
    plt.pause(2)
    plt.imshow(ClusterIm)
    plt.pause(5)
    return ClusterIm
