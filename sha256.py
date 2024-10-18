def right_rotate(value, amount):
    return ((value >> amount) | (value << (32 - amount))) & 0xFFFFFFFF

def generate_constants():
    # Generate the first 64 prime numbers
    primes = []
    num = 2
    while len(primes) < 64:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 1
    
    # Calculate constants using the cube root of the first 64 primes
    K = []
    for p in primes:
        # Calculate the cube root and take the fractional part
        frac = (p ** (1/3)) - int(p ** (1/3))
        K.append(int(frac * (1 << 32)) & 0xFFFFFFFF)

    return K

def sha256(message):
    K = generate_constants()

    # Preprocessing
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    message += original_bit_len.to_bytes(8, 'big')

    # Initial hash values
    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # Process each 512-bit chunk
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        w = list(int.from_bytes(chunk[j:j + 4], 'big') for j in range(0, 64, 4)) + [0] * 48

        for j in range(16, 64):
            s0 = right_rotate(w[j - 15], 7) ^ right_rotate(w[j - 15], 18) ^ (w[j - 15] >> 3)
            s1 = right_rotate(w[j - 2], 17) ^ right_rotate(w[j - 2], 19) ^ (w[j - 2] >> 10)
            w[j] = (w[j - 16] + s0 + w[j - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = H

        for j in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[j] + w[j]) & 0xFFFFFFFF
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Add the compressed chunk to the current hash value
        H = [(x + y) & 0xFFFFFFFF for x, y in zip(H, [a, b, c, d, e, f, g, h])]

    # Produce the final hash value
    return b''.join(h.to_bytes(4, 'big') for h in H)

if __name__ == "__main__":
    input_string = input("Enter a string to hash: ")
    input_bytes = input_string.encode('utf-8')
    hash_result = sha256(input_bytes)
    print("SHA-256 hash:", hash_result.hex())
