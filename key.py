from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("Copy and paste this key into your code:")
print(key)
