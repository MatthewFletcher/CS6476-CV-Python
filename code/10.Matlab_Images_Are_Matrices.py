import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
image = cv2.imread("../images/peppers.jpg")

# Extract the green channel
green_channel = image[:, :, 1]

# Choose an arbitrary Y value for the horizontal line
y_value = 100

# Create a copy of the green channel image to draw the line on
green_with_line = green_channel.copy()

# Draw the line (in white) with increased thickness
cv2.line(green_with_line, (0, y_value), (green_channel.shape[1], y_value), (255,), 3)

# Plotting side by side
fig, ax = plt.subplots(1, 2, figsize=(15, 5))

# Display the green channel with the horizontal line
ax[0].imshow(green_with_line, cmap='gray')
ax[0].set_title(f"Green Channel with Horizontal Line at y={y_value}")
ax[0].axis('off')

# Plot the pixel values underneath the line
pixel_values = green_channel[y_value, :]
ax[1].plot(pixel_values)
ax[1].set_title("Pixel Values Underneath Horizontal Line")
ax[1].set_xlabel("X Dimension")
ax[1].set_ylabel("Pixel Value")

plt.tight_layout()
plt.show()

