import os
from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
from PIL import Image, ImageTk
from scipy import ndimage as nd
from tkinter import messagebox

from TreeView import Treeview_ImageProcess
from saveimage import *
from showimage import *
from grayimage import *
from opencam import open_camera
from clearimage import clear_img_box
from openviewimg import viewimage

root = Tk()
root.title("Image processing")
root.geometry("1300x750+70+30")
root.wm_resizable(width=True, height=True)
# root.configure(background='#80CBC4')
# root.maxsize(1920, 1080)

img_counter = 0
img_path = None
pic_default = Image.open('./Image/icon/icon_default.png')
# convert images to ImageTK format
img_def = ImageTk.PhotoImage(pic_default)

# Set Title Name App
name = Label(root, text="Image processing analysis: v1.0",
             fg="#000", bd=0, bg="#80CBC4")
name.config(font=("Engravers MT", 18))
name.grid(column=0, row=0, columnspan=10, pady=10)

# frame treeview
tree_frame = Frame(root)
tree_frame.grid(column=0, row=2, columnspan=3, padx=10)
Treeview_ImageProcess(tree_frame)

# title Image before
before_name = Label(root, text="Image Before",
                    fg="#FFFFFF", bd=0, bg="#80CBC4")
before_name.config(font=("Arial", 16, "bold"))
before_name.grid(column=3, row=1,)

# Image box before
box_img_before = Label(root, image=img_def, width=480,
                       height=500, bg="#00695C")
box_img_before.grid(column=3, row=2, rowspan=3, padx=10, pady=5)

# title Image After
after_name = Label(root, text="Image After",
                   fg="#FFFFFF", bd=0, bg="#80CBC4")
after_name.config(font=("Arial", 16, "bold"))
after_name.grid(column=4, row=1, padx=10, pady=5)


# Image box before
box_img_after = Label(root, image=img_def, width=480,
                      height=500, bg="#00695C")
box_img_after.grid(column=4, row=2, rowspan=3, padx=10, pady=5)

