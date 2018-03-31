from sompy import SOM
import numpy as np
from numpy import random as rand
import scipy.io as scipy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sklearn.cluster
from sklearn.decomposition import PCA

def MySOM05(img1,ImageType,numClust):

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

    #for hyper simply change the img_vector after pca with 3 dimensions
    if(ImageType=='Hyper'):
        pca = PCA(3)
        principalComponents = pca.fit_transform(img_vector)
        img_vector = principalComponents
    #map sizeis 25X25
    N = 25
    som = SOM((N, N), img_vector)
    som.set_parameter(neighbor=0.1, learning_rate=0.2)
    output_map = som.train(100000)

    # print output_map.shape
    somMap = output_map.reshape([output_map.shape[0]*output_map.shape[1],3])

    # kmeans to find new centroids
    kmeans2 = sklearn.cluster.KMeans(n_clusters=numClust, init="k-means++", max_iter=10).fit(somMap)
    uT = kmeans2.labels_
    new_centroids = kmeans2.cluster_centers_

    # use new_centroids for kmeans of 1 iteration only to find final output
    kmeans3 = sklearn.cluster.KMeans(n_clusters=numClust, init=new_centroids,n_init=1, max_iter=300).fit(img_vector)

    ClusterIm = np.reshape(kmeans3.labels_,(img_height,img_width))

    plt.imshow(ClusterIm)
    plt.savefig("som.png")
    plt.pause(5)
    return ClusterIm


# mat = scipy.loadmat('PaviaRGB.mat')
# img1 = mat["PaviaRGB"]
# MySOM5(img1,'RGB',4)

# mat = scipy.loadmat('PaviaHyperIm.mat')
# img = mat["PaviaHyperIm"]
# mat = scipy.loadmat('SanBarHyperIm.mat')
# img = mat["SanBarIm88x400"]
# MySOM5(img,'Hyper',4)
