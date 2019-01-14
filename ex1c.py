import numpy as np
from matplotlib import pyplot as plt
import random
import cv2

def main():
    """read a grayscale image and show it"""
    img=cv2.imread("panda.jpg",0)
    plt.imshow(img, cmap='gray')
    plt.show()
    
    """gaussian blurring filter."""
    filter=[[1.0/16,2.0/16,1.0/16],[2.0/16,4.0/16,2.0/16],[1.0/16,2.0/16,1.0/16]]
    blur = cv2.filter2D(img, -1,np.array(filter))
    plt.imshow(blur, cmap='gray')
    plt.show()
    
    """sharp the image using a Gaussian Sharpen filter."""
    clear = cv2.filter2D(blur, -1,np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]]))
    plt.imshow(clear, cmap='gray')
    plt.show()
    
    """show the dist between the original image and the sharpen image."""
    dist=img-clear
    plt.imshow(dist, cmap='gray')
    plt.show()
    
    
    
    


if __name__=="__main__":
    main()

