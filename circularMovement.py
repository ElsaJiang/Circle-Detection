"""
Simple Circular Shape Detection for Soda Can
Project: Q3 PROJECT 4 - Simplified Version
"""

import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture('can.MOV')

# Keep track of last detected circle to prevent flickering
last_circle = None

while True:
    # Read frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=50, param2=30, minRadius=280, maxRadius=287)

    # If circles are found
    if circles is not None:
        circles = np.uint16(np.around(circles))

        # Get the first (strongest) circle
        x, y, r = circles[0][0]
        last_circle = (x, y, r)

    # Draw the circle if we have one (use last_circle if no new detection)
    if last_circle is not None:
        x, y, r = last_circle

        # Draw circumference (green circle)
        cv2.circle(frame, (x, y), r, (0, 255, 0), 3)

        # Draw center (red dot with cross)
        cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
        cv2.line(frame, (x-10, y), (x+10, y), (0, 0, 255), 2)
        cv2.line(frame, (x, y-10), (x, y+10), (0, 0, 255), 2)

        # Display center coordinates
        cv2.putText(frame, f"Center: ({x}, {y})", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show result
    cv2.imshow('Circle Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
~                                                                                                                                   
~                                                                                                                                   
~                                                                                                                                   
"circlemove1.py" 64L, 1801B
