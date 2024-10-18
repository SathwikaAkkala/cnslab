import math

# Constants for MD5
S = [7, 12, 17, 22] * 4  # Shift amounts
K = [int(4294967296 * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

# Initial MD5 values
A0, B0, C0, D0 = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476)

def left_rotate(x, c):
    return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

def md5_padding(input_string):
    original_byte_len = len(input_string)
    original_bit_len = original_byte_len * 8
    input_string += b'\x80'
    while (len(input_string) * 8 + 64) % 512 != 0:
        input_string += b'\x00'
    input_string += original_bit_len.to_bytes(8, 'little')
    return input_string

def md5_hash(input_string):
    # Pad input
    padded_input = md5_padding(input_string.encode('utf-8'))

    # Initialize variables
    A, B, C, D = A0, B0, C0, D0

    # Process each 512-bit chunk
    for i in range(0, len(padded_input), 64):
        chunk = padded_input[i:i + 64]
        M = [int.from_bytes(chunk[j:j + 4], 'little') for j in range(0, 64, 4)]

        A_temp, B_temp, C_temp, D_temp = A, B, C, D

        # Main loop
        for j in range(64):
            if j < 16:
                F = (B_temp & C_temp) | (~B_temp & D_temp)
                g = j
            elif j < 32:
                F = (D_temp & B_temp) | (~D_temp & C_temp)
                g = (5 * j + 1) % 16
            elif j < 48:
                F = B_temp ^ C_temp ^ D_temp
                g = (3 * j + 5) % 16
            else:
                F = C_temp ^ (B_temp | ~D_temp)
                g = (7 * j) % 16

            F = (F + A_temp + K[j] + M[g]) & 0xFFFFFFFF
            A_temp, D_temp = D_temp, (B_temp + left_rotate(F, S[j % 4])) & 0xFFFFFFFF
            B_temp, C_temp = (B_temp + left_rotate(F, S[j % 4])) & 0xFFFFFFFF, B_temp

        # Add the compressed chunk to the current hash value
        A = (A + A_temp) & 0xFFFFFFFF
        B = (B + B_temp) & 0xFFFFFFFF
        C = (C + C_temp) & 0xFFFFFFFF
        D = (D + D_temp) & 0xFFFFFFFF

    # Produce the final hash value (little-endian)
    return (A, B, C, D)

def md5_hexdigest(hash_values):
    return ''.join(f'{value:08x}' for value in hash_values)

# Dynamic input
if __name__ == "__main__":
    input_string = input("Enter a string to hash: ")
    hash_values = md5_hash(input_string)
    print(f"MD5 hash of '{input_string}': {md5_hexdigest(hash_values)}")
