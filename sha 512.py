import hashlib

def sha512_hash_string(input_string):
    # Create a SHA-512 hash object
    sha512_hash = hashlib.sha512()
    
    # Update the hash object with the bytes of the input string
    sha512_hash.update(input_string.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    return sha512_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a string to hash using SHA-512 : ")
    hashed_output = sha512_hash_string(user_input)
    print(f"SHA-512 hash of  '{user_input}' : {hashed_output}")
