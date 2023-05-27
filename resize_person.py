import cv2
from pytorch_openpose.src.body import Body


# Load the input image
test_image = r'pytorch_openpose/images/1414.jpg'
input_image = cv2.imread(test_image)
# Load the pose estimation model (you can replace this with your own model)
# Load the body pose estimation model
body_estimation = Body(r'C:\Users\מירי\PycharmProjects\newProject\pytorch_openpose\model\body_pose_model.pth')

# Define the target height (in pixels) for the person in the image
target_height = 500

# Get the height and width of the input image
height, width = input_image.shape[:2]

# Create a blob from the input image to feed into the pose estimation model
blob = cv2.dnn.blobFromImage(input_image, 1.0, (width, height), (0, 0, 0), swapRB=True, crop=False)

# Feed the blob into the pose estimation model to get the pose keypoints
pose_keypoints = body_estimation.predict(blob)

# Find the bounding box of the person in the image
min_x, min_y = int(min(pose_keypoints[:, 0])), int(min(pose_keypoints[:, 1]))
max_x, max_y = int(max(pose_keypoints[:, 0])), int(max(pose_keypoints[:, 1]))
person_bbox = (min_x, min_y, max_x - min_x, max_y - min_y)

# Resize the person in the image to the target height while preserving aspect ratio
scale_factor = target_height / person_bbox[3]
resized_width = int(scale_factor * person_bbox[2])
resized_height = target_height
resized_bbox = (person_bbox[0], person_bbox[1], resized_width, resized_height)

# Crop the image to the resized bounding box
resized_image = input_image[resized_bbox[1]:resized_bbox[1]+resized_bbox[3], resized_bbox[0]:resized_bbox[0]+resized_bbox[2]]

# Display the resized image for visualization
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
