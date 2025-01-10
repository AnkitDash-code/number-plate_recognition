import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr

def predict(img):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(img)
    final = result[0][-2]
    return final