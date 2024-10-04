import random

def diffie_hellman():
    # Step 1: Input the prime number (p) and base (g)
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a base (g): "))

    # Step 2: Private keys (a for Alice, b for Bob)
    a = random.randint(1, p-1)
    b = random.randint(1, p-1)

    print(f"\nPrivate key for Alice (a): {a}")
    print(f"Private key for Bob (b): {b}")

    # Step 3: Compute public keys
    A = pow(g, a, p)  # A = g^a mod p
    B = pow(g, b, p)  # B = g^b mod p

    print(f"\nPublic key for Alice (A): {A}")
    print(f"Public key for Bob (B): {B}")

    # Step 4: Exchange public keys and compute the shared secret
    # Alice computes the shared secret S_A
    shared_secret_alice = pow(B, a, p)  # S_A = B^a mod p
    # Bob computes the shared secret S_B
    shared_secret_bob = pow(A, b, p)    # S_B = A^b mod p

    print(f"\nShared secret computed by Alice: {shared_secret_alice}")
    print(f"Shared secret computed by Bob: {shared_secret_bob}")

    # Step 5: Both shared secrets should be the same
    if shared_secret_alice == shared_secret_bob:
        print(f"\nShared secret (S) established successfully: {shared_secret_alice}")
    else:
        print("\nError: Shared secrets do not match!")

if __name__ == "__main__":
    diffie_hellman()
