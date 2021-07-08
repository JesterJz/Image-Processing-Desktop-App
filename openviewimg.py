from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def viewimage(root, img_path):

    passwd_var = StringVar()
    viewer = Toplevel(root)
    viewer.title('List image Endcode')
    try:
        img = ImageTk.PhotoImage(Image.open(img_path))
        # image_list = [img_path]
        lblImage = Label(viewer, image=img)
        lblImage.pack()
    except Exception:
        lblImage = Label(viewer, text="not show image")
        lblImage.pack()
        print('Error caught : ', Exception.__name__)

    lblPw = Label(viewer, text="Enter password encrypt")
    lblPw.pack()
    passwd_entry = Entry(viewer, textvariable=passwd_var,
                         show='*')
    passwd_entry.pack()
    btnEncrypt = Button(viewer, text='Encryption',
                        command=lambda: Encryption(img_path, passwd_var))
    btnEncrypt.pack(side=LEFT, fill=BOTH)

    btnDecrypt = Button(viewer, text='Decryption')
    btnDecrypt.pack(side=RIGHT, fill=BOTH)

    btnCheck = Button(viewer, text='Check')
    btnCheck.pack()

    viewer.mainloop()


def Encryption(img_path, passwd_var):
    # Assign values
    data = 1281
    key = 27

    # # Display values
    # print('Original Data:', data)
    # print('Key:', key)

    # # Encryption
    # data = data ^ key
    # print('After Encryption:', data)

    # # Decryption
    # data = data ^ key
    # print('After Decryption:', data)

    # try block to handle exception
    try:
        # taking encryption key as input
        key = int(passwd_var.get())

        # print path of image file and encryption key that
        # we are using
        print('The path of file : ', img_path)
        print('Key for encryption : ', key)

        # open file for reading purpose
        fin = open(img_path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writting purpose
        fin = open(img_path, 'wb')

        # writing encrypted data in image
        fin.write(image)
        fin.close()
        messagebox.showinfo("Dialog", "Encryption Done...")
        print('Encryption Done...')

    except Exception:
        messagebox.showerror("Error", "Can't Encryption. Try later, Pls")
        print('Error caught : ', Exception.__name__)

    # nhan Encryption -> encrypt image with pass label
    # xem image nhung k da encrypt by pass
