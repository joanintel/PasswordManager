import os
import json
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

# --- Constants ---
KDF_ITERATIONS = 200_000
KEY_LENGTH = 32  #256-bit AES key
NONCE_LENGTH = 12  #AES-GCM recommended


def generate_salt(length=16):
    """Generate a random salt"""
    return os.urandom(length)


def derive_key(master_password, salt):
    """Derive encryption key from master password + salt"""
    if isinstance(master_password, str):
        master_password = master_password.encode()
    key = PBKDF2(master_password, salt, dkLen=KEY_LENGTH, count=KDF_ITERATIONS, hmac_hash_module=SHA256)
    return key


def encrypt_data(data, key):
    """Encrypt Python data (list/dict) using AES-GCM"""
    # Convert to JSON bytes
    plaintext = json.dumps(data).encode()

    # Generate nonce
    nonce = os.urandom(NONCE_LENGTH)

    # AES-GCM encrypt
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Return: nonce + ciphertext + tag
    return nonce + ciphertext + tag


def decrypt_data(encrypted_data, key):
    """Decrypt AES-GCM encrypted data and return Python object"""
    if len(encrypted_data) < NONCE_LENGTH + 16:
        raise ValueError("Encrypted data is too short or corrupted")

    nonce = encrypted_data[:NONCE_LENGTH]
    tag = encrypted_data[-16:]
    ciphertext = encrypted_data[NONCE_LENGTH:-16]

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return json.loads(plaintext.decode())
