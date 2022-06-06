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
from slideShow import showSlicesKey
from zScore import zScoreSlice, zScoreSlices
from frangi import frangi

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
    
# img=ApplyRobex("minimal.nii")
img= getPixelDataNifti("./examples/LR_SI_Case_2_Rep_1_Res_(1_1_1).nii")
# showSlicesKey(frangi(img,sigmas=(1,10),gamma=15),0,grayVal=False)
showSlicesKey(img,0,grayVal=False)
# showSideBySide(img[94,:,:],frangi(img[94,:,:],sigmas=(0.01,0.1),gamma=1))


#
