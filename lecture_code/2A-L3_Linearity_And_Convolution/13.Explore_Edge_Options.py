import cv2
from lecture_code.utils import *

img_filename = '../../images/fall-leaves.png'
img = cv2.imread(img_filename)

filter_size = 21
filter_sigma = 3

# swap out your bordertype to see the difference,
smoothed_img = cv2.GaussianBlur(img, (filter_size, filter_size), filter_sigma, borderType=cv2.BORDER_REPLICATE)

view_image(smoothed_img)
