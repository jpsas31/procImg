from cmath import pi
from curses import set_tabsize
from procImgRGB import greyScaleYCbCr, toYCbCr, leerImg, showSideBySide
from PIL import Image
from scipy import ndimage
import math
import numpy

def applyMean(filterArea,row,col,img):
    suma=0
    count=0
    for i in range(-filterArea,filterArea+1,1):
        for j in range(-filterArea,filterArea+1,1):
            if(row+i>=0 and row+i<img.shape[0] and col+j>=0 and col+j<img.shape[1]):
                count+=1
                suma+=img[row+i][col+j]
    return suma/count
    
def meanFilter(img, filterArea):
    imgN= numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgN[i][j]=applyMean(filterArea,i,j,img)
    return imgN

def applyMedian(filterArea,row,col,img):
    values=[]
    for i in range(-filterArea,filterArea+1,1):
        for j in range(-filterArea,filterArea+1,1):
            if(row+i>=0 and row+i<img.shape[0] and col+j>=0 and col+j<img.shape[1]):
                values.append(img[row+i][col+j])
    return numpy.median(values)

    
def medianFilter(img, filterArea):
    imgN= numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgN[i][j]=applyMedian(filterArea,i,j,img)
    return imgN

def calculateValuesGaussian(variance):
    size=1
    constant=1/(2*pi*variance)
    
    while(True):

        matrix=numpy.zeros((size*2 + 1,size*2 + 1))
        for i in range(-size,size+1,1):
            for j in range(-size,size+1,1):
                # print(i,j)
                matrix[i+size][j+size]=constant*math.exp(-0.5*(i**2 + j**2)/variance)
        # print(numpy.sum(matrix))
        if(abs(1-numpy.sum(matrix))<0.1):
            return matrix
        else:size+=1

def calculateValuesRayleigh(variance):
    size=1    
    while(True):

        matrix=numpy.zeros((size*2 + 1,size*2 + 1))
        for i in range(-size,size+1,1):
            for j in range(-size,size+1,1):
                matrix[i+size][j+size]=(i*j/(variance**2))*math.exp(-0.5*(i**2 + j**2)/variance)
        print(numpy.sum(matrix))
        # print(matrix)
        if(size>4):
            return
        if(abs(1-numpy.sum(matrix))<0.1):
            return matrix
        else:size+=1

def applyMatrix(img, matrix,row,col):
    side=matrix.shape[0]
    suma=0.0
    size=int(0.5*(side-1))
    # print(size)
    for i in range(-size,size+1,1):
        for j in range(-size,size+1,1):
            if(row+i>=0 and row+i<img.shape[0] and col+j>=0 and col+j<img.shape[1]):
        
                suma+=(img[row+i][col+j]*matrix[i+size][j+size])
    
    return math.ceil(suma)
   

def gaussianFilter(img,variance):
    matrix=calculateValuesGaussian(variance)
    # matrix=numpy.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])
    print(matrix)
    imgN= numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgN[i][j]=applyMatrix(img,matrix,i,j)
    return imgN

def rayleighFilter(img,variance):
    matrix=calculateValuesRayleigh(variance)
    # matrix=numpy.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])
    print(matrix)
    imgN= numpy.zeros(numpy.shape(img))
    for i in range(numpy.shape(img)[0]):
        for j in range(numpy.shape(img)[1]):
            imgN[i][j]=applyMatrix(img,matrix,i,j)
    return imgN


# greyScaleYCbCr(toYCbCr(leerImg('1InNDn3NRlzAQOGsR6zfuRwiJ_5gqY6-5_lqcWxiwjY.webp'))).show()  
# Image.fromarray( meanFilter(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('1InNDn3NRlzAQOGsR6zfuRwiJ_5gqY6-5_lqcWxiwjY.webp')))),1)).show()
# showSideBySide(greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg'))),
# Image.fromarray( gaussianFilter(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg')))),1)))

# showSideBySide(greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg'))),
# Image.fromarray( ndimage.gaussian_filter(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg')))),sigma=1)))

# showSideBySide( rayleighFilter(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg')))),1),
# Image.fromarray( gaussianFilter(numpy.asarray( greyScaleYCbCr(toYCbCr(leerImg('300px-Kodim17_noisy.jpg')))),1)))