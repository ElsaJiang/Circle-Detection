#Version number, author, date created, version 1.0.0
import cv2
import numpy as np
# Load the image
img = cv2.imread('circle1.png')
# Create a copy of the image
original_img = img.copy()
# Preprocessing for better edge detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply multiple blurring techniques
gray = cv2.medianBlur(gray, 5)  # Reduces noise while preserving edges
gray = cv2.GaussianBlur(gray, (9, 9), 2)  # Additional smoothing
# Adjust Hough Circle parameters for better detection
circles = cv2.HoughCircles(
    image=gray,
    method=cv2.HOUGH_GRADIENT,
    dp=1.2,  # Increased slightly for better detection
    minDist=1000,  # Increased minimum distance between circles
    param1=100,  # Higher threshold for Canny edge detector
    param2=40,  # Accumulator threshold (adjusted for better precision)
    minRadius=412,  # Set minimum radius based on expected can size
    maxRadius=460,  # Set maximum radius based on expected can size
)
# Draw the detected circles
detected_circles = []
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(original_img, (i[0], i[1]), i[2], (0, 255, 0), 3)
        # Draw the center of the circle
        cv2.circle(original_img, (i[0], i[1]), 3, (0, 0, 255), 5)
        detected_circles.append((i[0], i[1], i[2]))
        # Crop and display the detected region
        crop_circle = original_img[i[1]-i[2]:i[1]+i[2], i[0]-i[2]:i[0]+i[2]]
        cv2.imshow(f'Crop {len(detected_circles)}', crop_circle)
# Display results
cv2.imshow('Original Image', img)
cv2.imshow('Detected Circles', original_img)
print(f"Detected {len(detected_circles)} circles")
cv2.waitKey(0)
cv2.destroyAllWindows()


