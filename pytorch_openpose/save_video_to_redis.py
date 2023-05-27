import redis
import base64


with open('images/111.mp4', 'rb') as f:
    video_data = f.read()

encoded_data = base64.b64encode(video_data).decode('utf-8')
redis_client = redis.Redis(host='localhost', port=6379, db=0)
redis_client.set('my_video', encoded_data)
#print(r.ping())


my_video =redis_client.get('my_video')
my_video2 = base64.b64decode(my_video)
print('aa', my_video2)