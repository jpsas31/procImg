from pydoc import getpager
import pydicom
from pydicom import dcmread
import matplotlib.pyplot as plt
import dicom2nifti
import dicom2nifti.settings as settings
import nibabel as nib

def getPixelDataDicom(fileName):
    ds = dcmread(fileName)

    return ds.pixel_array

def getPixelDataNifti(fileName):
    epi_img = nib.load(fileName)
    return epi_img.get_fdata()


def show_slices(slices):
   fig, axes = plt.subplots(1, len(slices))

   for i, slice in enumerate(slices):
       axes[i].imshow(slice.T, cmap="gray", origin="lower")
       
       
def showPixels(pixels):
    plt.imshow(pixels, cmap="gray")
    plt.show()
def convertDirectory(dir):
    settings.disable_validate_slicecount()
    dicom2nifti.convert_directory(dir, dir, compression=True, reorient=True)
    
# showPixels(getPixelDataDicom("4F6A0EC1(1)"))

showPixels(getPixelDataNifti('7_t2_tse_tra.nii.gz'))

