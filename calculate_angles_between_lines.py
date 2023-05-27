import datetime
import matplotlib.pyplot as plt
import cv2
import copy
from PIL import Image
import numpy as np
from pytorch_openpose.src import util
from pytorch_openpose.src.body import Body
import math
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




def calculateEquationsOfStraightLine(crd1, crd2):
    if len(crd1) == 0 or len(crd2) == 0:
        return 'unidentified'
    if ((crd1[0]) - (crd2[0])) == 0:
        slope = float('inf')
        # y_intercept = 0
    else:
        slope = ((720 - crd1[1]) - (720 - crd2[1])) / (crd1[0] - crd2[0])
        print(crd1, crd2)
        # y_intercept = (crd1[1]) - slope * crd1[0]
    return slope# ,y_intercept


def getCoordinates(subset_index):
    if person_subset[subset_index] != -1:
        return candidate[int(person_subset[subset_index]), :2]
    return []


def angleBetweenLines(m1, m2):
    if m1 == 'unidentified' or m2 == 'unidentified':
        return 'unidentified'
    print(m1, m2)
    theta = math.atan(abs((m2 - m1) / (1 + m1 * m2)))

    angle_degrees = math.degrees(theta)
    if m2 > m1:
        direction = "clockwise"
    else:
        direction = "counterclockwise"
    return m1, m2, angle_degrees, direction,

person_subset = subset[0]

limbs = {
    "Nose": getCoordinates(0),            #point_a = candidate[int(person_subset[index_a]), :2]
    "Neck": getCoordinates(1),
    "RightShoulder": getCoordinates(2),
    "RightElbow": getCoordinates(3),
    "RightWrist": getCoordinates(4),
    "LeftShoulder": getCoordinates(5),
    "LeftElbow": getCoordinates(6),
    "LeftWrist": getCoordinates(7),
    "RightHip": getCoordinates(8),
    "RightKnee": getCoordinates(9),
    "RightAnkle": getCoordinates(10),
    "LeftHip": getCoordinates(11),
    "LeftKnee": getCoordinates(12),
    "LeftAnkle": getCoordinates(13),
}
# [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]
Slopes = {
    "Nose_Neck": calculateEquationsOfStraightLine(limbs["Nose"], limbs["Neck"]),
    "Neck_RightShoulder": calculateEquationsOfStraightLine(limbs["Neck"], limbs["RightShoulder"]),
    "Neck_LeftShoulder": calculateEquationsOfStraightLine(limbs["Neck"], limbs["LeftShoulder"]),
    "RightShoulder_RightElbow": calculateEquationsOfStraightLine(limbs["RightShoulder"], limbs["RightElbow"]),
    "RightElbow_RightWrist": calculateEquationsOfStraightLine(limbs["RightElbow"], limbs["RightWrist"]),
    "LeftShoulder_LeftElbow": calculateEquationsOfStraightLine(limbs["LeftShoulder"], limbs["LeftElbow"]),
    "LeftElbow_LeftWrist": calculateEquationsOfStraightLine(limbs["LeftElbow"], limbs["LeftWrist"]),
    "Neck_RightHip": calculateEquationsOfStraightLine(limbs["Neck"], limbs["RightHip"]),
    "RightHip_RightKnee": calculateEquationsOfStraightLine(limbs["RightHip"], limbs["RightKnee"]),
    "RightKnee_RightAnkle": calculateEquationsOfStraightLine(limbs["RightKnee"], limbs["RightAnkle"]),
    "Neck_LeftHip": calculateEquationsOfStraightLine(limbs["Neck"], limbs["LeftHip"]),
    "LeftHip_LeftKnee": calculateEquationsOfStraightLine(limbs["LeftHip"], limbs["LeftKnee"]),
    "LeftKnee_LeftAnkle": calculateEquationsOfStraightLine(limbs["LeftKnee"], limbs["LeftAnkle"])
}



