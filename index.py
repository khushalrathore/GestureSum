from flask import Flask, render_template, Response
import cv2
import numpy as np
import math

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed_route():
    return Response(video_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Load the hand gesture recognition model
def hand_recognizer(frame):
    try:
        frame = cv2.flip(frame, 1)
        kernel = np.ones((3, 3), np.uint8)

        # Define region of interest
        roi = frame[100:300, 100:300]

        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # Define range of skin color in HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)

        # Extract skin color image
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Extrapolate the hand to fill dark spots within
        mask = cv2.dilate(mask, kernel, iterations=4)

        # Blur the image
        mask = cv2.GaussianBlur(mask, (5, 5), 100)

        # Find contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find contour of max area (hand)
        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        # Approximate the contour a little
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # Make convex hull around hand
        hull = cv2.convexHull(cnt)

        # Define area of hull and area of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)

        # Find the percentage of area not covered by hand in convex hull
        arearatio = ((areahull - areacnt) / areacnt) * 100

        # Find the defects in convex hull with respect to hand
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)

        # Number of defects
        l = 0

        # Code for finding number of defects due to fingers
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])

            # Find length of all sides of triangle
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            s = (a + b + c) / 2
            ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

            # Distance between point and convex hull
            d = (2 * ar) / a

            # Apply cosine rule
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

            # Ignore angles > 90 and points very close to convex hull
            if angle <= 90 and d > 30:
                l += 1

        l += 1

        # Print corresponding gestures
        if l == 1:
            if areacnt < 2000:
                text = ''
            elif arearatio < 12:
                text = '0'
            elif arearatio < 17.5:
                text = 'Best of luck'
            else:
                text = '1'
        elif l == 2:
            text = '2'
        elif l == 3:
            if arearatio < 27:
                text = '3'
            else:
                text = 'ok'
        elif l == 4:
            text = '4'
        elif l == 5:
            text = '5'
        elif l == 6:
            text = 'reposition'
        else:
            text = 'reposition'

        # Draw text on the frame
        cv2.putText(frame, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)

        return frame

    except Exception as e:
        print("Error:", str(e))
        return frame

def video_feed():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame = hand_recognizer(frame)
        ret, buffer = cv2.imencode('.jpg', processed_frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

if __name__ == '__main__':
    app.run(debug=True)
