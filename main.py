# main.py
import cv2
from color_detection import setup_trackbars, get_trackbar_values, stackImages, getContours
from color_classifier import classify_color
from motion_controller import get_servo_angles_for_color, move_robot_arm
import numpy as np

# Setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

setup_trackbars()

while True:
    success, frame = cap.read()
    if not success:
        print("Error: Could not read frame")
        break

    values = get_trackbar_values()
    h_min, h_max, s_min, s_max, v_min, v_max = values

    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    imgContour = frame.copy()
    getContours(mask, imgContour)

    # Classify the color from dominant HSV value in mask
    hsv_pixels = imgHSV.reshape(-1, 3)
    hsv_pixels = hsv_pixels[np.any(hsv_pixels != [0, 0, 0], axis=1)]
    if len(hsv_pixels) > 0:
        dominant = tuple(np.mean(hsv_pixels, axis=0).astype(int))
        color = classify_color(dominant)
        print(f"Detected color: {color}")
        angles = get_servo_angles_for_color(color)
        move_robot_arm(angles)

    # Stack & show
    imgBlank = np.zeros_like(frame)
    imgStack = stackImages(0.6, ([frame, imgHSV, mask], [result, imgContour, imgBlank]))
    cv2.imshow("Output", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
