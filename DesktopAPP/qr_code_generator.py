import os
import qrcode
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json

data = b"this is a highly secret message please don't tell anyone save it with you life"
directory = os.path.join(os.getcwd(), 'DesktopAPP')

# Check if the key is loaded if not then create it 
try:
    with open(os.path.join(directory, 'key.bin'), 'rb') as file:
        key = file.read()
except FileNotFoundError:
    key = get_random_bytes(16)
    with open(os.path.join(directory, 'key.bin'), 'wb') as file:
        file.write(key)

cipher = AES.new(key, AES.MODE_CBC)
encrypted_data = b64encode(cipher.iv + cipher.encrypt(pad(data, AES.block_size)))

print(f'Data: {data}\n')
print(f'Key is : {key} in Bytes\n')
print(f'Key length is : {len(key)} in Bytes\n')
print(f'Key is : {b64encode(key)} in Base64\n')
print(f'Key length is : {len(b64encode(key))} in Base64\n')

print(f'the encrypted Data :{encrypted_data +b64encode(key)}')

# Generate QR Code using the encrypted data and saving it
img = qrcode.make(encrypted_data+b64encode(key))
img.save(os.path.join(directory, 'result.jpg'))

print("Script Complete")
