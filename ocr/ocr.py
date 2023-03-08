import pytesseract
import pyautogui
import cv2
import numpy as np
import time

# Set up the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the screen region to capture
x, y, w, h = 350, 206, 200, 60

# Set the threshold value
threshold = 200

# Set the OCR engine parameters
config = '--psm 6 --oem 3 -l eng'

ace_count = 0
while True:
    # Capture a screenshot of the region of interest
    screenshot = np.array(pyautogui.screenshot(region=(x, y, w, h)))

    # Convert the screenshot to grayscale
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Apply erosion and dilation to improve the quality of the image
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(screenshot_gray, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)

    # Apply thresholding to the grayscale image
    _, thresholded = cv2.threshold(dilation, threshold, 255, cv2.THRESH_BINARY_INV)

    # Use OCR to extract text from the thresholded image
    text = pytesseract.image_to_string(thresholded, config=config)

    # Check if the word "ACE" is found in the extracted text
    if "ACE" in text:
        ace_count += 1
        print(f"{ace_count} ACE detected, waiting for 5 seconds...")
        time.sleep(5)

    # Display the thresholded image for debugging purposes
#     cv2.imshow("Thresholded Image", thresholded)

    # Wait for a key press to exit the program
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Clean up the OpenCV windows
cv2.destroyAllWindows()