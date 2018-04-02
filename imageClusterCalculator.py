
import numpy as np
import scipy.io as scipy
import glob
import os


filenames = glob.glob("ImsAndSegs/*")
files = os.listdir("ImsAndSegs")
arrayOfFiles = np.asarray(filenames)
array2 = np.asarray(files)
dict = {}
print arrayOfFiles.shape
for j in xrange(0,arrayOfFiles.shape[0]):
# for i in xrange(0,5):
    #seg1--------------------------------------------

    mat = scipy.loadmat(arrayOfFiles[j])
    seg1 = mat["Seg1"]
    seg2 = mat["Seg2"]
    seg3 = mat["Seg3"]
    # print seg1
    maxSeg1 = np.amax(seg1)
    threshold = 50
    counter1 = np.zeros(maxSeg1+1,int)

    for i in xrange(0,seg1.shape[0]):
        for k in xrange(0,seg1.shape[1]):
            val = seg1[i][k]
            counter1[val]+=1
    threshold = 0.5*np.mean(counter1)
    maxClust1 = 0
    for i in xrange(1,maxSeg1+1):
        if(counter1[i]>threshold):
            maxClust1+=1

    #seg2-----------------------------------------
    maxSeg2 = np.amax(seg2)
    counter2 = np.zeros(maxSeg2+1,int)
    for i in xrange(0,seg2.shape[0]):
        for k in xrange(0,seg2.shape[1]):
            val = seg2[i][k]
            counter2[val]+=1
    threshold = 0.5*np.mean(counter2)
    maxClust2 = 0
    for i in xrange(1,maxSeg2+1):
        if(counter2[i]>threshold):
            maxClust2+=1

    #seg3------------------------------------------
    maxSeg3 = np.amax(seg3)
    counter3 = np.zeros(maxSeg3+1,int)
    for i in xrange(0,seg3.shape[0]):
        for k in xrange(0,seg3.shape[1]):
            val = seg3[i][k]
            counter3[val]+=1
    threshold = 0.5*np.mean(counter3)
    maxClust3 = 0
    for i in xrange(1,maxSeg3+1):
        if(counter3[i]>threshold):
            maxClust3+=1
    print j
    dict[array2[j]]=max(maxClust1,maxClust2,maxClust3)
    print array2[j]
    print dict[array2[j]]



np.save('numClusters.npy',dict)
print len(dict)
dict["filname.mat"]


