import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

def loading(input_image):
    # Image loading
    img = cv2.imread(input_image)
    # greyscale filter 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #new_img = (cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)) #for testing
    #Noise reduction
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) 
    #Edge detection
    edged = cv2.Canny(bfilter, 30, 200) #change till detection
    #new_img = cv2.cvtColor(edged, cv2.COLOR_BGR2RGB) # for testing
    # all contours detection
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10] #change till detection
    # Numberplate location detection
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True) # change till detection
        if len(approx) == 4:
            location = approx
            break
    # Masking
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    # Isolation
    (x,y) = np.where(mask==255)
    (x1,y1) = (np.min(x), np.min(y))
    (x2,y2) = (np.max(x), np.max(y))
    isolated_image = gray[x1:x2+1, y1:y2+1]

    return isolated_image,approx