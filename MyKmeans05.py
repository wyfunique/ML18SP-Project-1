import numpy as np
import scipy.io as scipy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sklearn.cluster
from sklearn.decomposition import PCA
import getCCIM
def MyKmeans05(img1,ImageType,numClust):

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

    kmeans= sklearn.cluster.KMeans(n_clusters=numClust,init="k-means++",max_iter=300).fit(img_vector)
    ClusterIm = np.reshape(kmeans.labels_,(img_height,img_width))
    ccImOneBase = getCCIM.getCCIM(ClusterIm, 4)
    return ClusterIm, ccImOneBase
#     plt.imshow(ClusterIm)
#     plt.savefig("kmeans.png")
#     plt.pause(5)
#     return ClusterIm
#
# mat = scipy.loadmat('PaviaRGB.mat')
# img1 = mat["PaviaRGB"]
# print np.amin(img1)
# print np.amax(img1)
# MyKmeans05(img1,'RGB',4)

# mat = scipy.loadmat('PaviaHyperIm.mat')
# img = mat["PaviaHyperIm"]
# mat = scipy.loadmat('SanBarHyperIm.mat')
# img = mat["SanBarIm88x400"]
# print img
# print np.amin(img)
# print np.amax(img)
# MyKmeans05(img,'Hyper',4)
