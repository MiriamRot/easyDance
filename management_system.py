from calculate_matching import CalculateMatching
from create_movement_details import FrameDetails
from pytorch_openpose.src.body import Body

class ManagementSystem():
    """
    A class representing a management system for body pose estimation and matching.

    Attributes:
        None

    Methods:
        __init__(): Initializes an instance of the ManagementSystem class.
        load_model(): Loads the body pose estimation model.
        get_mark_for_two_frames(): Computes the mark for two frames by performing body pose estimation and matching.
    """
    def __init__(self):
        """
        Initializes an instance of the ManagementSystem class.

         Args:
             None

         Returns:
            None
         """
        pass

    def load_model(self):
        """
        Loads the body pose estimation model.

        Args:
            None

        Returns:
            body_estimation (Body): An instance of the Body class representing the loaded body pose estimation model.
        """
         # Load the body pose estimation model
        body_estimation = Body(r'C:\Users\מירי\PycharmProjects\newProject\pytorch_openpose\model\body_pose_model.pth')
        return body_estimation

    # frame = FrameDetails()
    # matching = CalculateMatching()

    def get_mark_for_two_frames(self, body_estimation, img, db_frame, frame, matching):
        """
        Computes the mark for two frames by performing body pose estimation and matching.

        Args:
            body_estimation (Body): An instance of the Body class representing the body pose estimation model.
            img: The input image for body pose estimation.
            db_frame: The frame used for comparison with the input frame.
            frame (FrameDetails): An instance of the FrameDetails class for creating frame details.
            matching (CalculateMatching): An instance of the CalculateMatching class for comparing frames.

        Returns:
            None
        """
        candidate, subset = body_estimation(img)
        frame_details = frame.get_frame_details(candidate, subset)
        matching.compare_2_frames(frame_details, db_frame)

