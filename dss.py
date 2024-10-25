import random

# Helper functions
def mod_exp(base, exp, mod):
    """Modular Exponentiation: (base^exp) % mod."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def generate_prime_candidate(bits):
    """Generate an odd integer randomly of specified bit size."""
    p = random.getrandbits(bits) | (1 << (bits - 1)) | 1  # Ensure it's odd and of correct bit length
    return p

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    # Find r and d such that n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bits):
    """Generate a prime number of the specified bit length."""
    p = generate_prime_candidate(bits)
    while not is_prime(p):
        p = generate_prime_candidate(bits)
    return p

def mod_inverse(a, m):
    """Compute the modular inverse of a modulo m using the Extended Euclidean Algorithm."""
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Step 1: Key Generation
# Generate p, q, and g (usually requires large bit sizes, simplified here)
p = generate_large_prime(10)  # Small size for example
q = generate_large_prime(5)   # Small size for example
g = random.randint(2, p - 1)

# Private and Public Keys
x = random.randint(1, q - 1)       # Private key
y = mod_exp(g, x, p)               # Public key

print("Public parameters (p, q, g):", p, q, g)
print("Private key (x):", x)
print("Public key (y):", y)

# Step 2: Signature Generation
message = "Hello"
hashed_msg = sum(ord(char) for char in message) % q  # Simple hash (not secure, just for illustration)

k = random.randint(1, q - 1)
r = mod_exp(g, k, p) % q
k_inv = mod_inverse(k, q)  # Find modular inverse of k mod q
s = (hashed_msg + x * r) * k_inv % q  # Now we use k_inv instead of pow(k, -1, q)

print("Message:", message)
print("Signature (r, s):", (r, s))

# Step 3: Signature Verification
def verify_signature(r, s, hashed_msg):
    """Verify the signature."""
    w = mod_inverse(s, q) % q
    u1 = (hashed_msg * w) % q
    u2 = (r * w) % q
    v = ((mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p) % q
    return v == r

# Verify
if verify_signature(r, s, hashed_msg):
    print("Signature is valid.")
else:
    print("Signature is invalid.")
