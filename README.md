# PCA-algorithm-in-Image-Processing
The theory relating to PCA and how to impement

You can refer to my .py file to learn how to use PCA method by python  
And there is an example to process the image of Dirac. 

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

  1. calculate the covariance matrix <b>C</b>(d by d) of <b>X</b>(N by d):  
    (1) cov(<b>d_i</b> ,<b>d_j</b>) = 1/(d-1) \sum_k (d_ik - u_i)^T(d_jk - u_j)  
    Also we have the scatter matrix:  
     for d_i(N by 1): d_i' = d_i - u_i(N by 1)  
     S_ij = d_i'^Td_j' is an element of the scatter matrix <b>S</b>:  
     <b>S</b> = (<b>X</b> - <b>u</b>)^T(<b>X</b> - <b>u</b>)  
     <b>u</b> = [[u_1, u_2, ..., u_d ]  
                [u_1, u_2, ..., u_d ]  
                 ...  ...  ...  ...  
                [u_1, u_2, ..., u_d ]] (N by d).  
     Factly, <b>C</b> = 1/(d-1) <b>S</b>
     $u = \begin{bmatrix}
     u_1
     \end{bmatrix}$
     
  2. get the eigen values and eigen vectors of <b>C</b>,
    This is a math problem, we can solve the equation lambda<b>I</b> - C = 0  
    or use SVD method to get the values and vectors    
      (1) Suppose we have gotten the eigen values c_1, c_2, ..., c_d and their   
      corresponding eigen vectors <b>v_1</b>, <b>v_2</b>, ..., <b>v_d</b>.  
      (2) rank the eigenvalues from the largest to the smallest.  
      get the first k values and k eigenvectors.  
      use these k vectors to form a matrix <b>T</b>(After normalizing each vector).  
      (3) get the new matrix <b>X'</b>: <b>X'</b> = <b>XT</b>
      
