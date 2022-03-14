# Castelan Hernandez Mario
# Simplified DES


from typing import Tuple


def initial_permutation(m: str) -> str:
    return m[1] + m[5] + m[2] + m[0] + m[3] + m[7] + m[4] + m[6]


def inverse_permutation(m: str) -> str:
    return m[3] + m[0] + m[2] + m[4] + m[6] + m[1] + m[7] + m[5]


def subkeys(key: str) -> Tuple[str, str]:
    # Permuted according to the permutation:(2,4,1 6,3 9,0 8,7 5)
    key = key[2] + key[4] + key[1] + key[6] + key[3] + \
        key[9] + key[0] + key[8] + key[7] + key[5]
    # Cyclically shifted one bit to the left
    key = key[1:5] + key[0] + key[6:] + key[5]
    # Subkey one is obtained by taking these bits out of the result of the last operation: (5,2,6,3,7,4,9,8)
    k1 = key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8]
    # The key shifted before is  shifted two bits to the left:
    k2 = key[2:5] + key[0:2] + key[7:] + key[5:7]
    # Subkey two is obtained by taking these bits out of the result of the last operation: (5,2,6,3,7,4,9,8)
    k2 = k2[5] + k2[2] + k2[6] + k2[3] + k2[7] + k2[4] + k2[9] + k2[8]
    # Another way
    # k1 = key[0] + key[6] + key[8] + key[3] + key[7] + key[2] + key[9] + key[5]
    # k2 = key[7] + key[2] + key[5] + key[4] + key[9] + key[1] + key[8] + key[0]
    return k1, k2


def sBox_0(m: str) -> str:
    # The outer two bits give the row number; the inner two bits the column number
    s = [[1, 0, 3, 2],
         [3, 2, 1, 0],
         [0, 2, 1, 3],
         [3, 1, 3, 2]]
    row = int(m[0]+m[3], 2)
    col = int(m[1:3], 2)
    return f'{s[row][col]:0>2b}'


def sBox_1(m: str) -> str:
    # The outer two bits give the row number; the inner two bits the column number
    s = [[0, 1, 2, 3],
         [2, 0, 1, 3],
         [3, 0, 1, 0],
         [2, 1, 0, 3]]
    row = int(m[0] + m[3], 2)
    col = int(m[1:3], 2)
    return f'{s[row][col]:0>2b}'


def feistel(m: str, k: str) -> str:
    l_m = m[:4]
    r_m = m[4:]
    # 4-bit block expanded into 8-bits
    r_m = r_m[3] + r_m[0] + r_m[1] + r_m[2] + r_m[1] + r_m[2] + r_m[3] + r_m[0]
    # The subkey is XOR-ed with this expansion
    r_m = f'{(int(r_m, 2) ^ int(k, 2)):0>8b}'
    # The result is broken into two halves of 4 bits each. These halves are turned into 2 bits,
    # each by means of two S-boxes S0 and S1, then left and right halves are concatenated
    r_m = sBox_0(r_m[:4]) + sBox_1(r_m[4:])
    # Result is pemutated according to (1,3,2,0)
    r_m = r_m[1] + r_m[3] + r_m[2] + r_m[0]
    # This output is now XOR-ed with the left half
    r_m = f'{(int(r_m, 2) ^ int(l_m, 2)):0>4b}'
    # Finally the output is concatenated with right half of text plain
    return r_m + m[4:]


def encrypt(m: str, key: str) -> str:
    m = initial_permutation(m)
    # Two subkeys of 8 bits each are used in each round
    k1, k2 = subkeys(key)
    # Feistel operation using subkey K1
    round1 = feistel(m, k1)
    # Switch left and right halves
    round1 = round1[4:] + round1[:4]
    # Feistel operation using subkey K2
    round2 = feistel(round1, k2)
    return inverse_permutation(round2)


def decrypt(m: str, key: str) -> str:
    m = initial_permutation(m)
    # Two subkeys of 8 bits each are used in each round
    k1, k2 = subkeys(key)
    # Feistel operation using subkey K2
    round1 = feistel(m, k2)
    # Switch left and right halves
    round1 = round1[4:] + round1[:4]
    # Feistel operation using subkey K1
    round2 = feistel(round1, k1)
    return inverse_permutation(round2)


# Driver code
if __name__ == '__main__':
    option = input()
    key = input()
    plaintext = input()
    if option == 'E':
        print(encrypt(plaintext, key))
    elif option == 'D':
        print(decrypt(plaintext, key))
