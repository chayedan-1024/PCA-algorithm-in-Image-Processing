# PCA-algorithm-in-Image-Processing
The theory relating to PCA and how to impement

PCA is a method of feature extraction.

Apply a linear transformation to features to make the new 
features linearly independent.

  *the dependency among features can be expressed by a
  covariance matrix: the element in the i-th row and j-th
  column is the correlation between the i-th and j-th feature
  
  *therefore, if off-diagonal elements are zero, then all features
  are linearly independent
  
Suppose we have training examples represented by a
normalized N × d matrix X. We aim to find a matrix T such that
the covariance matrix of X′ = XT after transformation is a
diagonal matrix

For X, eigenvectors of the associated covariance matrix meet
the above requirements

So the steps to achieve the goal is,

  1. calculate the covariance matrix C(d by d) of X(N by d):
    (1) cov(<b>d1</b> ,)
  3. 
