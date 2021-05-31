import cv2 as cv
from saveimage import *
from showimage import *


def Gray_Scale(input_image, box_img_after):
    # after_name1.configure(text="Gray Scale")
    img = cv.imread(input_image)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    name_image = "Gray_"
    # print("{} -> {}".format("get", img_path))
    show_image(save_image(name_image, gray_img), box_img_after)
    return
