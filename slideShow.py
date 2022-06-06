from math import fabs
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from frangi import frangi
ind=0
fig, ax = plt.subplots()
dim=0
img=None
gray=True
frangiToggle=True

ax.axis('off')
def showSliceKey(img, dimension=0):
    global ax
    global ind
    global gray
    global frangiToggle
    
    if(dimension<0):dimension=0
    if(dimension>2): dimension=2
    
    ax.clear()
    ax.set_title(f'slice {ind}')
    if(gray):cmap="gray"
    else:cmap=None
    if(frangiToggle): imagen=frangi(np.rollaxis(img, dimension)[52+ind],sigmas=(0.01,0.1),gamma=1)
    else: imagen=np.rollaxis(img, dimension)[52+ind]
    ax.imshow(imagen,cmap=cmap) 
    
def on_press(event):
    global ind
    global fig
    global dim
    global frangiToggle
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
        frangiToggle= not frangiToggle
        showSliceKey(img,dim)
    fig.canvas.draw()
    fig.canvas.flush_events()  
        
def showSlicesKey(imga,dimension=0,grayVal=True):
    global dim
    global img
    global gray
    gray = grayVal
    img=imga
    dim=dimension
    fig.canvas.mpl_connect('key_press_event', on_press)
    plt.show()

# img= getPixelDataNifti("./examples/LR_SI_Case_2_Rep_1_Res_(1_1_1).nii")
# showSlicesKey(img,0)
