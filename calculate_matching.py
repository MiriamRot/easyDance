
class CalculateMatching():
    """
    A class representing the calculation and comparison of angles between two frames.

    Attributes:
        None

    Methods:
        __init__(): Initializes an instance of the CalculateMatching class.
        compare_2_frames(origin_angles, new_angles): Compares the angles between two frames.

    """

    def __init__(self):
        pass

    def compare_2_frames(self, origin_angles, new_angles):
        """
        Compares the angles between two frames.

        Args:
            origin_angles (dict): A dictionary containing the original frame's angles between body parts.
            new_angles (dict): A dictionary containing the new frame's angles between body parts.

        Returns:
            None
        """
        final_score = 0
        for k in origin_angles.keys():
            print("------------")
            print(k)
            if "Left" in k:
                new_key = k.replace("Left", "Right")
            else:
                new_key = k.replace("Right", "Left")
            score = 0
            # print(new_angles[new_key])
            print(new_key)

            # מייצג את ההפרש שבין זוג השיפועים
            difference_m1 = abs(new_angles[new_key][0] - origin_angles[k][0])
            difference_m2 = abs(new_angles[new_key][1] - origin_angles[k][1])
            direction = new_angles[new_key][3] == origin_angles[k][3]
            print(direction)

            if(difference_m1 < 2 and difference_m2 < 2) and direction:
                if abs(new_angles[new_key][2] - origin_angles[k][2]) < 20:
                    score += 10
                    print('*****************************')
                    print(score)
                else:
                    score += 5
                    print('*****************************')
                    print(score)
            elif difference_m1 < 2 or difference_m2 < 2:
                score += 2.5
                print('*****************************')
                print(score)
            elif difference_m1 < 5 or difference_m2 < 5:
                score += 1
                print('*****************************')
                print(score)
            else:
                score += 0
                print('*****************************')
                print(score)
            final_score += score
        print(final_score)
        return final_score



    #scores = compare_2_frames(origin_frame, new_frame)
    # print(final_score)
# Create an instance of the CalculateMatching class
calculator = CalculateMatching()

origin_angles = {'Nose_Neck_LeftShoulder': (19.25, -0.10909090909090909, 86.74790201805433, 'counterclockwise'),
                 'Nose_Neck_RightShoulder': (19.25, -0.08, 88.39980982257926, 'counterclockwise'),
                 'Neck_RightShoulder_RightElbow': (0.28, 0.28, 0.0, 'counterclockwise'),
                 'RightShoulder_RightElbow_RightWrist': (0.28, 0.2361111111111111, 2.357379972306539, 'counterclockwise'),
                 'Neck_LeftShoulder_LeftElbow': (-0.10909090909090909, -0.576271186440678, 23.727779103375727, 'counterclockwise'),
                 'LeftShoulder_LeftElbow_LeftWrist': (-0.576271186440678, -0.06896551724137931, 26.00842193876393, 'clockwise'),
                 'Neck_RightHip_RightKnee': (6.03030303030303, -10.214285714285714, 15.007184147297513, 'counterclockwise'),
                 'RightHip_RightKnee_RightAnkle': (-10.214285714285714, -5.56, 4.604430491529606, 'clockwise'),
                 'Neck_LeftHip_LeftKnee': (-4.217391304347826, -33.25, 11.616586831740598, 'counterclockwise'),
                 'LeftHip_LeftKnee_LeftAnkle': (-33.25, 26.0, 3.9252602333886077, 'clockwise')}


new_angles = {'Nose_Neck_LeftShoulder': (19.25, -0.08, 88.39980982257926, 'counterclockwise'),
              'Nose_Neck_RightShoulder': (19.25, -0.10909090909090909, 86.74790201805433, 'counterclockwise'),
              'Neck_RightShoulder_RightElbow': (-0.10909090909090909, -0.576271186440678, 23.727779103375727, 'counterclockwise'),
              'RightShoulder_RightElbow_RightWrist': (-0.576271186440678, -0.06896551724137931, 26.00842193876393, 'clockwise'),
              'Neck_LeftShoulder_LeftElbow': (0.28, 0.28, 0.0, 'counterclockwise'),
              'LeftShoulder_LeftElbow_LeftWrist': (0.28, 0.2361111111111111, 2.357379972306539, 'counterclockwise'),
              'Neck_RightHip_RightKnee': (-4.217391304347826, -33.25, 11.616586831740598, 'counterclockwise'),
              'RightHip_RightKnee_RightAnkle': (-33.25, 26.0, 3.9252602333886077, 'clockwise'),
              'Neck_LeftHip_LeftKnee': (6.03030303030303, -10.214285714285714, 15.007184147297513, 'counterclockwise'),
              'LeftHip_LeftKnee_LeftAnkle': (-10.214285714285714, -5.56, 4.604430491529606, 'clockwise')}


# Call the compare_2_frames method and capture the final_score value
final_score = calculator.compare_2_frames(origin_angles, new_angles)

# Print the final_score value
print(final_score)