import cv2

import os
from pytorch_openpose.src import util
from pytorch_openpose.src.body import Body
import copy
from PIL import Image
import numpy as np
from pytorch_openpose.create_matrix import Create_Matrix


NUM_KEYS_POINTS = 18


# def create_white_background(background_path: str, width: int, height: int):
#     background_img = Image.new('RGB', (width, height), color="white")
#     background_img.save(background_path)
#     background_np = np.array(background_img)
#     return background_np


def split_video_to_frame(video_path: str, frames_directory: str, body_estimation: Body):#, background_path:str):
    # Open the video file
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    if fps != 0:
        FRAMES_COUNT = int(num_frames / fps)
    else:
        # Handle the case when fps is zero
        FRAMES_COUNT = 0  # or any other appropriate value
    #FRAMES_COUNT = int(num_frames/fps)

    # Check if the video was successfully opened
    if not video.isOpened():
        print('Error opening video file')
        exit()

    # Create a directory to save the frames
    if not os.path.exists(frames_directory):
        os.makedirs(frames_directory)
    interval = 1.0
    # Initialize variables
    frame_count = 0
    success = True
    matrix = np.zeros((FRAMES_COUNT, NUM_KEYS_POINTS), dtype=object)
    matrix_object = Create_Matrix(matrix)
    # Loop through the video frames
    while success:
        # Read a frame
        success, frame = video.read()
        width, height, _ = frame.shape
        # Check if the frame was successfully read
        if not success:
            break

        if frame is None:
            # Skip this frame if it's invalid
            continue
        # Skip this frame if it's invalid
        # if frame_count == 0:
            # back = create_white_background(background_path, width, height)
            # print(back.shape)
        # Save the frame as an image file
        # if frame_count % int(interval * fps) == 0:
        #filename #= f'{frames_directory}/frame_{frame_count:04d}.jpg'
            # matrix_object.create_matrix(frame, frame_count/fps, matrix)
        frame_count += 1
        # candidate, subset = body_estimation(frame)
        # canvas = copy.deepcopy(frame)
        # canvas = util.draw_bodypose(back, candidate, subset)
        # cv2.imwrite(filename, canvas)
    # Release the video and close the window
    video.release()
    cv2.destroyAllWindows()


video_path = r'C:\Users\מירי\Desktop\513.mp4'
frames_directory = 'detects_frames'
body_estimation = Body(
    r'C:\Users\מירי\Documents\תיכנות\שנה ב\פרויקט גמר\open pose\pytorch_openpose\model\body_pose_model.pth')
# background_path = 'white_back.png'
split_video_to_frame(video_path, frames_directory, body_estimation) #, background_path)