Angles = {
    "Nose_Neck_LeftShoulder": angleBetweenLines(Slopes["Nose_Neck"],
                                                Slopes["Neck_LeftShoulder"]),
    "Nose_Neck_RightShoulder": angleBetweenLines(Slopes["Nose_Neck"],
                                                   Slopes["Neck_RightShoulder"]),
    "Neck_RightShoulder_RightElbow": angleBetweenLines(Slopes["RightShoulder_RightElbow"],
                                                         Slopes["RightShoulder_RightElbow"]),
    "RightShoulder_RightElbow_RightWrist": angleBetweenLines(Slopes["RightShoulder_RightElbow"],
                                                               Slopes["RightElbow_RightWrist"]),
    "Neck_LeftShoulder_LeftElbow": angleBetweenLines(Slopes["Neck_LeftShoulder"],
                                                       Slopes["LeftShoulder_LeftElbow"]),
    "LeftShoulder_LeftElbow_LeftWrist": angleBetweenLines(Slopes["LeftShoulder_LeftElbow"],
                                                            Slopes["LeftElbow_LeftWrist"]),
    "Neck_RightHip_RightKnee": angleBetweenLines(Slopes["Neck_RightHip"],
                                                   Slopes["RightHip_RightKnee"]),
    "RightHip_RightKnee_RightAnkle": angleBetweenLines(Slopes["RightHip_RightKnee"],
                                                         Slopes["RightKnee_RightAnkle"]),
    "Neck_LeftHip_LeftKnee": angleBetweenLines(Slopes["Neck_LeftHip"],
                                                 Slopes["LeftHip_LeftKnee"]),
    "LeftHip_LeftKnee_LeftAnkle": angleBetweenLines(Slopes["LeftHip_LeftKnee"],
                                                      Slopes["LeftKnee_LeftAnkle"])
}


Angles2 = {
    "Nose_Neck_LeftShoulder" : angleBetweenLines(Slopes["Nose_Neck"],
                                                   Slopes["Neck_LeftShoulder"]),
    "Nose_Neck_RightShoulder": angleBetweenLines(Slopes["Nose_Neck"],
                                                   Slopes["Neck_RightShoulder"]),
    "Neck_RightShoulder_RightElbow": angleBetweenLines(Slopes["RightShoulder_RightElbow"],
                                                         Slopes["RightShoulder_RightElbow"]),
    "RightShoulder_RightElbow_RightWrist": angleBetweenLines(Slopes["RightShoulder_RightElbow"],
                                                               Slopes["RightElbow_RightWrist"]),
    "Neck_LeftShoulder_LeftElbow": angleBetweenLines(Slopes["Neck_LeftShoulder"],
                                                       Slopes["LeftShoulder_LeftElbow"]),
    "LeftShoulder_LeftElbow_LeftWrist": angleBetweenLines(Slopes["LeftShoulder_LeftElbow"],
                                                            Slopes["LeftElbow_LeftWrist"]),
    "Neck_RightHip_RightKnee": angleBetweenLines(Slopes["Neck_RightHip"],
                                                   Slopes["RightHip_RightKnee"]),
    "RightHip_RightKnee_RightAnkle": angleBetweenLines(Slopes["RightHip_RightKnee"],
                                                         Slopes["RightKnee_RightAnkle"]),
    "Neck_LeftHip_LeftKnee": angleBetweenLines(Slopes["Neck_LeftHip"],
                                                 Slopes["LeftHip_LeftKnee"]),
    "LeftHip_LeftKnee_LeftAnkle": angleBetweenLines(Slopes["LeftHip_LeftKnee"],
                                                      Slopes["LeftKnee_LeftAnkle"])
}

def compare_2_frames(origin_angels,new_angels):
    for k in origin_angels.keys():
        print("------------")
        print(k)
        if "Left" in k:
            new_key = k.replace("Left","Right")
        else:
            new_key = k.replace("Right","Left")

        print(new_angels[new_key])
        print(new_key)
        mark = 0
        m1_e = new_angels[new_key][0] - origin_angels[k][0]
        m2_e = new_angels[new_key][1] - origin_angels[k][1]
        if m1_e < 10 and m2_e < 10:
            if new_angels[new_key][3] - origin_angels[k][3]:
                mark += 0
            else:
                mark += 0
        else:
            mark += 0


#
# def getAngels(frame)
# return []


# angel1=getAngels(f1)
# angel2=getAngels(f2)


