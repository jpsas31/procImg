from cmath import exp
import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import  RadioButtons, TextBox
from thresholding import applyThreshold

class Formatter(object):
        def __init__(self, im):
            self.im = im
        def __call__(self, x, y):
            z = self.im.get_array()[int(y), int(x)]
            return 'x={:.01f}, y={:.01f}, val={:.01f}'.format(x, y, z)
        
class SlideShow():
    
    #imgs = las imagenes que desea ver
    #dimension = en que eje desea ver la imagen inicial mente
    #grayVal = set to grayscale
    #
    
    def __init__(self,imgs=None,dimension=2,grayVal=True):
        
        self.ind=0
        self.currentIndex=0
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        self.imagenes=imgs
        self.img=self.imagenes[0]
        self.gray = grayVal
        self.dim=dimension
        self.frangiToggle=0
        self.tresh= False
        self.threshType=0
        self.fig.canvas.mpl_disconnect(self.fig.canvas.manager.key_press_handler_id)
        self.ax.axis('off')
        
        #Binary threshold value selector
        self.axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
        self.threshVal = TextBox(self.axfreq, 'Threshold', initial='1')

        #Threshold selector
        self.axfreq.set_visible(False)
        self.rax = plt.axes([0.025, 0.3, 0.15, 0.15], facecolor='lightgoldenrodyellow')
        self.radio = RadioButtons(self.rax, ('0 Otsu', '1 Isodata', '2 LI', '3 Local', '4 Mean', '5 Binary'), active=0)
        self.rax.set_visible(False)
        
        #instructions
        texAx = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor='lightgoldenrodyellow')
        texAx.axis('off')
        texAx.text(0, 0.5,  '''
            x: avanzar mri
            z: regresar mri
            c/v/b: cambiar axis de vision
            a: retroceder a imagen anterior
            s: avanzar a siguiente imagen
            f: toggle threshold
            ''', fontsize=10,
                verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    #Threshold type selector
    def colorfunc(self,label):
        self.threshType=int(label.split(' ')[0])
        self.showSliceKey() 
        self.fig.canvas.draw_idle()
        
   

    def update(self,val):
        print(val)
        self.fig.canvas.draw_idle()
        
    

   
        
    #slice formatter    
    def showSliceKey(self):
    
        if(self.dim<0):self.dim=0
        if(self.dim>2): self.dim=2
        
        self.ax.clear()
        self.ax.axis('off')
        self.ax.set_title(f'slice {self.ind} {self.img[1]}')
        
        if(self.gray):cmap="gray"
        else:cmap=None
        
        imagen=np.rollaxis(self.img[0], self.dim)[self.ind]
        imagen[imagen<10**-8]=0
        
        if(self.tresh):
            self.rax.set_visible(True)
            mean=np.mean(imagen)
            std= 3* np.std(imagen)
            i=abs(mean-std)
            f=mean+std
            if(self.threshType != 5):
                self.axfreq.set_visible(False)
                self.fig.canvas.draw_idle()
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()
                imagen=applyThreshold(imagen,self.threshType)
            else:
                self.axfreq.set_visible(True)
                self.fig.canvas.draw_idle()
                self.fig.canvas.draw()
                self.fig.canvas.flush_events()
                try:
                    imagen= (imagen < eval(self.threshVal.text.strip())) * imagen
                except:
                    print('no es un valor numerico')
        else:
            self.rax.set_visible(False)
            
        im = self.ax.imshow(imagen,cmap=cmap) 
        self.ax.format_coord = Formatter(im)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()  

        
    #key events handler
    def on_press(self,event):
        '''
        x: avanzar mri
        z: regresar mri
        c/v/b: cambiar axis de vision
        a: retroceder a imagen anterior
        s: avanzar a siguiente imagen
        f: toggle threshold
        '''
        sys.stdout.flush()
        if event.key == 'x':
            self.ind+=1
                
        if event.key == 'z':
            self.ind-=1
            
        if event.key == 'c':
            self.dim=0
            
        if event.key == 'v':
            self.dim=1
            
        if event.key == 'b':
            self.dim=2
            
        if event.key == 'a':
            if(self.currentIndex>0): 
                self.ind=0
                self.currentIndex-=1
            
        if event.key == 's':
            if(self.currentIndex<(len(self.imagenes)-1)): 
                self.ind=0
                self.currentIndex+=1
            
        if event.key == 'f':
            self.tresh= not self.tresh
            if(not self.tresh):
                self.axfreq.set_visible(False)
                
    
        self.img=self.imagenes[self.currentIndex]
        self.showSliceKey() 
        
    #mostrar las imagenes
    def showSlicesKey(self):  
        self.fig.canvas.mpl_connect('key_press_event', self.on_press)  
        self.radio.on_clicked(self.colorfunc)
        self.threshVal.on_submit(self.update)
        plt.show()

