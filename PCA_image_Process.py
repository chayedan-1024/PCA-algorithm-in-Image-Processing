import matplotlib.pyplot as plt
import numpy as np

img_plt = plt.imread("Dirac.jpg")
# plt.imshow(img_plt)
row, column = img_plt.shape
#use PCA
#for single-channel images
#assume that row is number of examples and column is number of features


#1. get the scatter matrix of original image matrix
# print(img_plt.shape,img_plt)
mean_vals = np.mean(img_plt,axis=0)
new_img = img_plt-mean_vals
# print(new_img.shape,new_img)
S = np.dot(new_img.T,new_img)
S = np.mat(S)
#2. get the eigenvalues and eigenvectors of S
eigenvalues, eigenvectors = np.linalg.eig(S)


#sort the eigenvalues and their corresponnding eigenvectors
eigenvalues_sorted = np.argsort(eigenvalues)
#select from 1st to 12th largest eigenvalue
eigenvalues_sorted_k = eigenvalues_sorted[-1:-13:-1]
print(eigenvalues_sorted_k.shape)

#get the selected eigenvectors
eigenvectors_sorted_k = eigenvectors[:,eigenvalues_sorted_k]

#get the projection for each example along each sorted direction
img_projections = np.dot(new_img,eigenvectors_sorted_k)
#rebuild the image
new_img = np.dot(img_projections,eigenvectors_sorted_k.T) + mean_vals
#
plt.subplot(1,2,1)
plt.imshow(img_plt)
plt.subplot(1,2,2)
plt.imshow(new_img)
plt.show()



