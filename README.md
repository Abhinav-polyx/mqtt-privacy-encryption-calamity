# MQTT Privacy Project

## Tools Used
- Python
- Paho MQTT
- Mosquitto Broker
- `cryptography` library

## Setup Instructions

### Install Dependencies
```bash
sudo apt install mosquitto mosquitto-clients
pip install paho-mqtt cryptography
```

### Run MQTT Broker
```bash
mosquitto
```

### Run Publisher
```bash
python publisher.py
```

### Run Subscriber
```bash
python subscriber.py
```
