###### PART 1 ######

import cv2
import os
from keras_yolo3.yolo import YOLO
from filterpy.kalman import KalmanFilter
import numpy as np

def detectObjects(yolo, frame):
    detectedObjects = yolo.detect_image(frame)
    return detectedObjects

def processVid(yolo, vidDirectory):
    cap = cv2.VideoCapture(vidDirectory)
    frameCnt = 0


    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detectObjects(yolo, frame)

        if detections:
            cv2.imwrite(f'detections/{os.path.basename(vidDirectory)}_frame_{frameCnt}.jpg', frame)

        frame_count += 1
    cap.release()

def processVids(yolo, vidDirectory):

    for filename in os.listdir(vidDirectory):
        if filename.endswith('.mp4'):
            vidDirectory = os.path.join(vidDirectory, filename)
            processVid(yolo, vidDirectory)

#### main moved to part 2 ####
# if __name__ == "__main__":

    # yolo = YOLO()
    # vidDirectory = "path/to/videos"
    # processVids(yolo, vidDirectory)


############ PART 2 ############
def initKFilter():

    kFilter = KalmanFilter(dim_x=4, dim_z=2)
    kFilter.x = np.array([0, 0, 0, 0])  #[x1, x2, y1, y2]
    kFilter.P *= 1e-2 
    kFilter.R = np.array([[1, 0], [0, 1]])
    kFilter.H = np.array([[1, 0, 0, 0], [0, 0, 1, 0]])

    return kFilter

def updateKalmanFilter(kFilter, detection):

    kFilter.predict()
    kFilter.update(detection)

def drawTrajectories(frame, trajectory):

    for i in range(1, len(trajectory)):
        cv2.line(frame, tuple(trajectory[i - 1]), tuple(trajectory[i]), (0, 255, 0), 2)

def processVid(yolo, kFilter, vidDirectory):
    cap = cv2.VideoCapture(vidDirectory)
    frameCnt = 0
    trajectory = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detectObjects(yolo, frame)

        if detections:
            detection = detections[0]
            updateKalmanFilter(kFilter, np.array([detection['box'][0], detection['box'][1]]))
            predictedState = kFilter.x.astype(int)
            trajectory.append((predictedState[0], predictedState[2]))
            cv2.rectangle(frame, (detection['box'][0], detection['box'][1]), (detection['box'][2], detection['box'][3]), (255, 0, 0), 2)
            drawTrajectories(frame, trajectory)
            cv2.imwrite(f'tracked/frame_{frameCnt}.jpg', frame)

        frameCnt += 1

    cap.release()

def processVid(yolo, kFilter, vidDirectory):
    for filename in os.listdir(vidDirectory):
        if filename.endswith('.mp4'):
            vidDirectory = os.path.join(vidDirectory, filename)
            processVid(yolo, kFilter, vidDirectory)


if __name__ == "__main__":
    yolo = YOLO()

    kFilter = initKFilter()

    vidDirectory = "UavTracking/Drone tracking 2.mp4"

    processVid(yolo, kFilter, vidDirectory)