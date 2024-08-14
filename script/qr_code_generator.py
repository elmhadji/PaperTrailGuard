import os
import qrcode
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

directory = os.path.join(os.getcwd(), 'script')

def get_data_to_code():
    global directory
    data = input('Please Enter the Data you want to encrypt : ')
    data = data.encode("utf-8")
    # Check if there is a key file and if not create one
    key_path = os.path.join(directory, 'key.bin')
    if os.path.exists(key_path):
        response = input(f"A key file already exists at {key_path}. Do you want to create a new key? (y/N): ")
        if response.lower() == 'y':
            key = get_random_bytes(16)
            with open(key_path, 'wb') as file:
                file.write(key)
        else:
            with open(key_path, 'rb') as file:
                key = file.read()
    else:
        key = get_random_bytes(16)
        with open(key_path, 'wb') as file:
            file.write(key)
    return data, key

def encrypt_text(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = b64encode(cipher.iv + cipher.encrypt(pad(data, AES.block_size)))
    return encrypted_data

def generate_qr(encrypted_data, key):
    global directory
    # Generate encrypted QR Code & save it in result.jpg
    img = qrcode.make(encrypted_data+b64encode(key))
    img.save(os.path.join(directory, 'result.jpg'))

if __name__ == '__main__':
    data, key = get_data_to_code()
    encrypted_data = encrypt_text(data, key)
    generate_qr(encrypted_data, key)

    # Simple print statement to show the encrypted data
    print(f'Data: {data}\n')
    print(f'Key is : {key} in Bytes\n')
    print(f'Key length is : {len(key)} in Bytes\n')
    print(f'Key is : {b64encode(key)} in Base64\n')
    print(f'Key length is : {len(b64encode(key))} in Base64\n')
    print(f'the encrypted Data :{encrypted_data +b64encode(key)}')

    # Print statement to show that the script is complete
    print("Script Complete")