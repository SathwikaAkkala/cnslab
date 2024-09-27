def generate_key_matrix(key):
    # Create an empty 5x5 matrix
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")  # Replace J with I

    # Remove duplicate characters from the key
    used = set()
    new_key = ""
    for char in key:
        if char not in used and char in alphabet:
            used.add(char)
            new_key += char

    # Add the remaining letters of the alphabet
    for char in alphabet:
        if char not in used:
            new_key += char

    # Create the matrix
    for i in range(5):
        matrix.append([new_key[j + i * 5] for j in range(5)])

    return matrix

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def playfair_encrypt(text, key_matrix):
    text = text.upper().replace("J", "I")
    text = [char for char in text if char.isalpha()]

    # Insert 'X' between duplicate letters
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text.insert(i + 1, 'X')
        i += 2

    # If the text length is odd, add an extra 'X' at the end
    if len(text) % 2 != 0:
        text.append('X')

    ciphertext = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(key_matrix, text[i])
        row2, col2 = find_position(key_matrix, text[i + 1])

        if row1 == row2:
            # Same row: Shift right
            ciphertext += key_matrix[row1][(col1 + 1) % 5]
            ciphertext += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column: Shift down
            ciphertext += key_matrix[(row1 + 1) % 5][col1]
            ciphertext += key_matrix[(row2 + 1) % 5][col2]
        else:
            # Rectangle: Swap columns
            ciphertext += key_matrix[row1][col2]
            ciphertext += key_matrix[row2][col1]

    return ciphertext

def playfair_decrypt(ciphertext, key_matrix):
    text = ciphertext.upper().replace("J", "I")
    text = [char for char in text if char.isalpha()]

    decrypted_text = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(key_matrix, text[i])
        row2, col2 = find_position(key_matrix, text[i + 1])

        if row1 == row2:
            # Same row: Shift left
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column: Shift up
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else:
            # Rectangle: Swap columns
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]

    # Remove 'X' inserted between duplicate letters
    return decrypted_text

# Input
key = input("Enter the encryption key: ").strip()
plaintext = input("Enter the plain text to encrypt: ").strip()

# Generate the key matrix
key_matrix = generate_key_matrix(key)

# Encrypt the plain text
encrypted_text = playfair_encrypt(plaintext, key_matrix)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = playfair_decrypt(encrypted_text, key_matrix)
print(f"Decrypted Text: {decrypted_text}")
