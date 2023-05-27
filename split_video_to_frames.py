import cv2
import os

def split_video_to_frames(video_path, output_directory, frame_rate=4):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Get the frame rate of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate the frame interval based on the desired frame rate
    frame_interval = int(fps / frame_rate)

    # Read and save each frame of the video
    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if no frame was retrieved
        if not ret:
            break

        # Save the frame as an image file
        if frame_count % frame_interval == 0:
            frame_filename = f"frame_{frame_count}.jpg"
            frame_path = os.path.join(output_directory, frame_filename)
            cv2.imwrite(frame_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Split video into {frame_count} frames")

# Example usage:
video_path = r"C:/Users/מירי/Desktop/111.mp4"
output_directory = "pytorch_openpose/frames"
split_video_to_frames(video_path, output_directory, 20)
