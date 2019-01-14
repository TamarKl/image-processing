import numpy as np
from matplotlib import pyplot as plt
import cv2
from ex1b import max_filter
from ex1a import convolve


def find_vert_lines(img):
    """ this function tries to find the thick vertical lines of the sudoku image.
        firts: runs on the image and looks for long vertical lines.
        second: runs on the list of found lines and colors these lines in white and the rest of the image in black.
    """
    M, N = img.shape
    result=np.zeros([M,N])
    result.fill(0)
    sum_row=0
    i=1
    line_color=255
    lines_to_color=[]
    """iterate over the image's columns."""
    while i<N-1: 
        sum_col=0
        curr_center=i
        """iterate over the image's lines."""
        for j in range(1, M-1):
            """try to find a long white line - could move one pixel to the sides."""
            if img[j][curr_center]==line_color:
                sum_col+=1
                if img[j+1][curr_center]!=line_color:
                    if img[j+1][curr_center-1]==line_color:
                        curr_center=curr_center-1
                        continue
                    if img[j+1][curr_center+1]==line_color:
                        curr_center=curr_center+1
        """a long white line was found."""
        if sum_col> 3*M/4:
            lines_to_color.append(i)
            if curr_center>i+2:
                i=curr_center
            else:
                i+=3 
        i+=1
        
    """iterate over all the cols where a long white line was found."""    
    for i in range(len(lines_to_color)):
        curr_center=lines_to_color[i]
        """ find the long path found before- now color the path in the result image."""
        for j in range(M-1):
            result[j][curr_center]=line_color
            if img[j+1][curr_center]!=line_color:
                if img[j+1][curr_center-1]==line_color:
                    curr_center=curr_center-1
                if img[j+1][curr_center+1]==line_color:
                    curr_center=curr_center+1 
            
    return result



def main():   
    img=cv2.imread("sudoku.jpg",0)
    new_img=(img<48)*255
    """use the max filter in order to make the white lines thicker."""
    clear=max_filter(new_img,3)
    """change the function that finds the vertical lines."""
    img2=find_vert_lines(clear)
    """this loop will put the lines found on top of the original picture."""
    clear2=max_filter(img2,3)
    output=img
    line, col=img.shape
    """this loop will put the lines found on top of the original picture."""
    out=cv2.merge((output,output,output))
    """this loop will generate the picture with the found lines on top."""
    for i in range(line):
        for j in range(col):
            if clear2[i][j]==255:
                out.itemset((i,j,1),0)
                out.itemset((i,j,2),0)
                out.itemset((i,j,0),255)
    plt.imshow(out)
    plt.show()
    

if __name__=="__main__":
    main()
