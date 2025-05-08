import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet
import hashlib
import json
import time

broker = "localhost"
port = 1883
topic = "calamity/help"

# Generate key and write once to file
key = Fernet.generate_key()
with open("aes.key", "wb") as f:
    f.write(key)

cipher = Fernet(key)

# Hash real name using SHA-256 + salt
real_name = "Jonathan"
salt = "Calamity-Dr"
hashed_id = hashlib.sha256((salt + real_name).encode()).hexdigest()

victim_data = {
    "id": hashed_id,
    "location": "zone_a",
    "message": "HELP"
}

client = mqtt.Client()
client.connect(broker, port)

while True:
    json_payload = json.dumps(victim_data).encode()
    encrypted_payload = cipher.encrypt(json_payload)
    client.publish(topic, encrypted_payload)
    print("Published encrypted message.")
    time.sleep(5)
