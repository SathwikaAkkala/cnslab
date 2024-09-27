def caesar_cipher(text, shift, direction='encrypt'):
    result = ''
    
    if direction == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not a letter, leave it unchanged
        else:
            result += char

    return result

# Step 1: Encrypt the plain text
plain_text = input("Enter the plain text to encrypt: ")
shift = int(input("Enter the shift (key): "))

# Encrypt the plain text
encrypted_text = caesar_cipher(plain_text, shift, 'encrypt')
print(f"Encrypted Text: {encrypted_text}")

# Step 2: Decrypt the encrypted text back to the plain text
decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
print(f"Decrypted Text: {decrypted_text}")
