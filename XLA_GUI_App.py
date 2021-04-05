import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import filedialog
from os import path

root = Tk()
root.title("Xử lý ảnh")
root.geometry("1250x700")
# root.maxsize(600, 880)
# root.iconphoto('bg.jpg')

# load = Image.open('./Image/bg.jpg')
# render = ImageTk.PhotoImage(load)
# img = Label(root, image=render)
# img.place(x=0, y=0)

# root.configure(background='pink')

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
    global path

    path = filedialog.askopenfilename()

    if len(path) > 0:
        # load the image from disk
        img = cv.imread(path)

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


def Sobel():
    return


def Laplacian():
    return


def Gray_Scale():
    return


def Histogram():
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
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_sobel.grid(column=0, row=3)

# button Laplacian
btn_Laplacian = Button(root, text="Laplacian", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_Laplacian.grid(column=1, row=3)

# button Gray Scale
btn_Gray_Scale = Button(root, text="Gray Scale", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_Gray_Scale.grid(column=2, row=3)

# button Histogram
btn_Histogram = Button(root, text="Histogram", font=(
    ("Arial"), 10, 'bold'), bg='#fff', fg='#000', command=clear)
btn_Histogram.grid(column=3, row=3)

root.mainloop()
