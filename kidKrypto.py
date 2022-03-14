# Castelan Hernandez Mario
# Assignment: 05 - Kid Krypto

from typing import Tuple


# Computes private and public key
def compute_keys(a: int, b: int, A: int, B: int) -> Tuple:
    M = a * b - 1
    e = A * M + a
    d = B * M + b
    n = (e * d - 1) // M
    return e, d, n


# Encrypts a message using public key
def encrypt(message: int, e: int, n: int) -> int:
    return message * e % n


# Decrypts a message using private key
def decrypt(ciphertext: int, d: int, n: int) -> int:
    return ciphertext * d % n


# Driver code
if __name__ == '__main__':
    option = input()
    a = int(input())
    b = int(input())
    A = int(input())
    B = int(input())
    text = int(input())
    e, d, n = compute_keys(a, b, A, B)
    if option == 'E':
        print(encrypt(text, e, n))
    elif option == 'D':
        print(decrypt(text, d, n))
