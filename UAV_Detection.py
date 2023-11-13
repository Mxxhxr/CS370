import cv2
import os
from keras_yolo3.yolo import YOLO

yolo = YOLO()

def detect_objects(frame):
    #perform object detection on the frame using YOLO
    detected_objects = yolo.detect_image(frame)

    return detected_objects

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        #perform object detection on the current frame
        detections = detect_objects(frame)

        if detections:
            #save frames with detections in the 'detections' folder
            cv2.imwrite(f'detections/frame_{frame_count}.jpg', frame)

        frame_count += 1

    cap.release()

def process_videos_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.mp4'):
            video_path = os.path.join(directory_path, filename)
            process_video(video_path)

if __name__ == "__main__":
    video1 = "Drone_Tracking_1.mp4"
    process_videos_in_directory(video1)

    video2 = "Drone_tracking_2.mp4"
    process_videos_in_directory(video2)