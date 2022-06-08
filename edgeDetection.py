from cmath import pi
from procImgRGB import greyScaleYCbCr, toYCbCr, leerImg, showSideBySide
import math
import numpy
from thresholding import applyThreshold, applyBinaryThreshold

import cv2 as cv

from PIL import Image
from filtros import applyMatrix, gaussianFilter,calculateValuesGaussian,calculateValuesGaussianLaplace
# https://towardsdatascience.com/image-derivative-8a07a4118550
# https://homepages.inf.ed.ac.uk/rbf/HIPR2/log.htm
def edgeDetectCanny(img,variance,t1,t2):
    # img=gaussianFilter(img,variance)
    # img=edgeDetectRobert(img)
    # imgF=numpy.zeros(numpy.shape(img))
    # for i in range(numpy.shape(img)[0]):
    #     for j in range(numpy.shape(img)[1]):
    #         imgF[i][j]=applyMatrix(img,matrix,i,j)

    return cv.Canny(img,t1,t2)

def edgeDetectLaplacianGauss(img,variance,tipo=1):
    matrix=calculateValuesGaussianLaplace(1.4,4)
    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgF[i][j]=applyMatrix(img,matrix,i,j)

    return imgF

def edgeDetectLaplacian(img,variance,tipo=1):
    img=gaussianFilter(img,1)
    if(tipo==1):
        matrix=numpy.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    else:
        matrix=numpy.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgF[i][j]=applyMatrix(img,matrix,i,j)
      
    return imgF

def edgeDetectRobert(img):
    
    matrixX=numpy.array([[1,0,],[0,-1]])
    matrixY=numpy.array([[0,1],[-1,0]])

    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            valx=0
            valy=0
            for k in range(0,2):
                for l in range(0,2):
                    if(k+i>=0 and k+i<img.shape[0] and l+j>=0 and l+j<img.shape[1]):
                        valx+=img[i+k][j+l]*matrixX[k][l]
                        valy+=img[i+k][j+l]*matrixY[k][l]
            imgF[i][j]=round(math.sqrt(valx **2 + valy**2))
            
    return imgF

def edgeDetectSobel(img):
    
    matrixX=numpy.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    matrixY=numpy.array([[-1,-2,-1],[0,0,0],[1,2,1]])

    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgF[i][j]=round(math.sqrt(applyMatrix(img,matrixX,i,j) **2 + applyMatrix(img,matrixY,i,j)**2))
            # print(round(math.sqrt(applyMatrix(img,matrixX,i,j) **2 + applyMatrix(img,matrixY,i,j)**2)))
            # print(applyMatrix(img,matrixX,i,j)+applyMatrix(img,matrixY,i,j))
            # imgF[i][j]=(round(abs(applyMatrix(img,matrixX,i,j)) + abs(applyMatrix(img,matrixY,i,j))))
            
    return imgF
def edgeDetectPrewitt(img,meanVal):
    
    matrixX=numpy.array([[-1/meanVal,0,1],[-1/meanVal ,0,1/meanVal],[-1/meanVal,0,1/meanVal]])
    matrixY=numpy.array([[-1/meanVal,-1/meanVal,-1/meanVal],[0,0,0],[1/meanVal,1/meanVal,1/meanVal]])

    imgF=numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgF[i][j]=round(math.sqrt(applyMatrix(img,matrixX,i,j) **2 + applyMatrix(img,matrixY,i,j)**2))

    return imgF


# print(calculateValuesGaussian(0.2))
# Image.fromarray( edgeDetectSobel(gaussianFilter( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1))).show()
# Image.fromarray( edgeDetectLaplacian(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1,1)).show()
# Image.fromarray( edgeDetectLaplacianGauss(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1)).show()
# Image.fromarray( edgeDetectCanny(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1,100,200)).show()

# showSideBySide( edgeDetectSobel(gaussianFilter( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1)),
# edgeDetectPrewitt(gaussianFilter( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1)))

# showSideBySide( edgeDetectSobel( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg'))))),
# edgeDetectCanny(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg')))),1,100,200))

# Image.fromarray(applyBinaryThreshold( edgeDetectSobel( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg'))))),100)).show()
# Image.fromarray(applyThreshold( edgeDetectSobel( numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('400px-Bikesgray.jpg'))))))).show()