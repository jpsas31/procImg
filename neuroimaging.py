from turtle import filling
from pydicom import dcmread
import matplotlib.pyplot as plt
import dicom2nifti
import dicom2nifti.settings as settings
import nibabel as nib
from robex import ApplyRobex
from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
from slideShow import SlideShow
from zScore import zScoreSlice, zScoreSlices
from frangi import frangi, frangiPropio
import cv2

def getPixelDataDicom(fileName):
    ds = dcmread(fileName)

    return ds.pixel_array

def getPixelDataNifti(fileName):
    epi_img = nib.load(fileName)
    return epi_img.get_fdata()

def showSlice(img,dimension,slice=0):
    if(img.shape[2]==1):slice=0
    plt.imshow(np.rollaxis(img, dimension)[52+slice], cmap="gray")
    plt.show( )
    
def writeImg(data,title,affine,header):
    img = nib.Nifti1Image(data, affine, header)
    nib.save(img, title)
    
def showAllSlices(img, timePerImg=0.5, dimension=0):
    plt.axis('off')
    if(dimension<0):dimension=0
    if(dimension>2): dimension=2
    for r in np.rollaxis(img, dimension):
        plt.figure(1)
        plt.clf()
        plt.imshow(r,cmap="gray")
        plt.pause(timePerImg)   

def convertDirectory(dir):
    settings.disable_validate_slicecount()
    dicom2nifti.convert_directory(dir, dir, compression=True, reorient=True)
    
    
def showSideBySide(img1,img2):
    plt.figure()
    plt.axis('off')
    plt.imshow(img1, cmap="gray")
    plt.figure()
    plt.axis('off')
    plt.imshow(img2)
    plt.show()

def applyMask(img,mask):
    mask= getPixelDataNifti(mask)
    # return cv2.bitwise_and(img,mask)
    return mask*img
    
file1="./examples/LR_SI_Case_30_Rep_1_Res_(1_1_1).nii"
# file1='./mriPrueba/sub-01_ses-01_T1w.nii'
file='./mrit2/BRAINIX_NIFTI_FLAIR.nii'
imgSinStand=ApplyRobex(file1)
imgSinStand2=ApplyRobex(file)

# imgSinStand=getPixelDataNifti(file1)
imgStand, imgStand2 = zScoreSlices([imgSinStand, imgSinStand2])
imgFilteredStand= frangiPropio(imgStand,scale_range=(0.4,0.8,0.2))
imgFilteredStand2 = frangiPropio(imgStand2,scale_range=(0.4,0.8,0.2))
# imgOriginal= ApplyRobex(getPixelDataNifti(file))

imgFilteredMasked= applyMask(imgFilteredStand,'./mask/LR_ROI_mask_Res_(1_1_1).nii')

imgArr=[[imgSinStand, 'Imagen sin estandarizacion'],[imgStand, 'Imagen estandarizada'], 
        [imgSinStand2, 'Imagen sin estandarizacion'],[imgStand2, 'Imagen estandarizada'], 
        [imgFilteredStand, 'Filtro de frangi en imagen estandarizada'],[imgFilteredStand2, 'Filtro de frangi en imagen estandarizada'],
        [imgFilteredMasked, 'Imagen artificial con mascara']]
# maskedImg=applyMask(imgStand,'./mask/LR_ROI_mask_Res_(1_1_1).nii')
# imgFilteredMasked= applyMask(imgFilteredStand,'./mask/LR_ROI_mask_Res_(1_1_1).nii')
# imgArr.append([maskedImg,'Imagen con mascara'])
# imgArr.append([imgFilteredMasked,'Imagen con mascara y frangi'])

# frangi(img,sigmas=np.arange(0.4,0.8,0.2),gamma=10)
# showSlicesKey(imgFiltered,maskedImg,imgOriginal, imgFilteredMasked,2,grayVal=False)
SlideShow(dimension=2,imgs=imgArr,grayVal=True).showSlicesKey()
# showSlicesKey(frangi(img,sigmas=(1,10),gamma=15),0,grayVal=False)
# showSlicesKey(img,0,grayVal=True,blackRidges=True)
# showSideBySide(img[94,:,:],frangi(img[94,:,:],sigmas=(0.01,0.1),gamma=1))

