from pytorch_openpose.src.body import Body
import cv2

image1 = cv2.imread('pytorch_openpose/images/1616.jpg')
image2 = cv2.imread('pytorch_openpose/images/3230.jpg')

# def compare_body_poses(image1, image2):
# Load the body pose estimation model
body_estimation = Body(r'C:\Users\מירי\PycharmProjects\newProject\pytorch_openpose\model\body_pose_model.pth')
# Perform body pose estimation on both images


candidate1, subset1 = body_estimation(image1)
candidate2, subset2 = body_estimation(image2)
print(subset1)
# Define the pairs of points for which you want to compare the slopes
pairs1 = [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]
pairs2 = [(0, 1), (1, 5), (1, 2), (5, 6), (6, 7), (2, 3), (3, 4), (1, 11), (11, 12), (12, 13), (1, 8), (8, 9), (9, 10)]

# Calculate the difference in slopes for each pair of points
differences = {}
for pair1, pair2 in zip(pairs1, pairs2):
    index_a, index_b = pair1
    # index_a, index_b = pair2
    if subset1.any() and subset2.any():
        if subset1[0][index_a] != -1 and subset1[0][index_b] != -1 and subset2[0][index_a] != -1 and subset2[0][index_b]!= -1:

            point_a1 = candidate1[int(subset1[0][index_a]), :2]

            point_b1 = candidate1[int(subset1[0][index_b]), :2]
            point_a2 = candidate2[int(subset2[0][index_a]), :2]
            point_b2 = candidate2[int(subset2[0][index_b]), :2]

            if ((700 - point_b1[1]) - (700 - point_a1[1])) == 0:
                m1 = float('inf')
            else:
                m1 = ((700 - point_b1[1]) - (700 - point_a1[1])) / (point_b1[0] - point_a1[0])

            if ((700 - point_b2[1]) - (700 - point_a2[1])) == 0:
                m2 = float('inf')
            else:
                m2 = ((700 - point_b2[1]) - (700 - point_a2[1])) / (point_b2[0] - point_a2[0])
            # if m2 == 'inf' or m2 == '-inf':

            differences[f"{index_a}-{index_b}"] = m2 - m1

            print(differences[f"{index_a}-{index_b}"])
    # return differences

# image1 = r'pytorch_openpose/images/2020.jpg'
# image2 = r'pytorch_openpose/images/1919.jpg'
# compare_body_poses(image1, image2)

# # def compare_body_poses(image1, image2):
#     # Load the body pose estimation model
# body_estimation = Body(r'C:\Users\מירי\PycharmProjects\newProject\pytorch_openpose\model\body_pose_model.pth')
#     # Perform body pose estimation on both images
#
#
# candidate1, subset1 = body_estimation(image1)
# candidate2, subset2 = body_estimation(image2)
#
#     # Define the pairs of points for which you want to compare the slopes
# #pairs = [(0, 1), (1, 2), (1, 5), (2, 3), (3, 4), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10), (1, 11), (11, 12), (12, 13)]
#
#     # Calculate the difference in slopes for each pair of points
# differences = {}
# pairs = [(2, 3), (5, 6)]
# for pair in pairs:
#     index_a, index_b = pair
#     if subset1.any() and subset2.any():
#         if subset1[0][index_a] != -1 and subset1[0][index_b] != -1 and subset2[0][index_a] != -1 and subset2[0][index_b] != -1:
#             point_a1 = candidate1[int(subset1[0][index_a]), :2]
#             point_b1 = candidate1[int(subset1[0][index_b]), :2]
#             point_a2 = candidate2[int(subset2[0][index_a]), :2]
#             point_b2 = candidate2[int(subset2[0][index_b]), :2]
#
#             if ((700-point_b1[1])-(700-point_a1[1])) == 0:
#                 m1 = float('inf')
#             else:
#                 m1 = ((700-point_b1[1])-(700-point_a1[1]))/(point_b1[0]-point_a1[0])
#
#             if ((700-point_b2[1])-(700-point_a2[1])) == 0:
#                 m2 = float('inf')
#             else:
#                 m2 = ((700-point_b2[1])-(700-point_a2[1]))/(point_b2[0]-point_a2[0])
#
#             differences[f"{index_a}-{index_b}"] = m2 - m1
#
#             print(differences[f"{index_a}-{index_b}"])
