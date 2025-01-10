import cv2
from lecture_code.utils import *

bike_filename = "../../images/bike.jpg"
bike_img = cv2.imread(bike_filename)
# view_image(bike_img)

# Note this will simply add rows/cols for the border.
# This might throw off your image if not careful.
border_bike_img = cv2.copyMakeBorder(bike_img, 0, 0, 0, 10, borderType=cv2.BORDER_REPLICATE)
# Other borderTypes: https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5

view_image(border_bike_img)

