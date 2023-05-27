import datetime
import matplotlib.pyplot as plt
import cv2
import copy
from PIL import Image
import numpy as np8
from pytorch_openpose.src import util
from pytorch_openpose.src.body import Body

now = datetime.datetime.now()

# Load the body pose estimation model
body_estimation = Body(r'C:\Users\מירי\PycharmProjects\newProject\pytorch_openpose\model\body_pose_model.pth')

# Load the test image
test_image = r'pytorch_openpose/images/511.jpg'
image = Image.open(test_image)

# Resize the image
new_size = (1280, 720)
img_resized = image.resize(new_size)

# Convert the PIL image back to a numpy array
img_resized = np.array(img_resized)
# image = cv2.imread(test_image)
# # Resize the image
# new_size = (1280, 720)
# img_resized = cv2.resize(image, new_size)
print(img_resized.shape)
# print(image.shape)

# # Resize the image to a certain size
# image = cv2.resize(image, (800, 600))
#
# # Set a certain point for the key point of the nose
# nose_keypoint = (400, 300)  # (x, y) coordinates of the key point of the nose
#
# # Draw a circle on the key point of the nose
# image = cv2.circle(image, nose_keypoint, 5, (0, 255, 0), -1)

# Perform body pose estimation
# candidate, subset = body_estimation(image)
candidate, subset = body_estimation(img_resized)

print(f'subset, {subset}')
# Print the pairs of points for each person detected in the image
#for person in subset:
# Print the coordinates of the key points for each body part pair
if subset.any():
    print("nobody here")
person_subset = subset[0]
# print(image.shape)
print(img_resized.shape)

image2 = cv2.line(img_resized, (480, 317), (479, 367), (0,  0, 255), 10)
plt.imshow(image2)
plt.show()
for pair in [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]:
    index_a, index_b = pair
    if person_subset[index_a] != -1 and person_subset[index_b] != -1:
        point_a = candidate[int(person_subset[index_a]), :2]
        point_b = candidate[int(person_subset[index_b]), :2]
        if ((700-point_b[1])-(700-point_a[1])) == 0:
            m = float('inf')
        else:
            m = ((700-point_b[1])-(700-point_a[1]))/(point_b[0]-point_a[0])
        print(f"{index_a}-{index_b}: {point_a}, {point_b}")
        print(f"m:{m}")


# Visualize the result
canvas = copy.deepcopy(img_resized)
canvas = util.draw_bodypose(canvas, candidate, subset)
plt.figure(figsize=(10, 10))
plt.imshow(canvas[:, :, [2, 1, 0]])
plt.axis('off')
plt.show()
# rgb->bgr [..., ::-1]