# button Select
btn_select = Button(root, text="Select", font=(
    ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF')
btn_select.config(command=lambda: select(box_img_before))
btn_select.grid(column=0, row=3)
# button action
btn_action = Button(root, text="Action", font=(
    ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF', command=lambda: select(box_img_before))
btn_action.grid(column=1, row=3)
# button open cam
btn_open_cam = Button(root, text="Camera", font=(
    ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF', command=lambda: open_camera(box_img_before))
btn_open_cam.grid(column=2, row=3)
# button Clear
btn_clear = Button(root, text="Clear", font=(
    ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF', command=lambda: clear_img_box(box_img_before, box_img_after))
btn_clear.grid(column=0, row=4)
# # button Quit
# btn_quit = Button(root, text="Quit", font=(
#     ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF', command=root.quit)
# btn_quit.grid(column=2, row=4)
# button view image
btn_view_img = Button(root, text="View Image", font=(
    ("Arial"), 10, 'bold'), bg='#43A047', width=10, height=1, fg='#FFFFFF', command=lambda: viewimage(root, img_path))
btn_view_img.grid(column=1, row=4)


def callback():
    """
    Asks the user if they really want to quit
    """
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()


def select(box_img):
    global img_path
    img_path = filedialog.askopenfilename()

    if len(img_path) > 0:
        try:
            show_image(img_path, box_img)
        except Exception:
            box_img.configure(text="image not show")
            box_img.image = "image not show"
    else:
        messagebox.askquestion(
            'Warning !!!', "Sorry. let's choice a image :((")


# def save_as():
#     messagebox.askquestion('Warning !!!', 'Sorry the feature is updating :((')

#     return 0

# def Sobel(Image_path):
#     im = cv.imread('./Image/a.jpg')
#     im = im.astype('int32')
#     dx = ndimage.sobel(im, 0)  # horizontal derivative
#     dy = ndimage.sobel(im, 1)  # vertical derivative
#     mag = np.hypot(dx, dy)  # magnitude
#     mag *= 255.0 / np.max(mag)  # normalize (Q&D)
#     mag.save('sobel.jpg')

#     # # Edge = np.sqrt(Edge_x**2 + Edge_y**2)
#     # print(Edge_x)
#     # # resize Image
#     # resize_bf = Edge_x.resize((600, 450), Image.ANTIALIAS)

#     # convert images to ImageTK format
#     img = ImageTk.PhotoImage(Image.open(Image_path))
#     # set image to Label
#     box_img_after.configure(image=img)
#     box_img_after.image = img
#     return

# def Histogram(input_image):
#     after_name1.configure(text="Histogram")
#     im = cv.imread(input_image)
#     # calculate mean value from RGB channels and flatten to 1D array
#     vals = im.mean(axis=2).flatten()
#     # plot histogram with 255 bins
#     b, bins, patches = plt.hist(vals, 255)
#     plt.xlim([0, 255])
#     plt.show()
#     return


# def Binary(input_image):
#     after_name1.configure(text="Binary")
#     hist = []
#     for i in range(0, 377):
#         hist.append(0)
#         binary_pt_image = Image.open(input_image)
#         pixel_val = binary_pt_image.load()

#     for i in range(binary_pt_image.size[0]):
#         for j in range(binary_pt_image.size[1]):
#             sum = 0
#             for k in range(0, 3):
#                 sum += pixel_val[i, j][k]
#             sum = sum//3
#             # print(sum)
#             hist[sum] += 1
#     percentage = 30
#     threshold_pixels = binary_pt_image.size[0]*binary_pt_image.size[1]*0.6
#     print(binary_pt_image.size[0]*binary_pt_image.size[1])
#     print(threshold_pixels)

#     for i in range(376, -1, -1):

#         sum += hist[i]
#         if(sum > threshold_pixels):
#             threshold_value = i
#             break
#     print(threshold_value)
#     for i in range(binary_pt_image.size[0]):
#         for j in range(binary_pt_image.size[1]):
#             sum = 0
#             for k in range(0, 3):
#                 sum += pixel_val[i, j][k]
#             sum = sum//3
#             if(sum > threshold_value):
#                 pixel_val[i, j] = (255, 255, 255)
#             else:
#                 pixel_val[i, j] = (0, 0, 0)

#     img_path = "./Image/ImageResult/BinaryPT_"

#     return

# #  phan nguong ,


# def Image_Thresholding(input_image):
#     after_name1.configure(text="Image Thresholding")
#     # read image
#     img = cv.imread(input_image)
#     # convert grayscale image
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     # Image_Thresholding
#     blur = cv.GaussianBlur(gray, (1, 1), 0)
#     ret, thers = cv.threshold(
#         blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
#     # ret : nguong da su dung
#     # thers : anh da cat nguong
#     # từ ngưỡng thang độ xám có thể sử dụng ngưỡng tạo hình ảnh nhị phân

#     name_image = "./Image/Image_Thresholding_"
#     save_show_image(name_image, thers)

#     return 0


# def Reverse_Image(input_image):
#     after_name1.configure(text="Reverse Image")
#     # read image
#     img = cv.imread(input_image)
#     # convert grayscale image/ chuyen doi khong gian mau
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # ReverseImage / chuyen muc xam
#     image = 255 - gray
#     name_image = "./Image/Reverse_Image_"
#     save_show_image(name_image, image)

#     return 0

# # #  các giá trị cường độ tối hơn được đưa ra các giá trị sáng hơn
# # #  chi tiết vùng tối hơn hoặc xám của hình ảnh dễ nhìn thấy hơn
# # #


# def Log_transf(input_image):
#     after_name1.configure(text="Logarithmic Transforms")
#     # read image
#     img = cv.imread(input_image)
#     # hang so tỷ lệ / chia đều pixcel
#     invGamma = 0.6
#     table = []
#     # chuyển đổi
#     for i in range(256):
#         table.append(((i/255.0)**invGamma)*255)
#     table = np.array(table).astype('uint8')
#     image = cv.LUT(img, table)

#     name_image = "./Image/Log_transf_"
#     save_show_image(name_image, image)

#     return 0


# # Chuyển đổi mức xám
# # Nâng cao hình ảnh cung cấp độ tương phản tốt hơn và hình ảnh chi tiết hơn
# def GLS(input_image):
#     after_name1.configure(text="Grey Level Slicing")
#     img = cv.imread(input_image, 0)
#     # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     m, n = img.shape
#     # the lower threshold value
#     T1 = 100

#     # the upper threshold value
#     T2 = 180

#     # create a array of zeros
#     img_thresh_back = np.zeros((m, n), dtype=int)
#     for i in range(m):

#         for j in range(n):

#             if T1 < img[i, j] < T2:
#                 img_thresh_back[i, j] = 255
#             else:
#                 img_thresh_back[i, j] = img[i, j]

#     # Convert array to  png image and save img
#     name_image = "GLS_"
#     save_show_image(name_image, img_thresh_back)
#     return 0

# # Làm mờ hình ảnh với nhiều bộ lọc thông thấp khác nhau
# # Làm mờ hình ảnh bằng cách sử dụng bộ lọc hộp chuẩn hóa


# def Smoothing_Image(input_image):
#     after_name1.configure(text="Smoothing Image")
#     img = cv.imread(input_image)
#     blur = cv.blur(img, (5, 5))
#     name_image = "Smoothing_Image_"
#     save_show_image(name_image, blur)
#     return 0


# def laplace_and_gau(input_image):
#     after_name1.configure(text="Laplace and Gaussiane")
#     img = cv.imread(input_image)
#     LoG = nd.gaussian_laplace(img, 1)
#     name_image = "laplace_and_gau_"
#     save_show_image(name_image, LoG)
#     return 0


# def save_show_image(name_image, image):
#     global img_counter
#     img_path = name_image+"{}".format(img_counter)+".jpg"
#     print(img_path)
#     if os.path.isfile(img_path):
#         print("co")
#         img_counter += 1
#         save_show_image(name_image, image)
#     else:
#         cv.imwrite(img_path, image)
#         print(img_counter)
#         # resize Image
#     resize_bf = Image.open(img_path).resize((720, 576), Image.ANTIALIAS)
#     # convert images to ImageTK format
#     img = ImageTk.PhotoImage(resize_bf)
#     # set image to Label
#     box_img_after.configure(image=img)
#     box_img_after.image = img
#     return

# # button Save as
# btn_save_as = Button(root, text="Save as", font=(
#     ("Arial"), 10, 'bold'), bg='#827717', width=12, height=1, fg='#FFFFFF', command=save_as)
# btn_save_as.grid(column=1, row=4, pady=5)
# # button Reverse Image
# btn_Reverse_Image = Button(root, text="Reverse", font=(
#     ("Arial"), 10, 'bold'), bg='#43A047', width=14, height=1, fg='#FFFFFF', command=lambda: Reverse_Image(temp_img))
# btn_Reverse_Image.grid(column=2, row=3, pady=5)
# ask Are you sure you want to quit?
root.protocol("WM_DELETE_WINDOW", callback)
root.mainloop()
