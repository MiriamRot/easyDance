#import cv2
import datetime
now = datetime.datetime.now()
print(now)
import matplotlib.pyplot as plt
import copy
import numpy as np
import os
#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

#from pytorch_openpose.src import model
from pytorch_openpose.src import util
from pytorch_openpose.src.body import Body
#from pytorch_openpose.src.hand import Hand

now = datetime.datetime.now()
print(1, now)

body_estimation = Body(r'C:\Users\מירי\Documents\תיכנות\שנה ב\פרויקט גמר\open pose\pytorch_openpose\model\body_pose_model.pth')
#hand_estimation = Hand(r'C:\Users\מירי\Documents\תיכנות\שנה ב\פרויקט גמר\open pose\pytorch_openpose\model\hand_pose_model.pth')


#test_image = '/kaggle/input/input-poses/baseball1.jpg'
test_image = r'C:\Users\מירי\Documents\תיכנות\שנה ב\פרויקט גמר\open pose\pytorch_openpose\images\baseball1.jpg'


# Specify the path of the folder you want to display
#path = r'C:/Users/מירי/Documents/תיכנות/שנה ב/פרויקט גמר/open pose/pytorch_openpose/images'

# Use the listdir() function to get a list of files and folders in the specified path
#files = os.listdir(path)

# Print the list of files and fo lders
#print(files)


image = plt.imread(test_image)
#image = cv2.imread(test_image)
#plt.figure(figsize=(10, 10))
#plt.imshow(image)
#plt.axis('off')
#plt.show()

#keypoints index : index = int(subset[n][i])
#keypoints corrd : x,y = candidate[index][0:2]

# enable GPU for acceleration
#oriImg = cv2.imread(test_image, cv2.IMREAD_UNCHANGED)
# print(oriImg)
# plt.imshow(oriImg)

candidate, subset = body_estimation(image)
print(candidate)
left_shoulder_idx = 5# index of the left shoulder keypoint
person_idx = 2  # index of the first person detected in the image

x, y = candidate[left_shoulder_idx, :2]


canvas = copy.deepcopy(image)
canvas = util.draw_bodypose(canvas, candidate, subset)
#print(len(candidate)) # number of keypoints
#print(len(subset))    # number of persons

# detect hand
#hands_list = util.handDetect(candidate, subset, image)
# all_hand_peaks = []
# for x, y, w, is_left in hands_list:
#     peaks = hand_estimation(image[y:y+w, x:x+w, :])
#     peaks[:, 0] = np.where(peaks[:, 0] == 0, peaks[:, 0], peaks[:, 0]+x)
#     peaks[:, 1] = np.where(peaks[:, 1] == 0, peaks[:, 1], peaks[:, 1]+y)
#     all_hand_peaks.append(peaks)
#canvas = util.draw_handpose(canvas, all_hand_peaks)
now = datetime.datetime.now()
print(2, now)
plt.figure(figsize=(10, 10))
plt.imshow(canvas[:, :, [2, 1, 0]][..., ::-1])
plt.axis('off')
plt.show()