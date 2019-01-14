import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random

img = np.zeros([100,100],dtype=np.int32)
img.fill(0) 
img[25:75, 25:75] = 255
plt.imshow(img, cmap='gray')
plt.show()
edge_vert=np.zeros([100,100],dtype = np.int32)
edge_vert.fill(0)
edge_horz=np.zeros([100,100],dtype = np.int32)
edge_horz.fill(0)
#vertical
for x in range(99):
    for y in range(99):
        edge_vert[x,y]=abs(img[x,y+1]-img[x,y])
#horizontal
for y in range(99):
    for x in range(99):
        edge_horz[x,y]=abs(img[x+1,y]-img[x,y])
res_final=np.zeros([100,100],dtype = np.int32)
res_final.fill(0)
for x in range(100):
    for y in range(100):
        res_final[x,y]=(edge_horz[x,y]+edge_vert[x,y])%256
        
plt.imshow(res_final, cmap='gray')
plt.show()  


#dirt an image with Gausian prob.

dirty=np.zeros([100,100],dtype = np.int32)
dirty.fill(0)
for x in range(100):
    for y in range(100):
        dirt= random.randint(0,100)
        if dirt>95:
            dirty[x][y]=np.random.normal(128, 10)
        else:
            dirty[x][y]=img[x][y]
            
#show dirty
plt.imshow(dirty, cmap='gray')
plt.show() 

filter=[[0,-1,0],[-1,2,0,],[0,0,0]]
convolve(dirty, filter)



            
        




