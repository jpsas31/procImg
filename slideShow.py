from math import fabs
import sys
import matplotlib.pyplot as plt
import numpy as np



ind=0
fig, ax = plt.subplots()
dim=0
img=None
original=None
imga2=None
imagenes=[]
gray=True

frangiToggle=0
black = True

ax.axis('off')
def showSliceKey(img, dimension=0):
    global ax
    global ind
    global gray
    global frangiToggle
    global black
    
    if(dimension<0):dimension=0
    if(dimension>2): dimension=2
    
    ax.clear()
    ax.set_title(f'slice {ind}')
    if(gray):cmap="gray"
    else:cmap=None
    # if(frangiToggle==1):
        # imagen=frangi(np.rollaxis(img, dimension)[52+ind],sigmas=(0.01,0.1,0.01),gamma=1,black_ridges=black)
    # if(frangiToggle==2):
    #     imagen=np.rollaxis(img, dimension)[52+ind]
    # if (frangiToggle==0 or frangiToggle==2): 
    imagen=np.rollaxis(img, dimension)[52+ind]
    ax.imshow(imagen,cmap=cmap) 
    
def on_press(event):
    global ind
    global fig
    global dim
    global frangiToggle
    global black
    global img
    global imga2
    global imagenes
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        ind+=1
        showSliceKey(img,dim)        
    if event.key == 'z':
        ind-=1
        showSliceKey(img,dim)
    if event.key == '1':
        dim=0
        showSliceKey(img,dim)
    if event.key == '2':
        dim=1
        showSliceKey(img,dim)
    if event.key == '3':
        dim=2
        showSliceKey(img,dim)
    if event.key == '4':
        frangiToggle= 0
        showSliceKey(img,dim)
    if event.key == '5':
        frangiToggle= 1
        img=imagenes[0]
        showSliceKey(img,dim)
    if event.key == '6':
        frangiToggle= 2
        # img3=img
        # img=imga2
        # imga2=img3
        img=imagenes[1]
        showSliceKey(img,dim)
    if event.key == '7':
        img=imagenes[2]
        showSliceKey(img,dim)
    fig.canvas.draw()
    fig.canvas.flush_events()  
        
def showSlicesKey(imga,img2=None,originalImg=None,dimension=0,grayVal=True, blackRidges=False):
    global dim
    global img
    global gray
    global black
    global imga2
    global original
    global imagenes
    imagenes.append(imga)
    imagenes.append(img2)
    imagenes.append(originalImg)
    original=originalImg
    imga2=img2
    black=blackRidges
    gray = grayVal
    img=imga
    dim=dimension
    fig.canvas.mpl_connect('key_press_event', on_press)
    plt.show()

# img= getPixelDataNifti("./examples/LR_SI_Case_2_Rep_1_Res_(1_1_1).nii")
# showSlicesKey(img,0)
