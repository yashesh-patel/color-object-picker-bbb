# color_classifier.py
import numpy as np

def classify_color(hsv_pixel):
    """
    Classifies a color name based on the HSV value of the pixel.
    hsv_pixel: a tuple/list of (h, s, v)
    Returns: color name as string
    """
    h, s, v = hsv_pixel

    if s < 50 and v > 200:
        return "white"
    if v < 50:
        return "black"

    if h < 10 or h > 160:
        return "red"
    elif 10 < h <= 30:
        return "yellow"
    elif 30 < h <= 85:
        return "green"
    elif 85 < h <= 130:
        return "blue"
    else:
        return "undefined"

def get_dominant_hsv_color(masked_img):
    """
    Returns the most frequent HSV color in the masked image.
    masked_img: image filtered by a mask
    Returns: (h, s, v) tuple
    """
    hsv = cv2.cvtColor(masked_img, cv2.COLOR_BGR2HSV)
    hsv_pixels = hsv.reshape(-1, 3)
    hsv_pixels = hsv_pixels[np.any(hsv_pixels != [0, 0, 0], axis=1)]  # remove black bg
    if len(hsv_pixels) == 0:
        return None
    dominant = np.mean(hsv_pixels, axis=0).astype(int)
    return tuple(dominant)
