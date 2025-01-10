import cv2
import numpy as np
from lecture_code.utils import view_image

img_path = "../../images/moon.png"
img = cv2.imread(img_path)

# It appears the matlab.imnoise function converts the img to grayscale we will do the same.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# view_image(gray_img)

# Add salt and pepper noise
# There isn't really a nice way to add this noise in CV2, so the following is used.
# source: https://stackoverflow.com/questions/14435632/impulse-gaussian-and-salt-and-pepper-noise-with-opencv
saltpepper_noise = np.random.uniform(low=0, high=255, size=gray_img.shape)
black_mask = saltpepper_noise < 1
white_mask = saltpepper_noise > 254

saltpepper_img = np.copy(gray_img)
saltpepper_img[white_mask] = 255
saltpepper_img[black_mask] = 0
view_image(saltpepper_img)

# Apply the median filter from cv2
median_img = cv2.medianBlur(saltpepper_img, 3)
view_image(median_img)
