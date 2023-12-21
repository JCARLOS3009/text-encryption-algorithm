from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def generate_key():
    return get_random_bytes(16)

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return iv, ciphertext

def decrypt_message(iv, ciphertext, key):
    iv = base64.b64decode(iv)
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode('utf-8')

# Exemplo de uso
key = generate_key()
message ="Mensagem a ser criptografada, AES encryption!"

iv, ciphertext = encrypt_message(message, key)
print("IV:", iv)
print("Ciphertext:", ciphertext)

decrypted_message = decrypt_message(iv, ciphertext, key)
print("Decrypted Message:", decrypted_message)
