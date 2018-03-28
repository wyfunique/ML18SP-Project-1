import numpy as np
import math
import scipy.io as scipy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import skfuzzy as fuzz

def MyFCM(img,ImageType,numClust):
    k=numClust
    num_features = img.shape[2]
    img_vector = np.zeros([img.shape[0]*img.shape[1],num_features])
    img_pixel = np.zeros([img.shape[0]*img.shape[1],2],int)
    count=0
    for i in xrange(0,img.shape[0]):
        for j in xrange(0,img.shape[1]):
            img_vector[count]=img[i][j]
            img_pixel[count]=np.array([i,j])
            count+=1
    num_samples = img_vector.shape[0]
    num_features = img_vector.shape[1]
    img_vector_T = img_vector.T
    cntr,u,u0,d,jm,p,fpc = fuzz.cmeans(img_vector_T,k,2.,error=0.05,maxiter=20)
    ClusterIm = np.zeros([img.shape[0], img.shape[1]],int)
    uT = u.T
    for i in xrange(0, num_samples):
        row = img_pixel[i][0]
        col = img_pixel[i][1]
        max_val = 0.
        max_cluster = 0
        for j in xrange(0,k):
            if uT[i][j]>max_val:
                max_val=uT[i][j]
                max_cluster=j+1
        ClusterIm[row][col] = max_cluster
    return ClusterIm

    # ClusterIm = np.zeros([img.shape[0], img.shape[1], 3], dtype=np.float32)
    # uT = u.T
    # print uT
    # for i in xrange(0,num_samples):
    #     row = img_pixel[i][0]
    #     col = img_pixel[i][1]
    #     max_val = 0.
    #     max_cluster = 0
    #     for j in xrange(0,k):
    #         if uT[i][j]>max_val:
    #             max_val=uT[i][j]
    #             max_cluster=j+1
    #     if max_cluster==1:
    #         ClusterIm[row][col] = [1, 0, 0]
    #     elif max_cluster==2:
    #         ClusterIm[row][col] = [0, 1, 0]
    #     elif max_cluster==3:
    #         ClusterIm[row][col] = [0, 0, 1]
    #     else:
    #         ClusterIm[row][col] = [0, 1, 1]
    #
    # imgplot = plt.imshow(img)
    # plt.pause(2)
    # plt.imshow(ClusterIm)
    # plt.savefig("clusterim2.png")
    # plt.pause(5)
#MyClust('SanBarRGB.png', 0, 0, 4)
#MyFCM('SanBarRGB.png','RGB',3)
