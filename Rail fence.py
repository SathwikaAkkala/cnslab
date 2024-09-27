def rail_fence_encrypt(plaintext, key):
    # Create an empty 2D array for rail pattern
    rail = [['\n' for i in range(len(plaintext))] for j in range(key)]

    # To determine the direction of movement
    direction_down = False
    row, col = 0, 0

    # Fill the rail matrix in a zigzag pattern
    for i in range(len(plaintext)):
        # Place the current character in the rail
        rail[row][col] = plaintext[i]
        col += 1

        # Change direction at the top and bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Move vertically in the appropriate direction
        row += 1 if direction_down else -1

    # Construct the encrypted message by reading the matrix row-wise
    encrypted_text = []
    for i in range(key):
        for j in range(len(rail[i])):
            if rail[i][j] != '\n':
                encrypted_text.append(rail[i][j])

    return "".join(encrypted_text)

def rail_fence_decrypt(ciphertext, key):
    # Create an empty 2D array for rail pattern
    rail = [['\n' for i in range(len(ciphertext))] for j in range(key)]

    # To determine the direction of movement
    direction_down = None
    row, col = 0, 0

    # Mark the positions in the rail where the characters will go
    for i in range(len(ciphertext)):
        # Place a placeholder
        rail[row][col] = '*'
        col += 1

        # Change direction at the top and bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Move vertically in the appropriate direction
        row += 1 if direction_down else -1

    # Fill the rail matrix with the ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the matrix in a zigzag pattern to reconstruct the original message
    decrypted_text = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        # Add the character to the decrypted text
        decrypted_text.append(rail[row][col])
        col += 1

        # Change direction at the top and bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        # Move vertically in the appropriate direction
        row += 1 if direction_down else -1

    return "".join(decrypted_text)

# Input
plaintext = input("Enter the plain text to encrypt: ").strip()
key = int(input("Enter the number of rails (key): ").strip())

# Encrypt the plain text
encrypted_text = rail_fence_encrypt(plaintext, key)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = rail_fence_decrypt(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")
