from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("Xử lý ảnh")
root.geometry("600x880")
root.maxsize(600, 880)
# root.iconphoto('bg.jpg')

# load = Image.open('./Image/bg.jpg')
# render = ImageTk.PhotoImage(load)
# img = Label(root, image=render)
# img.place(x=0, y=0)

root.configure(background='pink')

name = Label(root, text="Jester Jz", fg="#000", bd=0, bg="pink")
name.config(font=("Arial", 20))
name.pack(pady=10)

# title Image before
before_name = Label(root, text="Image Before", fg="#000", bd=0, bg="pink")
before_name.config(font=("Arial", 16))
before_name.pack()

# Image box before
# Open Img
pic_bf = Image.open('./Image/bg.jpg')
# resize Img
resize_bf = pic_bf.resize((450, 340), Image.ANTIALIAS)

img_bf = ImageTk.PhotoImage(resize_bf)
box_img_before = Label(root, image=img_bf)
box_img_before.pack(pady=10)

# title Image After
after_name = Label(root, text="Image After", fg="#000", bd=0, bg="pink")
after_name.config(font=("Arial", 16))
after_name.pack()

# Image box before
# Open Img
pic_af = Image.open('./Image/a.jpg')
# resize Img
resize_af = pic_af.resize((450, 340), Image.ANTIALIAS)

img_af = ImageTk.PhotoImage(resize_af)
box_img_after = Label(root, image=img_af)
box_img_after.pack(pady=10)

frame = Frame(root).pack(pady=10)


def clear():
    return


def select():
    return


def open_camera():
    return


# button select
btn_select = Button(frame, text="Select Image", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff', command=select())
btn_select.place(x=100, y=840)
# button open camera
btn_open_cam = Button(frame, text="Open Cam", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff', command=open_camera())
btn_open_cam.place(x=200, y=840)
# button clear
btn_clear = Button(frame, text="Clear Image", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff', command=clear())
btn_clear.place(x=355, y=840)
# button quit
btn_cls = Button(frame, text="Quit", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff', command=root.quit)
btn_cls.place(x=450, y=840)


root.mainloop()
