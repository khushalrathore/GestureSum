# Sign Language Detector

## Overview

This project is a real-time sign language detector built using a mathematical approach to recognize hand gestures. The detector utilizes concepts such as Heron's formula to calculate the area of triangles formed by the spaces between fingers and Gaussian blur for image processing. The application is built using Flask for the web interface and OpenCV for image and video processing.

## Features

- Real-time hand gesture recognition
- Uses mathematical techniques for accurate detection
- Flask-based web interface for live video feed
- OpenCV for image processing and contour detection

## Installation

To run this project, you need to have Python installed along with the required libraries. Follow the steps below to set up the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/sign-language-detector.git
    cd sign-language-detector
    ```

2. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    python app.py
    ```

## Usage

1. **Start the server:**
    Run the following command in your terminal:
    ```sh
    python app.py
    ```
   
2. **Access the web interface:**
    Open your web browser and go to `http://127.0.0.1:5000/`. You will see a live video feed from your webcam.

3. **Perform hand gestures:**
    The application will detect the number of fingers shown and display corresponding messages.

## Code Explanation

### Main Components

- **Flask Application:**
  - `app.py` initializes the Flask app and defines routes for the homepage and video feed.
  - The `index` function renders the homepage.
  - The `video_feed_route` function streams the processed video feed.

- **Hand Gesture Recognition:**
  - The `hand_recognizer` function processes each frame, identifying hand gestures by calculating contour areas and defects using Heron's formula.

- **Video Feed:**
  - The `video_feed` function captures video frames from the webcam, processes them using `hand_recognizer`, and streams the processed frames to the web interface.

### Key Techniques

- **Heron's Formula:**
  Used to calculate the area of triangles formed by defects in the convex hull of the hand contour, helping in gesture recognition.

- **Gaussian Blur:**
  Applied to smooth the image and reduce noise, aiding in better contour detection.

- **Convex Hull and Defects:**
  Used to find the outer boundary of the hand and the spaces between fingers, respectively.

## Acknowledgements

This project was developed in collaboration with [Arjun](https://github.com/justasharma), who contributed significantly to the mathematical modeling and algorithm development.

---

This README is designed to provide a clear and concise overview of the project for potential employers and collaborators. It highlights the technical aspects and innovative approaches used in the project.