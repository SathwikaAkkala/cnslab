def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return "".join(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        # Shift character by corresponding key character
        if plaintext[i].isalpha():  # Only encrypt alphabetic characters
            shift = (ord(plaintext[i].upper()) + ord(key[i].upper())) % 26
            ciphertext.append(chr(shift + 65))
        else:
            ciphertext.append(plaintext[i])  # Keep non-alphabetic characters unchanged
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].upper()) - ord(key[i].upper()) + 26) % 26
            plaintext.append(chr(shift + 65))
        else:
            plaintext.append(ciphertext[i])
    return "".join(plaintext)

# Input
plaintext = input("Enter the plain text to encrypt: ").strip().upper()
key = input("Enter the encryption key: ").strip().upper()

# Generate the repeating key
generated_key = generate_key(plaintext, list(key))

# Encrypt the plaintext
encrypted_text = vigenere_encrypt(plaintext, generated_key)
print(f"Encrypted Text: {encrypted_text}")

# Decrypt the encrypted text
decrypted_text = vigenere_decrypt(encrypted_text, generated_key)
print(f"Decrypted Text: {decrypted_text}")
