import cv2 as cv
from showimage import show_image
from saveimage import save_image


def open_camera(box_img):
    # CAP_DShow only windows because error ':~SourceReaderCB'
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # convert image to

        # Display the resulting frame
        cv.imshow('Take of Pictute On Camera', gray)
        if cv.waitKey(1) == 32:  # press 'space' to quit frame
            img_name = "take_of_pic_"
            img_path = save_image(img_name, frame)
            print("{} written!".format(img_name))
            show_image(img_path, box_img)  # show image in label image before
            break
        elif cv.waitKey(1) == 27:  # press and hold 'q' to quit frame
            break

    cap.release()
    cv.destroyAllWindows()
    return 0
