import cv2
from lecture_code.utils import *

# Load the image using OpenCV
img = cv2.imread("../../images/peppers.jpg")

# Convert the image from BGR to RGB for proper display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

view_image(img=img_rgb)

# Print the size and class of the image
print(f"Size of image: {img.shape}")  # Equivalent to size(img) in MATLAB
print(f"Class of image: {img.dtype}")  # Equivalent to class(img) in MATLAB
