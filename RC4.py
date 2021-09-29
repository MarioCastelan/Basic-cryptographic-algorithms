# Castelan Hernandez Mario



import sys
from typing import Generator, List

"""
The key-scheduling algorithm is used to initialize the permutation 
in the array "S". "keylength" is defined as the number of bytes in the 
key and can be in the range 1 ≤ keylength ≤ 256, typically between 5 and 
16, corresponding to a key length of 40 – 128 bits. First, the array "S" 
is initialized to the identity permutation. S is then processed for 256 
iterations in a similar way to the main PRGA, but also mixes in bytes of 
the key at the same time.
"""

def key_scheduling_algorithm(key: str) -> List[int]:
    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
    return S

"""
The output byte is selected by looking up the values of S(i) and S(j), 
adding them together modulo 256, and then using the sum as an index into 
S; S(S(i) + S(j)) is used as a byte of the key stream, K.
"""
def pseudo_random_generation_algorithm(S: List[int]) -> Generator:
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


# Driver code
if __name__ == "__main__":

    key = input()
    plaintext = input()

    S = key_scheduling_algorithm(key)   # Permutation of all 256 possible bytes
    keystream = pseudo_random_generation_algorithm(S) # keystream generator

    # Plaintext XORed with Keystream  
    for c in plaintext:
        sys.stdout.write(f"{(ord(c) ^ next(keystream)):02X}")
