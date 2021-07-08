from tkinter import *
from PIL import Image, ImageTk


def viewimage(root, img_path):
    passwd_var = StringVar()
    # xem image xu li trong frame
    # chon image xong thi ma hoa lun
    # truyen vao openview 1 image path lay image do ma hoa
    viewer = Toplevel(root)
    viewer.title('List image Endcode')
    # viewer.geometry("720x576+0+0")
    # viewer.configure(background='#80CBC4')

    img = ImageTk.PhotoImage(Image.open(img_path))
    # image_list = [img_path]
    lblImage = Label(viewer, image=img)
    lblImage.pack()
    lblPw = Label(viewer, text="Enter password encrypt")
    lblPw.pack()
    passwd_entry = Entry(viewer, textvariable=passwd_var,
                         show='*')
    passwd_entry.pack()
    btnEncrypt = Button(viewer, text='Encryption')
    btnEncrypt.pack(side=LEFT, fill=BOTH)

    btnDecrypt = Button(viewer, text='Decryption')
    btnDecrypt.pack(side=RIGHT, fill=BOTH)

    btnCheck = Button(viewer, text='Check')
    btnCheck.pack()

    viewer.mainloop()

    # lblEncrypt = Label(viewer, text="Encryption").grid(row=3, column=0)
    # # nhan Encryption -> encrypt image with pass label
    # passwd_entry = Entry(viewer, textvariable=passwd_var,
    #                      show='*').grid(row=3, column=1)
    # # xem image nhung k da encrypt by pass
    # btnCheck = Button(viewer, text='Check').grid(row=3, column=2)
