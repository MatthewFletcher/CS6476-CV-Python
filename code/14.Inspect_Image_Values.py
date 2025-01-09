import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV
img = cv2.imread('../images/dolphin.png')

# Convert the image from BGR to RGB for proper display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Load the image values into a NumPy array
image_array = np.array(img_rgb)

# Print the size and class of the image
print(f"Size of image: {img.shape}")  # Equivalent to size(img) in MATLAB
print(f"Class of image: {img.dtype}")  # Equivalent to class(img) in MATLAB

# Choose an arbitrary Y value for the horizontal line
y_value = 100

# Plot the image with the horizontal line at Y = y_value
fig, ax = plt.subplots(1, 2, figsize=(15, 5))

# Create a copy of the image to draw the line on
img_with_line = img_rgb.copy()
cv2.line(img_with_line, (0, y_value), (img_rgb.shape[1], y_value), (255, 255, 255), 3)

ax[0].imshow(img_with_line)
ax[0].set_title("Image with Horizontal Line")
ax[0].axis('off')

# Get the pixel values at the particular Y location
row_values = image_array[y_value, :, :]

# Plot the row values
ax[1].plot(row_values)
ax[1].set_title("Pixel Values at Y = 100")
ax[1].set_xlabel("X Dimension")
ax[1].set_ylabel("Pixel Value")
plt.show()

# Get arbitrary row and column values
arbitrary_row = image_array[50, :, :]  # Row at Y = 50
arbitrary_column = image_array[:, 75, :]  # Column at X = 75

# Print arbitrary row and column values
print(f"Arbitrary row (Y=50) values: {arbitrary_row}")
print(f"Arbitrary column (X=75) values: {arbitrary_column}")
