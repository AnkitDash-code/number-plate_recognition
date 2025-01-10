import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import streamlit as st
import processing
import ai

def app():
    st.title("Image Uploader")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # To read image file buffer with OpenCV:
        input_image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
        cv2.imwrite('image.jpg', input_image)
        sts = 'image.jpg'
    
        # To display the image:
        st.image(uploaded_file, caption="Uploaded Image")

        # To display next image:
        img,approx =processing.loading(sts)
        st.image(img, caption="Number Plate Image")

        #To display Number Plate in text
        text = ai.predict(img)
        T = "Number Plate is "+text
        font = cv2.FONT_HERSHEY_COMPLEX
        res = cv2.putText(input_image, text, org=(approx[0][0][0], approx[0][0][1]+60), fontFace=font, fontScale=1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        res = cv2.rectangle(input_image, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)
        st.image(res, caption=T)

if __name__ == "__main__":
    app()
