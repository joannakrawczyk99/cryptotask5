import decryption
import encryption
import key

if __name__ == '__main__':

    #key for encryption and also base for creating reversed key for decryption
    key_to_encrypt = {'a': 'q', 'b': 'v', 'c': 'x', 'd': 'z', 'e': 'y', 'f': 'w', 'g': 'u', 'h': 't', 'i': 's', 'j': 'r',
             'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'r': 'j', 's': 'i', 't': 'h', 'u': 'g', 'w': 'f',
             'y': 'e', 'z': 'd', 'x': 'c', 'v': 'b', 'q': 'a',
             'A': 'Q', 'B': 'V', 'C': 'X', 'D': 'Z', 'E': 'Y', 'F': 'W', 'G': 'U', 'H': 'T', 'I': 'S','J': 'R', 'K': 'P',
             'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'R': 'J', 'S': 'I', 'T': 'H', 'U': 'G', 'W': 'F', 'Y': 'E',
             'Z': 'D', 'X': 'C', 'V': 'B', 'Q': 'S',
             '1': '5', '2': '9', '3': '8', '4': '7', '5': '6', '6': '4', '7': '3', '8': '2', '9': '1',
             '.': ',', ',': '.', ':': ';', ';': ':', '?': '!', '!': '?', '-': '_', '_': '-', '(': ')', ')': '(',
             '%': '$', '$': '%', ' ': '&', '&': ' ', '+': '*', '*': '+'}

    #reading txt file where is the text for encryption
    with open('kafka.txt') as file:
        text_for_encryption = file.read()

    k1 = key.Key(key_to_encrypt)
    reversed_key = k1.createReverseKey()

    e1 = encryption.Encryption(key_to_encrypt, text_for_encryption)
    encrypted_text = e1.encrypt()
    print(encrypted_text)

    #saving encrypted message to txt file
    with open('encrypted.txt', 'w') as file:
        file.write(encrypted_text)

    #d1 = decryption.Decryption(reversed_key, encrypted_text)
    #print(d1.decrypt())


