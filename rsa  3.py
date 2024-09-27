import math
import random

def generate_keypair(p, q):
    # Calculate the modulus (n) and the totient (phi)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a random number (e) that is coprime to phi
    e = random.randint(2, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(2, phi)

    # Calculate the modular multiplicative inverse (d) of e modulo phi
    d = pow(e, -1, phi)

    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

def encrypt_rsa(message, public_key):
    n, e = public_key
    encrypted_message = pow(int(message), e, n)
    return encrypted_message

def decrypt_rsa(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message

# Get user input for the prime numbers p and q
p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))

# Generate a keypair using p and q
public_key, private_key = generate_keypair(p, q)

# Get user input for the message
message = int(input("Enter the message: "))

# Encrypt the message
encrypted_message = encrypt_rsa(message, public_key)

print("Encrypted message:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt_rsa(encrypted_message, private_key)

print("Decrypted message:", decrypted_message)
