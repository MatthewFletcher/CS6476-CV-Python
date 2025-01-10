# This file contains functions that are used throughout the repo and thus could be useful
import cv2
import numpy as np

def view_image(img: np.ndarray):
    """
    Pass in an image to view in a small window. Press any key to close the window

    NOTE: When using breakpoints when this function is within the file, pycharm will stall. OR - sometimes it works just
    fine. So if you have trouble with debugging, comment out the function in the script.
    TODO: Fix above
    :param img: A numpy array. You can get this object from a cv.imread()
    :return:
    """
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('frame', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
