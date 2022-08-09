from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from pyrobex.robex import robex

def getMean(data):
    # return np.nanmean(np.where(np.isclose(data,0), np.nan, data))
    return np.mean(data)

def stdDiv(data):
    # return np.nanstd(np.where(data==0, np.nan, data))
    return np.std(data)


def zScoreSlice(img,mean, div):
    imgStand= np.zeros(img.shape)
   
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # print(img[i][j],mean,img[i][j]-mean)
            imgStand[i][j]=(img[i][j]-mean)/div
            
    return imgStand

def zScoreSlices(img):
    print('realizando estandarizacion')
    copia=np.append(img[0].flatten(),img[1].flatten())
    imgStand1= np.zeros(img[0].shape)
    imgStand2= np.zeros(img[1].shape)
    mean=getMean(copia)
    div=stdDiv(copia)
    print(mean,div)
    for i in range(img[0].shape[2]):
        imgStand1[:,:,i]=zScoreSlice(img[0][:,:,i],mean,div)
    for i in range(img[1].shape[2]):     
        imgStand2[:,:,i]=zScoreSlice(img[1][:,:,i],mean,div)
    return [imgStand1,imgStand2]


        