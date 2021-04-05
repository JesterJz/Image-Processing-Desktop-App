import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import filedialog
from os import path
import numpy as np
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

root = Tk()
root.title("Xử lý ảnh")
root.geometry("1250x700")
root.maxsize(1250, 700)

temp_img = None

# root.iconphoto('bg.jpg')
# load = Image.open('./Image/bg.jpg')
# render = ImageTk.PhotoImage(load)
# img = Label(root, image=render)
# img.place(x=0, y=0)
# root.configure(background='pink')

# Set Title Name App
name = Label(root, text="Jester Jz", fg="#000", bd=0, bg="pink")
name.config(font=("Engravers MT", 20))
name.grid(column=0, row=0, columnspan=4, pady=10)

# title Image before
before_name = Label(root, text="Image Before", fg="#000", bd=0, bg="pink")
before_name.config(font=("Arial", 16, "bold"))
before_name.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

# Image box before
# Open Img
pic_default = Image.open('./Image/icon_default.png')

# convert images to ImageTK format
img_def = ImageTk.PhotoImage(pic_default)

box_img_before = Label(root, image=img_def, width=600,
                       height=450, bg="#303030")
box_img_before.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# title Image After
after_name = Label(root, text="Image After", fg="#000", bd=0, bg="pink")
after_name.config(font=("Arial", 16, "bold"))
after_name.grid(column=2, row=1, columnspan=2, padx=10, pady=10)

# Image box before
box_img_after = Label(root, image=img_def, width=600,
                      height=450, bg="#303030")
box_img_after.grid(column=2, row=2, columnspan=2, padx=10, pady=10)


def clear():
    pic_default = Image.open('./Image/icon_default.png')
    # convert images to ImageTK format
    img_def = ImageTk.PhotoImage(pic_default)
    # set image to Label default before
    box_img_before.configure(image=img_def)
    box_img_before.image = img_def

    # set image to Label default after
    box_img_after.configure(image=img_def)
    box_img_after.image = img_def
    return 0


def select():
    global path, temp_img

    path = filedialog.askopenfilename()

    if len(path) > 0:
        # load the image from disk
        img = cv.imread(path)
        temp_img = path
        # Convert img to RGB
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # convert images to PIL format
        img = Image.fromarray(img)

        # resize Image
        resize_bf = img.resize((600, 450), Image.ANTIALIAS)

        # convert images to ImageTK format
        img_bf = ImageTk.PhotoImage(resize_bf)

        # set image to Label
        box_img_before.configure(image=img_bf)
        box_img_before.image = img_bf
    return 0


def open_camera():
    global temp_img
    cap = cv.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow('Take of Pictute On Camera', gray)
        if cv.waitKey(1) == 32:
            img_name = "./Image/take_of_pic.png"
            cv.imwrite(img_name, frame)
            print("{} written!".format(img_name))

            # load the image from disk
            img_pic = cv.imread("./Image/take_of_pic.png")

            temp_img = "./Image/take_of_pic.png"

            # Convert img to RGB
            img_pic = cv.cvtColor(img_pic, cv.COLOR_BGR2RGB)

            # convert images to PIL format
            img_pic = Image.fromarray(img_pic)

            # resize Image
            resize_bf = img_pic.resize((600, 450), Image.ANTIALIAS)

            # convert images to ImageTK format
            img_bf = ImageTk.PhotoImage(resize_bf)
            # set image to Label
            box_img_before.configure(image=img_bf)
            box_img_before.image = img_bf

            break
        elif cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    return 0


def Sobel(Image):

    # im = cv.imread('./Image/a.jpg')
    # im = im.astype('int32')
    # dx = ndimage.sobel(im, 0)  # horizontal derivative
    # dy = ndimage.sobel(im, 1)  # vertical derivative
    # mag = np.hypot(dx, dy)  # magnitude
    # mag *= 255.0 / np.max(mag)  # normalize (Q&D)
    # mag.save('sobel.jpg')
    # # Edge_x = cv.Sobel(Image, cv.CV_64F, 1, 0, ksize=3)
    # # # cv.imshow('SobelY filter', Edge_x)
    # # Edge_y = cv.Sobel(Image, cv.CV_64F, 0, 1, ksize=3)

    # # # Edge = np.sqrt(Edge_x**2 + Edge_y**2)
    # # print(Edge_x)
    # # # resize Image
    # # resize_bf = Edge_x.resize((600, 450), Image.ANTIALIAS)

    # # convert images to ImageTK format
    # img = ImageTk.PhotoImage(Image.open(path))
    # # set image to Label
    # box_img_after.configure(image=img)
    # box_img_after.image = img
    return


