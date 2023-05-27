
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client['dancing']
# collection = db['users']
collection = db['videos']

# Define the data to be inserted
frame_details = {'video_id': 2,
       'frame_id': 1,
       'Nose_Neck_LeftShoulder': (1.4871794871794872, 0.025, 54.65047327886501, 'counterclockwise'),
       'Nose_Neck_RightShoulder': (1.4871794871794872, 0.02564102564102564, 54.613768748643835, 'counterclockwise'),
       'Neck_RightShoulder_RightElbow': (0.6190476190476191, 0.6190476190476191, 0.0, 'counterclockwise'),
       'RightShoulder_RightElbow_RightWrist': (0.6190476190476191, -0.55, 60.57027382778586, 'counterclockwise'),
       'Neck_LeftShoulder_LeftElbow': (0.025, -1.4137931034482758, 56.15967473556625, 'counterclockwise'),
       'LeftShoulder_LeftElbow_LeftWrist': (-1.4137931034482758, 3.3636363636363638, 51.82949282423504, 'clockwise'),
       'Neck_RightHip_RightKnee': (7.055555555555555, -48.0, 9.260421153775138, 'counterclockwise'),
       'RightHip_RightKnee_RightAnkle': (-48.0, 0.24, 0, 'clockwise'),
       'Neck_LeftHip_LeftKnee': (-4.846153846153846, 16.333333333333332, 15.162824298307456, 'clockwise'),
       'LeftHip_LeftKnee_LeftAnkle': (16.333333333333332, -52.0, 4.605237759990833, 'counterclockwise')}


# Insert the data into the collection
# result = collection.insert_one(frame_details)
frames_list = collection.find({"video_id": 1})
print(frames_list)
# Print the ID of the inserted document
# print(result.inserted_id)
