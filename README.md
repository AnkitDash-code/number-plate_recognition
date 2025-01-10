# Number Plate Recognition Application

## Overview

This project is a web-based number plate recognition application. Users can upload images of vehicles, and the application detects and extracts the text from the vehicle's number plate using computer vision and OCR technologies. The processed results are displayed back to the user with the detected number plate text overlayed on the image.

## Features

- Upload an image in `.jpg`, `.jpeg`, or `.png` format.
- Detects the number plate region from the uploaded image.
- Extracts text from the number plate using Optical Character Recognition (OCR).
- Displays the original image with the detected number plate region and the extracted text overlayed.

## Tech Stack

- **Frontend**: Streamlit for a simple and interactive web-based user interface.
- **Backend**: OpenCV for image processing and EasyOCR for text extraction.
- **Languages**: Python.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or above

### Steps

1. Clone the repository.
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run main.py
   ```
5. Access the app in your browser at `http://localhost:8501`.

## Project Structure

- **`main.py`**: Handles the frontend interface and integrates backend processing with the user interface.
- **`processing.py`**: Contains the functions for image preprocessing and number plate detection.
- **`ai.py`**: Implements OCR for extracting text from the detected number plate region.
- **`requirements.txt`**: Lists all the dependencies needed to run the application.

## Dependencies

- `streamlit`: For creating the web interface.
- `matplotlib`: For visualizing processed images (optional in this project).
- `cv2` (OpenCV): For image processing.
- `easyocr`: For Optical Character Recognition (OCR).
- `pytorch`: Backend dependency for EasyOCR.

## How It Works

1. The user uploads an image.
2. The application reads and processes the image to detect the number plate region.
3. Text is extracted from the detected region using OCR.
4. The processed image with overlayed text is displayed back to the user.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [OpenCV](https://opencv.org/)
- [Streamlit](https://streamlit.io/)

