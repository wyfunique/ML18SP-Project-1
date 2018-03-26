import numpy as np
import math
import scipy.io as scipy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sklearn.cluster

def MyKmeans5(image,ImageType,numClust):
    img = mpimg.imread(image)
    num_features = img.shape[2]
    k=numClust
    img_vector = np.zeros([img.shape[0]*img.shape[1],num_features])
    img_pixel = np.zeros([img.shape[0]*img.shape[1],2],int)
    count=0
    for i in xrange(0,img.shape[0]):
        for j in xrange(0,img.shape[1]):
            img_vector[count]=img[i][j]
            img_pixel[count]=np.array([i,j])
            count+=1
    num_samples = img_vector.shape[0]
    img_vector_T = img_vector.T

    kmeans= sklearn.cluster.KMeans(n_clusters=k,init="k-means++",max_iter=300).fit(img_vector)
    uT = kmeans.labels_
    ClusterIm = np.zeros([img.shape[0], img.shape[1]])
    for i in xrange(0, num_samples):
        row = img_pixel[i][0]
        col = img_pixel[i][1]
        ClusterIm[row][col]=uT[i]
    return ClusterIm
    #ClusterIm = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.float32)
    # uT = kmeans.labels_
    # for i in xrange(0,num_samples):
    #     row = img_pixel[i][0]
    #     col = img_pixel[i][1]
    #     if uT[i]==1:
    #         ClusterIm[row][col] = [1, 0, 0]
    #     elif uT[i]==2:
    #         ClusterIm[row][col] = [0, 1, 0]
    #     elif uT[i]==3:
    #         ClusterIm[row][col] = [0, 1, 1]
    #     else:
    #         ClusterIm[row][col] = [0, 0, 1]
    #
    # imgplot = plt.imshow(img)
    # plt.pause(2)
    # plt.imshow(ClusterIm)
    # plt.savefig("clusterimkmeans.png")
    # plt.pause(5)

#MyKmeans5('SanBarRGB.png',"RGB",3)
