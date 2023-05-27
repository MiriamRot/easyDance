import numpy as np

from pytorch_openpose.src.body import Body


NUM_KEYS_POINTS = 18

body_estimation = Body(r'C:\Users\מירי\Documents\תיכנות\שנה ב\פרויקט גמר\open pose\pytorch_openpose\model\body_pose_model.pth')


class Create_Matrix():
    def __init__(self, matrix):
        self.matrix = matrix

    def create_matrix(self, frame, id_frame):
        print('id_frmae:', id_frame, self.matrix)
        for j in range(NUM_KEYS_POINTS):
            candidate, subset = body_estimation(frame)
            x, y = candidate[j, :2]
            self.matrix[id_frame, j] = (x, y)
