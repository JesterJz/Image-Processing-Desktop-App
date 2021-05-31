from tkinter import filedialog
from showimage import show_image
from tkinter import messagebox


def select(box_img):
    # global temp_img
    img_path = filedialog.askopenfilename()

    if len(img_path) > 0:
        # # load the image from disk
        # img = cv.imread(path)
        # temp_img = path

        # # Convert img to RGB
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        # # convert images to PIL format
        # img = Image.fromarray(img)

        show_image(img_path, box_img)
        # print(img_path)
        return img_path
        # resize Image
        # resize_bf = img.resize((720, 576), Image.ANTIALIAS)

        # # convert images to ImageTK format
        # img_bf = ImageTk.PhotoImage(resize_bf)

        # # set image to Label
        # box_img_before.configure(image=img_bf)
        # box_img_before.image = img_bf
    else:
        messagebox.askquestion(
            'Warning !!!', "Sorry. let's choice a image :((")
