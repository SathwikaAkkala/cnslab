def decrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        # decrypt lowercase characters
        else:
            result += chr((ord(char) -s - 97) % 26 + 97)

    return result

#check the above function
text = input("enter the string")
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + decrypt(text,s))
