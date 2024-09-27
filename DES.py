from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plaintext, key):
    # Create a DES cipher object
    des = DES.new(key, DES.MODE_ECB)

    # Pad the plaintext to be a multiple of 8 bytes (64 bits)
    padded_text = pad(plaintext.encode(), DES.block_size)

    # Encrypt the plaintext
    ciphertext = des.encrypt(padded_text)
    
    return ciphertext

def des_decrypt(ciphertext, key):
    # Create a DES cipher object
    des = DES.new(key, DES.MODE_ECB)

    # Decrypt the ciphertext
    decrypted_padded_text = des.decrypt(ciphertext)

    # Unpad the decrypted text to get the original plaintext
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    
    return decrypted_text.decode()

# Example usage
if __name__ == "__main__":
    # Generate a random 8-byte (64-bit) key
    key = get_random_bytes(8)
    
    # Plaintext to encrypt
    plaintext = input("Enter the plaintext: ")
    
    # Encrypt the plaintext
    ciphertext = des_encrypt(plaintext, key)
    print(f"Ciphertext (in hex): {ciphertext.hex()}")
    
    # Decrypt the ciphertext
    decrypted_text = des_decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")
