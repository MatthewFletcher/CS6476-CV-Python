import cv2
from lecture_code.utils import *

img_filename = "../../images/peppers.jpg"
img = cv2.imread(img_filename)
# view_image(bike_img)

# Note this will simply add rows/cols for the border.
# This might throw off your image if not careful.
# Also, it might be a little hard to see the border. So play with the values a bit.
border_img = cv2.copyMakeBorder(img, 10, 10, 10, 10, borderType=cv2.BORDER_CONSTANT)
# Other borderTypes: https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5

view_image(border_img)

