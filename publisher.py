import paho.mqtt.client as mqtt
import time
import json
from cryptography.fernet import Fernet

key = b'kUPngUuvmpvHgAfUg6EaNeBbdkavMxTz-rMVEF_L4gg=' 
cipher = Fernet(key)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

message = {
    "user": "Jonathan",
    "loc": "zone_a",
    "msg": "help"
}

payload = cipher.encrypt(json.dumps(message).encode())

while True:
    client.publish("disaster/zone", payload)
    print("Encrypted message sent")
    time.sleep(5)
