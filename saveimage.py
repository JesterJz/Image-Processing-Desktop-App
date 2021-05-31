import os
import cv2 as cv

img_counter = 0


def save_image(name_image, image):
    global img_counter
    img_path = "./Image/ImageResult/" + name_image + \
        "{}".format(img_counter) + ".jpg"
    while os.path.isfile(img_path):
        img_path = "./Image/ImageResult/" + \
            name_image + "{}".format(img_counter) + ".jpg"
        img_counter += 1
        # print(img_path)
    cv.imwrite(img_path, image)
    # print("{} -> {}".format("save", img_path))
    return img_path
