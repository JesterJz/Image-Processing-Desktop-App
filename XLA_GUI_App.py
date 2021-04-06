import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import filedialog
import os
import numpy as np
import scipy.misc
from scipy import ndimage as nd
import matplotlib.pyplot as plt

root = Tk()
root.title("Xử lý ảnh")
root.geometry("1920x1080")
# root.maxsize(1920, 1080)

img_counter = 0
temp_img = None
# path = None

# Set Title Name App
name = Label(root, text="Jester Jz", fg="#000", bd=0, bg="pink")
name.config(font=("Engravers MT", 20))
name.grid(column=0, row=0, columnspan=6, pady=5)

# title Image before
before_name = Label(root, text="Image Before", fg="#000", bd=0, bg="pink")
before_name.config(font=("Arial", 16, "bold"))
before_name.grid(column=0, row=1, columnspan=3)

# Image box before
# Open Img
pic_default = Image.open('./Image/icon_default.png')

# convert images to ImageTK format
img_def = ImageTk.PhotoImage(pic_default)

box_img_before = Label(root, image=img_def, width=720,
                       height=576, bg="#303030")
box_img_before.grid(column=0, row=2, columnspan=3, padx=20, pady=5)

# title Image After
after_name = Label(root, text="Image After", fg="#000", bd=0, bg="pink")
after_name.config(font=("Arial", 16, "bold"))
after_name.grid(column=3, row=1, columnspan=3, padx=10, pady=5)

# Image box before
box_img_after = Label(root, image=img_def, width=720,
                      height=576, bg="#303030")
box_img_after.grid(column=3, row=2, columnspan=3, padx=20, pady=5)


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
    global temp_img

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
        resize_bf = img.resize((720, 576), Image.ANTIALIAS)

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
            resize_bf = img_pic.resize((720, 576), Image.ANTIALIAS)

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


def Sobel(Image_path):
    # im = cv.imread('./Image/a.jpg')
    # im = im.astype('int32')
    # dx = ndimage.sobel(im, 0)  # horizontal derivative
    # dy = ndimage.sobel(im, 1)  # vertical derivative
    # mag = np.hypot(dx, dy)  # magnitude
    # mag *= 255.0 / np.max(mag)  # normalize (Q&D)
    # mag.save('sobel.jpg')

    # # # Edge = np.sqrt(Edge_x**2 + Edge_y**2)
    # # print(Edge_x)
    # # # resize Image
    # # resize_bf = Edge_x.resize((600, 450), Image.ANTIALIAS)

    # convert images to ImageTK format
    # img = ImageTk.PhotoImage(Image.open(Image_path))
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
            # B = abs(im.item(i-1,j-1)+im.item(i,j-1)+im.item(i-1,j)-im.item(i+1,j+1)-im.item(i,j+1)-im.item(i+1,j))
            # mag = (A*A + B*B)**(.5)
            if(A < 0):
                temp.itemset((i, j), 0)
            elif(A > 255):
                temp.itemset((i, j), 255)
            else:
                temp.itemset((i, j), A)
    name_image = "./Image/Laplacian_"
    save_show_image(name_image, temp)
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
    name_image = "./Image/Gray_"
    temp = cv.imread(input_image, 0)
    save_show_image(name_image, temp)
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
    resize_bf = Image.open(img_path).resize((720, 576), Image.ANTIALIAS)
    # # convert images to ImageTK format
    img = ImageTk.PhotoImage(resize_bf)
    # set image to Label
    box_img_after.configure(image=img)
    box_img_after.image = img
    return


