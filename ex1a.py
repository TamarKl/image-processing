import numpy as np
from matplotlib import pyplot as plt

def convolve(img, filter):
    """this function implements the convolution between an image and a filter"""
    img_h, img_w=img.shape
    filter_h=len(filter)
    filter_w=len(filter[0])
    res_final=np.zeros([img_h,img_w],dtype = np.int32)
    res_final.fill(0)
    for i in range(img_h-filter_h+1):
        for j in range(img_w-filter_w+1):
            value=0
            for i_i in range(filter_h):
                for j_j in range(filter_w):
                    value+=img[i+i_i][j+j_j]*filter[i_i][j_j]
            res_final[i][j]=abs(value)
    return res_final
            

def get_rect_edges(img):
    """create a black image with a white rect in the center and returns the rect's edges"""
    img_h, img_w=img.shape
    res_final=np.zeros([img_h,img_w],dtype = np.int32)
    res_final.fill(0)
    edge_vert=np.zeros([img_h,img_w],dtype = np.int32)
    edge_vert.fill(0)
    edge_horz=np.zeros([img_h,img_w],dtype = np.int32)
    edge_horz.fill(0)
    edge_diag=np.zeros([img_h,img_w],dtype = np.int32)
    edge_diag.fill(0)
    edge_horz=convolve(img, [[1,0],[-1,0]]) 
    edge_vert=convolve(img, [[1,-1],[0,0]])
    edge_diag=convolve(img, [[1,0],[0,-1]])
    
    for x in range(img_h):
        for y in range(img_w):
            res_final[x,y]=(edge_horz[x,y]+edge_vert[x,y]+edge_diag[x,y])%256
            
    return res_final

def main():
    """create a black image with a white rect in the center"""
    img = np.zeros([200,200],dtype=np.int32)
    img.fill(0) 
    img[50:150, 50:150] = 255
    plt.imshow(img, cmap='gray')
    plt.show()
    """send to the func that finds the rect edges."""
    result=get_rect_edges(img)
    plt.imshow(result, cmap='gray')
    plt.show()
    
    
    
if __name__=="__main__":
    main()