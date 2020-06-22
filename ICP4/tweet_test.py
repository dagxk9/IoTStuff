#!/user/bin/env python
import sys
from twython import Twython
from picamera import PiCamera
from time import sleep


tweetStr = "test_tweet"

apiKey = "DYv8rQbWbmaK4Z6gcPk3IUOME"
apiSecret = "j5KXORf9GhKjQlZ2veSEamwg4iH1xjSprYWmZ05KGmTVIpDrJT"
accessToken = "1273736882699014145-yu5jWMgiNyptqC8uBf7hNsO4ZyHeDv"
accessTockenSecret = "SdnYAjbzj8Wv8WC5HcKu3eFNLKe5mDwgQEcY9Zizl903M"

api=Twython(apiKey,apiSecret,accessToken,accessTockenSecret)

camera = PiCamera()

for i in range(5):
    camera.start_preview()
    sleep(5)
    camera.capture('./image{}.jpg'.format(i))
    camera.stop_preview()
    sleep(5)
    photo=open('./image{}.jpg'.format(i),'rb')
    response = api.upload_media(media=photo)
    
    api.update_status(status="Image{} from raspberry Pi Camera".format(i), media_ids=[response['media_id']])


