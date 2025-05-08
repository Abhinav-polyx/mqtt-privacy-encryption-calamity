import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet

key = b'kUPngUuvmpvHgAfUg6EaNeBbdkavMxTz-rMVEF_L4gg='  
cipher = Fernet(key)

def on_message(client, userdata, msg):
    decrypted = cipher.decrypt(msg.payload).decode()
    print(f"Decrypted: {decrypted}")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("disaster/zone")
client.on_message = on_message
client.loop_forever()