def Image_Thresholding(input_image):

    # read image
    img = cv.imread(input_image)

    # convert grayscale image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Image_Thresholding
    blur = cv.GaussianBlur(gray, (1, 1), 0)
    ret, thers = cv.threshold(
        blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    # ret : nguong da su dung
    # thers : anh da cat nguong

    name_image = "./Image/Image_Thresholding_"
    save_show_image(name_image, thers)

    return 0


def Reverse_Image(input_image):

    # read image
    img = cv.imread(input_image)

    # convert grayscale image
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # ReverseImage
    image = 255 - gray
    name_image = "./Image/Reverse_Image_"
    save_show_image(name_image, image)

    return 0


def Log_transf(input_image):

    # read image
    img = cv.imread(input_image)

    invGamma = 0.6
    table = []
    for i in range(256):
        table.append(((i/255.0)**invGamma)*255)
    table = np.array(table).astype('uint8')
    image = cv.LUT(img, table)

    name_image = "./Image/Log_transf_"
    save_show_image(name_image, image)

    return 0


def GLS(input_image):

    img = cv.imread(input_image, 0)

    # # # convert grayscale image
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    m, n = img.shape
    # the lower threshold value
    T1 = 100

    # the upper threshold value
    T2 = 180

    # create a array of zeros
    img_thresh_back = np.zeros((m, n), dtype=int)

    for i in range(m):

        for j in range(n):

            if T1 < img[i, j] < T2:
                img_thresh_back[i, j] = 255
            else:
                img_thresh_back[i, j] = img[i, j]

    # Convert array to  png image and save img
    name_image = "GLS_"
    save_show_image(name_image, img_thresh_back)
    return 0


def Smoothing_Image(input_image):

    img = cv.imread(input_image)
    blur = cv.blur(img, (20, 20))
    name_image = "Smoothing_Image_"
    save_show_image(name_image, blur)
    return 0


def laplace_and_gau(input_image):

    img = cv.imread(input_image)
    LoG = nd.gaussian_laplace(img, 1)
    name_image = "laplace_and_gau_"
    save_show_image(name_image, LoG)
    return 0


def save_show_image(name_image, image):
    global img_counter
    img_path = name_image+"{}".format(img_counter)+".jpg"
    print(img_path)
    if os.path.isfile(img_path):
        print("co")
        img_counter += 1
        save_show_image(name_image, image)
    else:
        cv.imwrite(img_path, image)
        print(img_counter)
        # resize Image
        resize_bf = Image.open(img_path).resize((720, 576), Image.ANTIALIAS)
        # convert images to ImageTK format
        img = ImageTk.PhotoImage(resize_bf)
        # set image to Label
        box_img_after.configure(image=img)
        box_img_after.image = img
    return


# button Sobel
btn_sobel = Button(root, text="Sobel", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Sobel(temp_img))
btn_sobel.grid(column=0, row=3, pady=5)

# button Laplacian
btn_Laplacian = Button(root, text="Laplacian", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Laplacian(temp_img))
btn_Laplacian.grid(column=1, row=3, pady=5)

# button Gray Scale
btn_Gray_Scale = Button(root, text="Gray Scale", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Gray_Scale(temp_img))
btn_Gray_Scale.grid(column=2, row=3, pady=5)

# button Histogram
btn_Histogram = Button(root, text="Histogram", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Histogram(temp_img))
btn_Histogram.grid(column=3, row=3, pady=5)

# button Binary
btn_Binary = Button(root, text="Binary", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Binary(temp_img))
btn_Binary.grid(column=4, row=3, pady=5)

# button Reverse Image
btn_Reverse_Image = Button(root, text="Reverse Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Reverse_Image(temp_img))
btn_Reverse_Image.grid(column=4, row=3, pady=5)

# button Image Thresholding
btn_Image_Thresholding = Button(root, text="Image Thresholding", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Image_Thresholding(temp_img))
btn_Image_Thresholding.grid(column=5, row=3, pady=5)

# button Logarithmic transforms
btn_Log_transf = Button(root, text="Logarithmic transforms", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Log_transf(temp_img))
btn_Log_transf.grid(column=0, row=4, pady=5)

# button Grey level Slicing
btn_GLS = Button(root, text="Grey level Slicing", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: GLS(temp_img))
btn_GLS.grid(column=1, row=4, pady=5)

# button Smoothing Image
btn_Smoothing_Image = Button(root, text="Smoothing Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: Smoothing_Image(temp_img))
btn_Smoothing_Image.grid(column=2, row=4, pady=5)

# button Laplace and gaussian
btn_laplace_and_gau = Button(root, text="Laplace and gaussian", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=lambda: laplace_and_gau(temp_img))
btn_laplace_and_gau.grid(column=3, row=4, pady=5)

# button select
btn_select = Button(root, text="Select Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=select)
btn_select.grid(column=4, row=4, pady=5)

# button open camera
btn_open_cam = Button(root, text="Open Cam", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=open_camera)
btn_open_cam.grid(column=5, row=4, pady=5)

# button clear
btn_clear = Button(root, text="Clear Image", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_clear.grid(column=2, row=5, pady=5)

# button quit
btn_cls = Button(root, text="Quit", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=root.quit)
btn_cls.grid(column=3, row=5, pady=5)

root.mainloop()
