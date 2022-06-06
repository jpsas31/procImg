import nibabel as nib
from pyrobex.robex import robex

def ApplyRobex(fileName):
    image = nib.load(fileName)
    stripped, mask = robex(image)
    return stripped





