import base64
import hashlib
import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def get_key_from_password(password):
    password_bytes = password.encode('utf-8')
    digest = hashlib.sha256(password_bytes).digest()
    return digest[:16]

def encrypt_data(plaintext, password):
    key = get_key_from_password(password)
    backend = default_backend()
    
    data_bytes = plaintext.encode('utf-8')

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data_bytes) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(encrypted_data).decode('utf-8')

def decrypt_data(encrypted_text_b64, password):
    try:
        key = get_key_from_password(password)
        backend = default_backend()
        
        clean_b64 = re.sub(r'[^A-Za-z0-9+/=]', '', encrypted_text_b64)
        
        try:
            encrypted_data = base64.b64decode(clean_b64, validate=True)
        except Exception:
            return None 

        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()

        return decrypted_data.decode('utf-8')
        
    except Exception as e:
        return None