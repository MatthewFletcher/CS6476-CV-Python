import cv2
from lecture_code.utils import *

img_filename = "../../images/tiger.jpg"
img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

view_image(sobel_y)

# We are missing the gray color map, but I don't think that directly is needed?
