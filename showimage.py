from PIL import Image, ImageTk


def show_image(img_path, box_img_after):

    # print("{} -> {}".format("show", img_path))
    # resize Image
    resize_bf = Image.open(img_path).resize((720, 576), Image.ANTIALIAS)
    # convert images to ImageTK format
    img = ImageTk.PhotoImage(resize_bf)
    # set image to Label
    box_img_after.configure(image=img)
    box_img_after.image = img
