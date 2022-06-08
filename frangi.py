from cmath import exp, sqrt
from copyreg import constructor
import skimage.filters as sk
import skimage.filters.ridges as skR
import skimage.feature as skF
import numpy as np
from frangi3d import hessian
from frangi3d import frangi as fr

def frangi(img,sigmas=range(1, 10, 2), alpha=0.5, beta=0.5, gamma=15, black_ridges=True):
    
    return sk.frangi(img,sigmas=sigmas, alpha=alpha, beta=beta, gamma=gamma, black_ridges=black_ridges)




def plate_factor(Ra, alpha):
    return 1 - np.exp(np.negative(np.square(Ra)) / (2 * np.square(alpha)))


def blob_factor(Rb, beta):
    return np.exp(np.negative(np.square(Rb) / (2 * np.square(beta))))


def background_factor(S, c):
    return 1 - np.exp(np.negative(np.square(S)) / (2 * np.square(c)))

def vesselness(eigenValues,alpha,beta,c):
    
    eigen1=eigenValues[0]
    eigen1[eigen1==0]=1e-10
    eigen2=eigenValues[1]
    eigen2[eigen2==0]=1e-10
    eigen3=eigenValues[2]
    eigen3[eigen3==0]=1e-10
    print(eigen1.shape)
    # if(eigen2==0 or eigen3==0 or eigen1==0): return 0

    ra =  np.divide(np.abs(eigen2), np.abs(eigen3))
    rb = np.divide(np.abs(eigen1), np.sqrt(np.abs(np.multiply(eigen2, eigen3))))
    s = np.sqrt(np.square(eigen1) + np.square(eigen2) + np.square(eigen3))
  
    return plate_factor(ra,alpha) * blob_factor(rb,beta) * background_factor(s,c) 
    
def frangiPropio(img, scale_range=(0,1,1), alpha=0.5, beta=0.5):
    
    sigmas=np.arange(*scale_range)
    imgFiltered=np.zeros(sigmas.shape+img.shape)
    for sigmaPos,sigma in enumerate(sigmas):
        
        hessianMatrix=skF.hessian_matrix(img,sigma=sigma)
        
        c= np.linalg.norm(hessianMatrix)
        # c=1
        eigen= np.sort(np.absolute(skF.hessian_matrix_eigvals(hessianMatrix)),axis=0)
        #hipo oscuro
        #hiper claro
        #t2
        imgFiltered[sigmaPos]=vesselness(eigen,alpha,beta,c)
        # print(imgFiltered[sigmaPos].shape)
        # for i in  range(img.shape[0]):
        #     for j in  range(img.shape[0]):
        #         for k in  range(img.shape[0]):
        #             imgFiltered[sigmaPos,i,j,k]= vesselness(sorted(eigen[:,i,j,k]),alpha,beta,c)
    return np.max(imgFiltered, axis=0)



# a= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(skF.hessian_matrix_eigvals(skF.hessian_matrix(a)))
# print(hessian.absolute_hessian_eigenvalues(a))
# # def hessianEigen(img,row,col):


