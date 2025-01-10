import sys
import os
import cv2
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lecture_code.utils import view_image

# img_path = "../../images/moon.png"
# img = cv2.imread(img_path)
# view_image(img)
#
# # Add salt and pepper noise
# # There isn't really a nice way to add this noise in CV2, so the following is used.
# # source: https://stackoverflow.com/questions/14435632/impulse-gaussian-and-salt-and-pepper-noise-with-opencv
# #saltpepper_noise = np.random.uniform(low=0, high=255, size=(img.shape[0], img.shape[1]))
#
# filter_size = 3
# filter_sigma = 50
# sp_img = cv2.GaussianBlur(img,(filter_size,filter_size), filter_size)
# view_image(sp_img)
