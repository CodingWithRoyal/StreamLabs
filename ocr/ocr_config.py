import pytesseract
import pyautogui
import cv2
import numpy as np

# Set up the tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set the screen region to capture
x, y, w, h = 350, 206, 200, 60

# Capture the screen region
screenshot = pyautogui.screenshot(region=(x, y, w, h))

# Convert the screenshot to a NumPy array
screenshot = np.array(screenshot)

# Display the captured image in a named window
cv2.namedWindow("Captured Image", cv2.WINDOW_NORMAL)
cv2.imshow("Captured Image", screenshot)

cv2.waitKey(0)
cv2.destroyAllWindows()
print('Done')