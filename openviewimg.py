from tkinter import *
from PIL import Image, ImageTk


def viewimage(root, img_path):
    # xem image xu li trong frame
    # chon image xong thi ma hoa lun
    # truyen vao openview 1 image path lay image do ma hoa
    viewer = Toplevel(root)
    viewer.title('List image Endcode')
    # viewer.geometry("720x576+0+0")
    viewer.configure(background='#80CBC4')

    # my_img0 = ImageTk.PhotoImage(Image.open(
    #     "./Image/ImageBefore/Reverse_Image.png"))
    my_img0 = ImageTk.PhotoImage(Image.open(img_path))
    # image_list = [img_path]
    lblImage = Label(viewer, image=my_img0)
    lblImage.grid(row=0, column=0, columnspan=3)
    # def forward(image_number):

    #     Label(viewer, image=image_list[image_number-1]
    #           ).grid(row=0, column=0, columnspan=3)
    #     Button(viewer, text=">>", bg="#00897B", command=lambda: forward(
    #         image_number+1)).grid(row=1, column=2)
    #     Button(viewer, text="<<", bg="#00897B", command=lambda: back(
    #         image_number-1)).grid(row=1, column=1)
    #     if image_number == 4:
    #         Button(viewer, text=">>", state=DISABLED)

    # def back(image_number):

    #     Label(viewer, image=image_list[image_number-1]
    #           ).grid(row=0, column=0, columnspan=3)
    #     Button(viewer, text=">>", bg="#00897B", command=lambda: forward(
    #         image_number+1)).grid(row=1, column=2)
    #     Button(viewer, text="<<", bg="#00897B", command=lambda: back(
    #         image_number-1)).grid(row=1, column=1)

    #     if image_number == 1:
    #         Button(viewer, text="<<", state=DISABLED)

    # Button(viewer, text='<<', command=lambda: back(),
    #    state = DISABLED).grid(row = 1, column = 1)
    # Button(viewer, text='Exit', fg='#FFFFFF', bg='#1B5E20',
    #        command=viewer.destroy).grid(row=1, column=0)
    # Button(viewer, text='>>',  command=lambda: forward(2)).grid(row=1, column=2)

    lblEncrypt = Label(viewer, text="Encryption")
    lblEncrypt.grid(row=3, column=0)
    # nhan Encryption -> encrypt image with pass label
    encode = Entry(viewer).grid(row=3, column=1)
    # xem image nhung k da encrypt by pass
    btnCheck = Button(viewer, text='Check')
    btnCheck.grid(row=3, column=2)
    viewer.pack()
