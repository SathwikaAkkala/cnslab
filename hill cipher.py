import numpy as np

# Convert each character to a number (A = 0, B = 1, ..., Z = 25)
def char_to_num(c):
    return ord(c.upper()) - ord('A')

# Convert each number back to a character
def num_to_char(n):
    return chr(n + ord('A'))

# Prepare the text (remove spaces, uppercase, handle padding for blocks)
def prepare_text(text, block_size):
    text = text.upper().replace(" ", "")
    # Add padding if necessary to make the text a multiple of the block size
    while len(text) % block_size != 0:
        text += 'X'  # Padding character
    return text

# Encrypt a block using the Hill cipher matrix
def encrypt_block(block, key_matrix):
    block_vector = np.array([char_to_num(c) for c in block])
    encrypted_vector = np.dot(key_matrix, block_vector) % 26
    encrypted_block = ''.join(num_to_char(int(num)) for num in encrypted_vector)
    return encrypted_block

# Decrypt a block using the inverse key matrix
def decrypt_block(block, inverse_key_matrix):
    block_vector = np.array([char_to_num(c) for c in block])
    decrypted_vector = np.dot(inverse_key_matrix, block_vector) % 26
    decrypted_block = ''.join(num_to_char(int(num)) for num in decrypted_vector)
    return decrypted_block

# Function to calculate the inverse of the key matrix
def find_inverse_matrix(matrix):
    determinant = int(np.round(np.linalg.det(matrix)))  # Get the determinant
    determinant = determinant % 26
    try:
        determinant_inv = pow(determinant, -1, 26)  # Find the modular inverse of the determinant mod 26
    except ValueError:
        raise ValueError("Determinant is not invertible mod 26. Key matrix is invalid.")
    
    # Calculate the matrix of minors
    matrix_inv = np.round(np.linalg.inv(matrix)).astype(int) % 26
    
    # Multiply by the modular inverse of the determinant
    matrix_mod_inv = (determinant_inv * matrix_inv) % 26
    return matrix_mod_inv

# Hill Cipher Encryption
def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = len(key_matrix)
    plaintext = prepare_text(plaintext, block_size)
    
    ciphertext = ""
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        ciphertext += encrypt_block(block, key_matrix)
    
    return ciphertext

# Hill Cipher Decryption
def hill_cipher_decrypt(ciphertext, key_matrix):
    block_size = len(key_matrix)
    try:
        inverse_key_matrix = find_inverse_matrix(key_matrix)
    except ValueError as e:
        print(f"Error: {e}")
        return ""
    
    decrypted_text = ""
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        decrypted_text += decrypt_block(block, inverse_key_matrix)
    
    return decrypted_text

# Input from the user
key_matrix_input = input("Enter the key matrix (e.g., 2x2 or 3x3, rows separated by semicolon, elements separated by commas): ").strip()

# Parsing the key matrix input (e.g., '6,24;1,16' for a 2x2 matrix)
try:
    key_matrix = np.array([[int(num) for num in row.split(',')] for row in key_matrix_input.split(';')])
    print(f"Key Matrix:\n{key_matrix}")
except ValueError as e:
    print(f"Error parsing key matrix: {e}")
    exit(1)

plaintext = input("Enter the plain text to encrypt: ").strip()

# Encrypt the plaintext
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print(f"Encrypted Text: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print(f"Decrypted Text: {decrypted_text}")