def Laplacian(input_image):
    im = cv.imread(input_image, 0)
    temp = im.copy()
    # print(im.shape[0],im.shape[1])
    for i in range(1, im.shape[0]-1):
        for j in range(1, im.shape[1]-1):
            A = (4*im.item(i, j)-im.item(i, j+1) -
                 im.item(i+1, j)-im.item(i-1, j)-im.item(i, j-1))
            #B = abs(im.item(i-1,j-1)+im.item(i,j-1)+im.item(i-1,j)-im.item(i+1,j+1)-im.item(i,j+1)-im.item(i+1,j))
            #mag = (A*A + B*B)**(.5)
            if(A < 0):
                temp.itemset((i, j), 0)
            elif(A > 255):
                temp.itemset((i, j), 255)
            else:
                temp.itemset((i, j), A)

    img_path = "Laplacian.jpg"
    cv.imwrite(img_path, temp)

    # resize Image
    resize_bf = Image.open(img_path).resize((600, 450), Image.ANTIALIAS)
    # # convert images to ImageTK format
    img = ImageTk.PhotoImage(resize_bf)
    # set image to Label
    box_img_after.configure(image=img)
    box_img_after.image = img
    return


def Gray_Scale(input_image):
    gray_img = Image.open(input_image)
    pixel_val = gray_img.load()
    print(pixel_val[0, 0])
    for i in range(gray_img.size[0]):
        for j in range(gray_img.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            pixel_val[i, j] = (sum//3, sum//3, sum//3)
    img_path = "Gray.jpg"
    gray_img.save(img_path)
    # resize Image
    resize_bf = Image.open(img_path).resize((600, 450), Image.ANTIALIAS)
    # # convert images to ImageTK format
    img = ImageTk.PhotoImage(resize_bf)
    # set image to Label
    box_img_after.configure(image=img)
    box_img_after.image = img
    return


def Histogram(input_image):
    im = cv.imread(input_image)
    # calculate mean value from RGB channels and flatten to 1D array
    vals = im.mean(axis=2).flatten()
    # plot histogram with 255 bins
    b, bins, patches = plt.hist(vals, 255)
    plt.xlim([0, 255])
    plt.show()
    return


def Binary(input_image):
    hist = []
    for i in range(0, 377):
        hist.append(0)
    binary_pt_image = Image.open(input_image)
    pixel_val = binary_pt_image.load()

    for i in range(binary_pt_image.size[0]):
        for j in range(binary_pt_image.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            sum = sum//3
            # print(sum)
            hist[sum] += 1
    percentage = 30
    threshold_pixels = binary_pt_image.size[0]*binary_pt_image.size[1]*0.6
    print(binary_pt_image.size[0]*binary_pt_image.size[1])
    print(threshold_pixels)

    for i in range(376, -1, -1):

        sum += hist[i]
        if(sum > threshold_pixels):
            threshold_value = i
            break
    print(threshold_value)
    for i in range(binary_pt_image.size[0]):
        for j in range(binary_pt_image.size[1]):
            sum = 0
            for k in range(0, 3):
                sum += pixel_val[i, j][k]
            sum = sum//3
            if(sum > threshold_value):
                pixel_val[i, j] = (255, 255, 255)
            else:
                pixel_val[i, j] = (0, 0, 0)

    img_path = "BinaryPT.jpg"
    binary_pt_image.save(img_path)
    # resize Image
    resize_bf = Image.open(img_path).resize((600, 450), Image.ANTIALIAS)
    # # convert images to ImageTK format
    img = ImageTk.PhotoImage(resize_bf)
    # set image to Label
    box_img_after.configure(image=img)
    box_img_after.image = img
    return


# button select
btn_select = Button(root, text="Select Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=select)
btn_select.grid(column=0, row=4, padx=5, pady=5)

# button open camera
btn_open_cam = Button(root, text="Open Cam", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=open_camera)
btn_open_cam.grid(column=1, row=4, padx=5, pady=5)

# button clear
btn_clear = Button(root, text="Clear Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_clear.grid(column=2, row=4, padx=5, pady=5)

# button quit
btn_cls = Button(root, text="Quit", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=root.quit)
btn_cls.grid(column=3, row=4, padx=5, pady=5)

# button Sobel
btn_sobel = Button(root, text="Sobel", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Sobel(temp_img))
btn_sobel.grid(column=0, row=3)

# button Laplacian
btn_Laplacian = Button(root, text="Laplacian", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Laplacian(temp_img))
btn_Laplacian.grid(column=1, row=3)

# button Gray Scale
btn_Gray_Scale = Button(root, text="Gray Scale", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Gray_Scale(temp_img))
btn_Gray_Scale.grid(column=2, row=3)

# button Histogram
btn_Histogram = Button(root, text="Histogram", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Histogram(temp_img))
btn_Histogram.grid(column=3, row=3)

# button Sobel
btn_Binary = Button(root, text="Binary", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Binary(temp_img))
btn_Binary.grid(column=0, row=5)

root.mainloop()
