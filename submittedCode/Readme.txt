1. Dependencies:
    python 2.7.8
    scipy 1.0.0: loadmat() to load image mats
    numpy 1.13.1: main computing package 
    scikit-learn 0.19.1: GaussianMixture, SpectralClustering, PCA, cluster.kmeans
    scikit-image 0.13.1: image filters, image resizing/rescaling, label() for finding connected components
    SciKit-Fuzzy 0.2: cmeans
    matplotlib 2.2.2: pyplot.figure() to plot figures for Santa Barbara image
    sompy: https://github.com/ttlg/sompy
    
    

2. Notice:
    Function MyGMM05 and MySpectral05 is in projectYF.py file 
    Function MyClustEvalRGB05(CCIm, gt): it takes in two parameters, the type of these 
two parameters is numpy array rather than the filename. CCIm represent the connected component.
gt represent the ground truth for CCIm
    Function MyClustEvalHyper05(ClusterIm, gt, mask): it takes in three parameters, the type
of these three parameters is numpy array rather than the filename. ClusterIm represents the clustered
image we got by calling MyClust05. gt represents the ground truth for ClusterIm, and mask represent 
the ground truth mask.
    
