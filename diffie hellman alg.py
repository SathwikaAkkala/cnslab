def mod_exp(base, exp, mod):
    """ Efficiently compute (base^exp) % mod using modular exponentiation """
    return pow(base, exp, mod)

def main():
    # Input public parameters
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a base (generator) g: "))

    # Party A's private key and computation
    a = int(input("Party A, enter your private key (a): "))
    A = mod_exp(g, a, p)
    print(f"Party A's public key A: {A}")

    # Party B's private key and computation
    b = int(input("Party B, enter your private key (b): "))
    B = mod_exp(g, b, p)
    print(f"Party B's public key B: {B}")

    # Compute shared secret
    S_A = mod_exp(B, a, p)
    S_B = mod_exp(A, b, p)

    print(f"Party A's computed shared secret: {S_A}")
    print(f"Party B's computed shared secret: {S_B}")

    if S_A == S_B:
        print("Both parties have successfully computed the same shared secret.")
    else:
        print("There was an error. The shared secrets do not match.")

if __name__ == "__main__":
    main()
