import cv2
import matplotlib.pyplot as plt

# Load the image using OpenCV
img = cv2.imread("../../images/bike.jpg")

# Convert the image from BGR to RGB for proper display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the original image
plt.figure(figsize=(6, 6))
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Crop the image using array slicing (y_start:y_end, x_start:x_end)
cropped = img_rgb[110:310, 10:160]

# Display the cropped image
plt.figure(figsize=(6, 6))
plt.imshow(cropped)
plt.title("Cropped Image")
plt.axis("off")
plt.show()
