import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import random
import cv2

img=cv2.imread("panda.jpg",0)
plt.imshow(img, cmap='gray')
plt.show()
filter=np.zeros([3,3])
filter.fill(1.0/9)

blur = cv2.filter2D(img, -1,np.array(filter))
plt.imshow(blur, cmap='gray')
plt.show()
better = cv2.filter2D(blur, -1,np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]]))
plt.imshow(better, cmap='gray')
plt.show()

dist=img-better
plt.imshow(dist, cmap='gray')
plt.show()

better2=img-dist
plt.imshow(better2, cmap='gray')
plt.show()