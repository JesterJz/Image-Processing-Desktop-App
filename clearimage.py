from PIL import Image, ImageTk


def clear_img_box(box_img_before, box_img_after):
    pic_default = Image.open('./Image/icon/icon_default.png')
    # convert images to ImageTK format
    img_def = ImageTk.PhotoImage(pic_default)
    # set image to Label default before
    box_img_before.configure(image=img_def)
    box_img_before.image = img_def

    # set image to Label default after
    box_img_after.configure(image=img_def)
    box_img_after.image = img_def
    return 0
