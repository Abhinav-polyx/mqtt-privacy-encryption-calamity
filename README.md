# MQTT Privacy-Protected Messaging in Calamity Scenarios

This project implements a privacy-enhanced MQTT communication system to simulate secure messaging between victims and a command center during a disaster. It uses:

- 🛡️ **Fernet encryption** (AES-based) for payload protection
- 🧠 **SHA-256 hashing** for pseudonymizing victim identities
- ✅ A working publisher-subscriber loop using `paho-mqtt`

## 🔧 Requirements

- Python 3.7+
- `paho-mqtt`
- `cryptography`

```bash
pip install paho-mqtt cryptography

