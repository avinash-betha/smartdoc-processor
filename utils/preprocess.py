import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    # Denoise
    denoised = cv2.medianBlur(thresh, 3)

    # Optional: Deskew (not yet implemented)

    return denoised
