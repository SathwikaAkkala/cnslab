def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(encrypted_text,s):
    result = ""

    # traverse text
    for i in range(len(encrypted_text)):
        char =encrypted_text[i]

        # decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # decrypt lowercase characters
        else:
            result += chr((ord(char) -s - 97) % 26 + 97)

    return result
text = input("enter the string")
s = 4
encrypted_text = encrypt(text,s)
print(f"Encrypted Text: {encrypted_text}")
print ("Shift : " + str(s))

decrypted_text = decrypt(encrypted_text,s)
print(f"Decrypted Text: {decrypted_text}")

