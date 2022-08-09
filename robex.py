import nibabel as nib
from pyrobex.robex import robex

def ApplyRobex(fileName):
    print('realizando skull stripping')
    image = nib.load(fileName)
    stripped, mask = robex(image)
  
    return stripped.to_nibabel().get_fdata()





