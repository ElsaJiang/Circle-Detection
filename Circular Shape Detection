#-------------------------------------
# PSEUDOCODE: CIRCULAR SHAPE DETECTION
# Version: 1.0.0
# Author: Yi Jiang
# Date created: 01/08/2026
#-------------------------------------
# BEGIN Circle Detection

    # Load image
  # img ← LOAD_IMAGE('circle1.png')
  # original ← COPY(img)

    # Convert to grayscale and remove noise
  # gray ← CONVERT_TO_GRAY(img)
  # gray ← BLUR(gray)

    # Find circles with specific size range
  # circles ← FIND_CIRCLES(
      # gray,
      # min_radius=412,
      # max_radius=460
   # )

    # Process found circles
   # IF circles FOUND THEN
    #    FOR EACH circle IN circles
     #       x, y, radius ← circle

            # Mark on image
      #      DRAW_CIRCLE(original, x, y, radius, GREEN)
      #      DRAW_CIRCLE(original, x, y, 3, RED)


      #   END FOR
  #  END IF

    # Show results
  #  SHOW('Original', img)
  #  SHOW('Detected', original)
  #  PRINT "Found", COUNT(circles), "circles"

  #  WAIT_FOR_KEY()
  #  CLOSE_WINDOWS()

# END


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

# Find circles with specific size range
circles = cv2.HoughCircles(
    image=gray,
    method=cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=1000,
    param1=100,
    param2=40,
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


# Display results
cv2.imshow('Original Image', img)
cv2.imshow('Detected Circles', original_img)
print(f"Detected {len(detected_circles)} circles")
cv2.waitKey(0)
cv2.destroyAllWindows()
