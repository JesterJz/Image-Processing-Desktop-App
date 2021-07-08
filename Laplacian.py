import cv2 as cv
from saveimage import *


def Laplacian(input_path):
    im = cv.imread(input_path, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0]-1):
        for j in range(1, im.shape[1]-1):
            A = (4*im.item(i, j)-im.item(i, j+1) -
                 im.item(i+1, j)-im.item(i-1, j)-im.item(i, j-1))
            # B = abs(im.item(i-1,j-1)+im.item(i,j-1)+im.item(i-1,j)-im.item(i+1,j+1)-im.item(i,j+1)-im.item(i+1,j))
            # mag = (A*A + B*B)**(.5)
            if(A < 0):
                temp.itemset((i, j), 0)
            elif(A > 255):
                temp.itemset((i, j), 255)
            else:
                temp.itemset((i, j), A)
    name_image = "Laplacian_"
    save_image(name_image, temp)
    return
