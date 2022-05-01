from PIL import Image, ImageCms
import numpy as np
def leerImg(dir):
    img=Image.open(dir).convert('RGB')
    return img

#Y is luma(Brightness) component
#Cb is the difference between blue and green chroma component
#Cr is the difference between red and green chroma component
def toYCbCr(img):
    return img.convert('YCbCr')

#HUE - SATURATION - VALUE 
#Representa como se ven los colores bajo la luz
def toHSV(img):
    return img.convert('HSV')

#LIGHTNESS - RED-GREEN COMPONENT - BLUE-YELLOW COMPONENT
def toLAB(img):
    #Para convertir a lab se crea una transformacion
    srgb_p = ImageCms.createProfile("sRGB")
    lab_p  = ImageCms.createProfile("LAB")
    rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
    Lab = ImageCms.applyTransform(img, rgb2lab)
    return Lab
    
#Basta con tomar el canal Y porque es el que almacena la informacion mas relevante
def greyScaleYCbCr(imgYCbCr):
    y, cb, cr = imgYCbCr.split()
    return y

def showSideBySide(img1,img2):
    Image.fromarray(np.hstack((np.array(img1),np.array(img2)))).show()
# greyScaleYCbCr(toYCbCr(leerImg('1InNDn3NRlzAQOGsR6zfuRwiJ_5gqY6-5_lqcWxiwjY.webp'))).show()

# toLAB(leerImg('1InNDn3NRlzAQOGsR6zfuRwiJ_5gqY6-5_lqcWxiwjY.webp')).split()[0].show()
# toHSV(leerImg('1InNDn3NRlzAQOGsR6zfuRwiJ_5gqY6-5_lqcWxiwjY.webp')).split()[2].show()