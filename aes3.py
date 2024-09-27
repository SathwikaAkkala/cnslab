from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# AES key must be either 16, 24, or 32 bytes long
key = get_random_bytes(16)

def aes_encrypt(plaintext):
    # Convert plaintext to bytes if not already
    if isinstance(plaintext, str):
        plaintext = plaintext.encode('utf-8')
    
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(AES.block_size)
    
    # Create AES cipher with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the plaintext to match AES block size and encrypt
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    # Return IV + ciphertext (IV is needed for decryption)
    return iv + ciphertext

def aes_decrypt(ciphertext):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:AES.block_size]
    actual_ciphertext = ciphertext[AES.block_size:]
    
    # Create AES cipher with CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt and unpad the plaintext
    decrypted_data = unpad(cipher.decrypt(actual_ciphertext), AES.block_size)
    
    return decrypted_data.decode('utf-8')

# Example usage
plaintext = "This is a secret message!"
ciphertext = aes_encrypt(plaintext)
print(f"Encrypted: {ciphertext}")

decrypted_text = aes_decrypt(ciphertext)
print(f"Decrypted: {decrypted_text}")
