from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.title("xử lý ảnh")
root.geometry("630x800")
# root.maxsize(800, 800)
# root.iconphoto('bg.jpg')

# load = Image.open('./Image/bg.jpg')
# render = ImageTk.PhotoImage(load)
# img = Label(root, image=render)
# img.place(x=0, y=0)

root.configure(background='pink')

name = Label(root, text="Xử lý ảnh", fg="#fff", bd=0, bg="#000")
name.config(font=("Arial", 30))
name.pack(pady=10)

before = Label(root, text="Image Before", fg="#fff", bd=0, bg="#000")
before.config(font=("Arial", 18))
before.pack()

box = Label(root, width=60, height=15)
box.pack(pady=20)

after = Label(root, text="Image After", fg="#fff", bd=0, bg="#000")
after.config(font=("Arial", 18))
after.pack()

box = Label(root, width=60, height=15)
box.pack(pady=20)

btn_frame = Frame(root).pack(side=BOTTOM)


def clear():
    pass


def select():
    pass


btn_select = Button(btn_frame, text="Select Image", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff')
btn_select.place(x=150, y=670)
btn_clear = Button(btn_frame, text="Clear Image", font=(
    ("Arial"), 10, 'bold'), bg='#303030', fg='#fff')
btn_clear.place(x=400, y=670)

root.mainloop()
