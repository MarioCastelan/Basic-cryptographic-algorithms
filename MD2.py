# Castelan Hernandez Mario
# MD2

import sys
from typing import List

"""256-byte "random" permutation constructed from the digits of pi"""
S = [41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
     19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
     76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
     138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
     245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
     148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
     39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
     181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
     150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
     112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
     96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
     85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
     234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
     129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
     8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
     203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
     166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
     31, 26, 219, 153, 141, 51, 159, 17, 131, 20]

"""The message is "padded" (extended) so that its length (in bytes) is
congruent to 0, modulo 16. That is, the message is extended so that it 
is a multiple of 16 bytes long."""


def padding(M: List[int]) -> List[int]:
    i = 16 - (len(M) % 16)
    for _ in range(i):
        M.append(i)
    return M


"""A 16-byte checksum of the message is appended to the padded message."""


def checksum(M: List[int]) -> List[int]:
    N = len(M)
    # Clear checksum
    C = [0 for _ in range(16)]
    L = 0
    # Process each 16-word block
    for i in range(N // 16):
        # Checksum block i
        for j in range(16):
            c = M[16 * i + j]
            C[j] = C[j] ^ S[c ^ L]
            L = C[j]
    # The 16-byte checksum C[0 ... 15] is appended to the message
    return M + C


"""A 48-byte buffer X is used to compute the message digest. The buffer
is initialized to zero. Then process Message in 16-Byte Blocks to generate
the message digest.
"""


def hash(M: List[int]) -> List[int]:
    # Initialize MD Buffer
    X = [0 for _ in range(48)]
    N = len(M)
    # Process each 16-word block
    for i in range(N // 16):
        # Copy block i into X
        for j in range(16):
            X[j + 16] = M[16 * i + j]
            X[j + 32] = X[j + 16] ^ X[j]
        t = 0
        # Do 18 rounds
        for j in range(18):
            for k in range(48):
                t = X[k] ^ S[t]
                X[k] = t
            t = (t + j) % 256
    return X


def message_digest(M: List[int]) -> str:
    M = padding(M)
    M = checksum(M)
    X = hash(M)
    MD = ''
    # The message digest produced as output is X[0 ... 15]
    for byte in range(16):
        MD += f'{X[byte]:02x}'
    return MD


# Driver code
if __name__ == '__main__':
    plaintext = input()
    if plaintext == '""':
        plaintext = ''
    plaintext = plaintext.encode('utf-8')
    MD = message_digest([byte for byte in plaintext])
    sys.stdout.write(MD)
