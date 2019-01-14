import numpy as np
from matplotlib import pyplot as plt
import random
from ex1a import convolve

def add_dirt(img, prob):
    """create a dirty image- pixels will get dirty in the prob probability (between 0-100)"""
    img_h, img_w=img.shape
    dirty=np.zeros([img_h,img_w],dtype = np.int32)
    dirty.fill(0)
    for x in range(img_h):
        for y in range(img_w):
            dirt= random.randint(0,100)
            if dirt<prob:
                dirty[x][y]=random.randint(0,255)
            else:
                dirty[x][y]=img[x][y]
    return dirty

def max_filter(img, filter_dim):
    """ this function sets the pixel value as the max value of the pixels around."""
    img_h, img_w=img.shape
    for i in range(img_h-filter_dim+1):
        for j in range(img_w-filter_dim+1):
            max_value=0
            for i_i in range(filter_dim):
                for j_j in range(filter_dim):
                    if max_value<img[i+i_i][j+j_j]:
                        max_value=img[i+i_i][j+j_j]
            img[i][j]=max_value
    return img
    
    
    
def main():
    """create a black image with a white rect in the center"""
    img = np.zeros([200,200],dtype=np.int32)
    img.fill(0) 
    img[50:150, 50:150] = 255
    plt.imshow(img, cmap='gray')
    plt.show()
    """add dirt to the image with 5% probability."""
    dirty_image=add_dirt(img, 5)
    plt.imshow(dirty_image, cmap='gray')
    plt.show()
    """clean the dirty image with the max filter"""
    clean_dirt=max_filter(img, 2)
    filter=[[3,-1],[-1,-1]]
    """find the rect's edges"""
    rect=convolve(clean_dirt, filter)
    plt.imshow(rect, cmap='gray')
    plt.show()
    
    
if __name__=="__main__":
    main()