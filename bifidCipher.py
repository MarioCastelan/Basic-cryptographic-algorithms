# Castelan Hernandez Mario
# The Bifid cipher


from typing import List, Tuple



ALPHABET = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def create_tableau(key:str)->List[str]:
    tableau_helper = []
    tableau = [['' for _ in range(5)] for _ in range(5)] # Empty 5x5 Array 
    alphabet = ALPHABET[:] # Copy alphabet
    # Removes alphabet characters already in key 
    for char in key:
        alphabet.remove(char)
        tableau_helper.append(char)
    # Joins key with remaining alphabet characters
    tableau_helper += alphabet
    tableau_helper = iter(tableau_helper)
    # Creates tableau with key and alphabet in a 5x5 array
    for row in range(5):
        for col in range(5):
            tableau[row][col] = next(tableau_helper)

    return tableau

def get_indices(array: List[str], item:str) ->Tuple[int, int]:
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == item:
                return (row, col)



def bifidCipher_decrypt(key:str, cipher_text:str)->str:
    tableau = create_tableau(key)
    decoded_text = ""
    indices = []
    # Finds indices for each character in cipher text
    for char in cipher_text:
        row, col = get_indices(tableau, char)
        indices.append(row)
        indices.append(col)
    # Separates indices in two rows and form pair of indices from columns    
    # those indices corresponds to decypted text characters 
    for row, col in zip(indices[:len(cipher_text)], indices[len(cipher_text):]):
        decoded_text += tableau[row][col]

    return decoded_text


def bifidCipher_encrypt(key:str, message:str)->str:
    first_row = []
    second_row = []
    tableau = create_tableau(key)
    encoded_text = ""
    # Encodes the message using indices from the tableau
    # Indices are arranged in two rows
    for char in message.replace(' ',''): # Removes spaces from message
        row, col = get_indices(tableau, char)
        first_row.append(row)
        second_row.append(col)
    # Indices group in pairs and turned into letters
    for row, col in zip((first_row + second_row)[::2], (first_row + second_row)[1::2]):
        encoded_text += tableau[row][col]

    return encoded_text


# Driver code
if __name__ == "__main__":

    option = input()
    if 'ENCRYPT' in option:
        message = input()
        encrypted_text = bifidCipher_encrypt('ENCRYPT', message)
        print(encrypted_text)
    elif 'DECRYPT' in option:
        cipher_text = input()
        plain_text = bifidCipher_decrypt('ENCRYPT', cipher_text)
        print(plain_text)


