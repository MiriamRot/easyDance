import math


class FrameDetails():
    """
    A class representing frame details for body pose estimation.

    Attributes:
        None

    Methods:
        __init__(): Initializes an instance of the FrameDetails class.
        calculate_slops_of_straight_line(crd1, crd2): Calculates the equation of a straight line given two points.
        get_coordinates(subset_index, person_subset, candidate): Retrieves the coordinates of a body part from the candidate.
        angle_between_lines(m1, m2): Calculates the angle between two lines.
        get_frame_details(candidates, subset): Retrieves the details of a frame, including angles between body parts.
    """

    def __init__(self):
        """
        Initializes an instance of the FrameDetails class.

        Args:
            None

        Returns:
            None
        """
        pass

    def calculate_slops_of_straight_line(self, crd1, crd2):
        """
        Calculates the slops of a straight line given two points.

        Args:
            crd1 (list): The coordinates of the first point [x, y].
            crd2 (list): The coordinates of the second point [x, y].

        Returns:
            slope (float): The slope of the line passing through the two points.
        """
        if len(crd1) == 0 or len(crd2) == 0:
            return 'unidentified'
        if ((crd1[0]) - (crd2[0])) == 0:
            slope = float('inf')
            # y_intercept = 0
        else:
            slope = ((- crd1[1]) + crd2[1]) / (crd1[0] - crd2[0])
            print(crd1, crd2)
            # y_intercept = (crd1[1]) - slope * crd1[0]
        return slope  # ,y_intercept

    def get_coordinates(self, subset_index, person_subset, candidate):
        """
        Retrieves the coordinates of a body part from the candidate.

        Args:
            subset_index (int): The index of the body part in the person subset.
            person_subset (list): The subset containing body part indices for a person.
            candidate (list): The candidate containing body part coordinates.

        Returns:
            coordinates (list): The coordinates of the specified body part [x, y].
        """
        if person_subset[subset_index] != -1:
            return candidate[int(person_subset[subset_index]), :2]
        return []

    def angle_between_lines(self, m1, m2):
        """
        Calculates the angle between two lines.

        Args:
            m1 (float): The slope of the first line.
            m2 (float): The slope of the second line.

        Returns:
            angle (tuple): A tuple containing the slopes, angle in degrees, and direction of rotation.
        """
        if m1 == 'unidentified' or m2 == 'unidentified':
            return 'unidentified'
        theta = math.atan(abs((m2 - m1) / (1 + m1 * m2)))
        angle_degrees = math.degrees(theta)
        if m2 > m1:
            direction = "clockwise"
        else:
            direction = "counterclockwise"
        return m1, m2, angle_degrees, direction

    def get_frame_details(self, candidates, subset):
        """
        Calculates the angle between two lines.

        Args:
            m1 (float): The slope of the first line.
            m2 (float): The slope of the second line.

        Returns:
            angle (tuple): A tuple containing the slopes, angle in degrees, and direction of rotation.
        """
        Body_parts = {
            "Nose": self.get_coordinates(0, candidates, subset),  
            "Neck": self.get_coordinates(1, candidates, subset),
            "RightShoulder": self.get_coordinates(2, candidates, subset),
            "RightElbow": self.get_coordinates(3, candidates, subset),
            "RightWrist": self.get_coordinates(4, candidates, subset),
            "LeftShoulder": self.get_coordinates(5, candidates, subset),
            "LeftElbow": self.get_coordinates(6, candidates, subset),
            "LeftWrist": self.get_coordinates(7, candidates, subset),
            "RightHip": self.get_coordinates(8, candidates, subset),
            "RightKnee": self.get_coordinates(9, candidates, subset),
            "RightAnkle": self.get_coordinates(10, candidates, subset),
            "LeftHip": self.get_coordinates(11, candidates, subset),
            "LeftKnee": self.get_coordinates(12, candidates, subset),
            "LeftAnkle": self.get_coordinates(13, candidates, subset),
        }

        Slopes = {
            "Nose_Neck": self.calculate_slops_of_straight_line(Body_parts["Nose"], Body_parts["Neck"]),
            "Neck_RightShoulder": self.calculate_slops_of_straight_line(Body_parts["Neck"], Body_parts["RightShoulder"]),
            "Neck_LeftShoulder": self.calculate_slops_of_straight_line(Body_parts["Neck"], Body_parts["LeftShoulder"]),
            "RightShoulder_RightElbow": self.calculate_slops_of_straight_line(Body_parts["RightShoulder"], Body_parts["RightElbow"]),
            "RightElbow_RightWrist": self.calculate_slops_of_straight_line(Body_parts["RightElbow"], Body_parts["RightWrist"]),
            "LeftShoulder_LeftElbow": self.calculate_slops_of_straight_line(Body_parts["LeftShoulder"], Body_parts["LeftElbow"]),
            "LeftElbow_LeftWrist": self.calculate_slops_of_straight_line(Body_parts["LeftElbow"], Body_parts["LeftWrist"]),
            "Neck_RightHip": self.calculate_slops_of_straight_line(Body_parts["Neck"], Body_parts["RightHip"]),
            "RightHip_RightKnee": self.calculate_slops_of_straight_line(Body_parts["RightHip"], Body_parts["RightKnee"]),
            "RightKnee_RightAnkle": self.calculate_slops_of_straight_line(Body_parts["RightKnee"], Body_parts["RightAnkle"]),
            "Neck_LeftHip": self.calculate_slops_of_straight_line(Body_parts["Neck"], Body_parts["LeftHip"]),
            "LeftHip_LeftKnee": self.calculate_slops_of_straight_line(Body_parts["LeftHip"], Body_parts["LeftKnee"]),
            "LeftKnee_LeftAnkle": self.calculate_slops_of_straight_line(Body_parts["LeftKnee"], Body_parts["LeftAnkle"])
        }

        return {
            "Nose_Neck_LeftShoulder": self.angle_between_lines(Slopes["Nose_Neck"],
                                                               Slopes["Neck_LeftShoulder"]),
            "Nose_Neck_RightShoulder": self.angle_between_lines(Slopes["Nose_Neck"],
                                                                Slopes["Neck_RightShoulder"]),
            "Neck_RightShoulder_RightElbow": self.angle_between_lines(Slopes["RightShoulder_RightElbow"],
                                                                      Slopes["RightShoulder_RightElbow"]),
            "RightShoulder_RightElbow_RightWrist": self.angle_between_lines(Slopes["RightShoulder_RightElbow"],
                                                                            Slopes["RightElbow_RightWrist"]),
            "Neck_LeftShoulder_LeftElbow": self.angle_between_lines(Slopes["Neck_LeftShoulder"],
                                                                    Slopes["LeftShoulder_LeftElbow"]),
            "LeftShoulder_LeftElbow_LeftWrist": self.angle_between_lines(Slopes["LeftShoulder_LeftElbow"],
                                                                         Slopes["LeftElbow_LeftWrist"]),
            "Neck_RightHip_RightKnee": self.angle_between_lines(Slopes["Neck_RightHip"],
                                                                Slopes["RightHip_RightKnee"]),
            "RightHip_RightKnee_RightAnkle": self.angle_between_lines(Slopes["RightHip_RightKnee"],
                                                                      Slopes["RightKnee_RightAnkle"]),
            "Neck_LeftHip_LeftKnee": self.angle_between_lines(Slopes["Neck_LeftHip"],
                                                              Slopes["LeftHip_LeftKnee"]),
            "LeftHip_LeftKnee_LeftAnkle": self.angle_between_lines(Slopes["LeftHip_LeftKnee"],
                                                                   Slopes["LeftKnee_LeftAnkle"])
        }
