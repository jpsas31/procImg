from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from pyrobex.robex import robex

def getMean(data):
    return data.mean()

def stdDiv(data):
    return data.std()


def zScoreSlice(img):
    imgStand= np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            imgStand[i][j]=img[i][j]
    return imgStand

def zScoreSlices(img):
    imgStand= np.zeros(img.shape)
    for i in range(img.shape[2]):
        imgStand[:,:,i]=zScoreSlice(img[:,:,i])
    return imgStand

            
        