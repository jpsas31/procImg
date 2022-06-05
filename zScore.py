from pydicom import dcmread
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from pyrobex.robex import robex

def getMean(data):
    return data.mean()

def stdDiv(data):
    return data.std()
    