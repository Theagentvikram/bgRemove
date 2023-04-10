import cv2
import numpy as np

# Load the image
img = cv2.imread('input_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform binary thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour (which should be the subject)
largest_contour = max(contours, key=cv2.contourArea)

# Create a mask for the subject
mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [largest_contour], 0, (255, 255, 255), -1)

# Apply the mask to the image
result = cv2.bitwise_and(img, img, mask=mask)

# Display the result
cv2.imshow('Result', result)
cv2.waitKey(0)

# Save the result
cv2.imwrite('output_image.jpg', result)