# Angles = (
#     ( "Nose_Neck_RightShoulder", angleBetweenLines(Slopes["Nose_Neck"],
#                                                    Slopes["Neck_RightShoulder"])),
#     ("Neck_RightShoulder_RightElbow", angleBetweenLines(Slopes["RightShoulder_RightElbow"],
#                                                          Slopes["RightShoulder_RightElbow"])),
#     ( "RightShoulder_RightElbow_RightWrist", angleBetweenLines(Slopes["RightShoulder_RightElbow"],
#                                                                Slopes["RightElbow_RightWrist"])),
#     ("Neck_LeftShoulder_LeftElbow", angleBetweenLines(Slopes["Neck_LeftShoulder"],
#                                                        Slopes["LeftShoulder_LeftElbow"])),
#     ("LeftShoulder_LeftElbow_LeftWrist", angleBetweenLines(Slopes["LeftShoulder_LeftElbow"],
#                                                             Slopes["LeftElbow_LeftWrist"])),
#     ("Neck_RightHip_RightKnee", angleBetweenLines(Slopes["Neck_RightHip"],
#                                                    Slopes["RightHip_RightKnee"])),
#     ("RightHip_RightKnee_RightAnkle", angleBetweenLines(Slopes["RightHip_RightKnee"],
#                                                          Slopes["RightKnee_RightAnkle"])),
#     ("Neck_LeftHip_LeftKnee", angleBetweenLines(Slopes["Neck_LeftHip"],
#                                                  Slopes["LeftHip_LeftKnee"])),
#     ("LeftHip_LeftKnee_LeftAnkle", angleBetweenLines(Slopes["LeftHip_LeftKnee"],
#                                                       Slopes["LeftKnee_LeftAnkle"]))
# )
#
# Angles2 = (
#     ( "Nose_Neck_RightShoulder", angleBetweenLines(Slopes["Nose_Neck"],
#                                                    Slopes["Neck_RightShoulder"])),
#     ("Neck_RightShoulder_RightElbow", angleBetweenLines(Slopes["RightShoulder_RightElbow"],
#                                                          Slopes["RightShoulder_RightElbow"])),
#     ( "RightShoulder_RightElbow_RightWrist", angleBetweenLines(Slopes["RightShoulder_RightElbow"],
#                                                                Slopes["RightElbow_RightWrist"])),
#     ("Neck_LeftShoulder_LeftElbow", angleBetweenLines(Slopes["Neck_LeftShoulder"],
#                                                        Slopes["LeftShoulder_LeftElbow"])),
#     ("LeftShoulder_LeftElbow_LeftWrist", angleBetweenLines(Slopes["LeftShoulder_LeftElbow"],
#                                                             Slopes["LeftElbow_LeftWrist"])),
#     ("Neck_RightHip_RightKnee", angleBetweenLines(Slopes["Neck_RightHip"],
#                                                    Slopes["RightHip_RightKnee"])),
#     ("RightHip_RightKnee_RightAnkle", angleBetweenLines(Slopes["RightHip_RightKnee"],
#                                                          Slopes["RightKnee_RightAnkle"])),
#     ("Neck_LeftHip_LeftKnee", angleBetweenLines(Slopes["Neck_LeftHip"],
#                                                  Slopes["LeftHip_LeftKnee"])),
#     ("LeftHip_LeftKnee_LeftAnkle", angleBetweenLines(Slopes["LeftHip_LeftKnee"],
#                                                       Slopes["LeftKnee_LeftAnkle"]))
# )


#
#
# def compareTwoFrames(candidate1, candidate2):
#     for




#
# for key, value in Angles.items():
#     print(key, value)

print(f'subset, {subset}')
# Print the pairs of points for each person detected in the image
# for person in subset:
# Print the coordinates of the key points for each body part pair
if subset.any():
    print("nobody here")
# print(image.shape)
print(img_resized.shape)

image2 = cv2.line(img_resized, (480, 317), (479, 367), (0, 0, 255), 10)
plt.imshow(image2)
plt.show()

# for pair in [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]:
#     index_a, index_b = pair
#
#     if person_subset[index_a] != -1 and person_subset[index_b] != -1:
#         point_a = candidate[int(person_subset[index_a]), :2]
#         point_b = candidate[int(person_subset[index_b]), :2]
#         if ((700 - point_b[1]) - (700 - point_a[1])) == 0:
#             m = float('inf')
#         else:
#             m = ((700 - point_b[1]) - (700 - point_a[1])) / (point_b[0] - point_a[0])
#         print(f"{index_a}-{index_b}: {point_a}, {point_b}")
#         print(f"m:{m}")
#         vector_a = np.array(point_a)
#         vector_b = np.array(point_b)
#         angle_degrees = math
#         print(angle_degrees)

# import math
#
# pairs1 = [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]
#
#
#
#
#
# theta = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
#             angle_degrees = math.degrees(theta)
#             if m2 > m1:
#                     direction = "clockwise"
#             else:
#                     direction = "counterclockwise"
#             print(angle_degrees, direction)

# m1 = 2
# m2 = 1
# c1 = -0.5
# c2 = 3
# def angleBetweenLines(m1, c1, m2, c2):
# theta = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
# return math.degrees(theta)
# angle_degrees = math.degrees(theta)
# if m2 > m1:
#         direction = "clockwise"
# else:
#         direction = "counterclockwise"

# Example usage
# angle_degrees = angleBetweenLines(2, 1, -0.5, 3)
# print(angle_degrees, direction)

if __name__ == "__main__":
    print(Angles)
    # print("******88", calculateEquationsOfStraightLine([1, 4], [1, 4]))
    # print("******88", calculateEquationsOfStraightLine([1, 2], [3, 4]))

    # compare_2_frames(Angles, Angles2)

