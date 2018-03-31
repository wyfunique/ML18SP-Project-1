# ML18SP-Project-1

The project 1 of course Machine Learning in Spring 2018.

1. projectYF.py contains MyGMM, which only supports RGB now.
2. You will need to install the library "skimage" since I use some filters in this library to preprocess the input RGB image.
3. You can envalute the function based on all 3 types of filtering - mean, median or no filter.
   This is because though I have done a lot of tests to determine main parameters in this MyGMM, I cannot determine which filter to use. It is hard to decide which is better by my eyes.

Call Evaluation Instruction
1. The evaluation code is in MyMartionIndex05.py. 
2. Here is a sample code to call the evalucation function:

    fileName = "ImsAndTruths2092.mat"

    imsAndSeg = sio.loadmat(fileName)

    score = calOCE(imsAndSeg.get('Seg1'), imsAndSeg.get('Seg3'))

   It will give you the evalucation score. For the parameter of calOCE(mat1, mat2), mat1 and mat2 are the segment matrix. One is the ground truth, and the other is what we got after calling cluster function. The order doesn't matter.

3. For score, the lower, the better. It cannot lower than 0, or higher than 1.
4. From my understanding, the evaluation would both focus on both the connectivity and the shape of clusters. 
    For image A having M clusters and image B having N clusters, each cluster in A would iterate over each culster in B to count the number of intersected pixels |Ai^Bj|, and the number of union pixels |Ai U Bj|. (Ai represent cluster i in A, Bj represent cluster j in B). 

    Pi = sum over j (|Ai^Bj|/|Ai U Bj|\*|Bj|/|B|). 
    
    socre = sum over i ((1-Pi)\*|Ai|/|A|)   where |A| means the number of pixels in A.
   
Problems need to fix
1. file name
2. myGMM and mySpectral parameter not the same as required