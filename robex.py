from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from pyrobex.robex import robex

def showSlice(img,slice):
    plt.imshow(img.data[:,:,59+slice], cmap="gray")
    plt.show( )

def ApplyRobex(fileName):
    image = nib.load(fileName)
    stripped, mask = robex(image)
    return stripped

def writeImg(data,title,affine,header):
    img = nib.Nifti1Image(data, affine, header)
    nib.save(img, title)