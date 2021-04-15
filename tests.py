import unittest

import decryption
import encryption
import key


class MyTestCase(unittest.TestCase):
    def test_init_key(self):
        key_to_encrypt = {'a': 'q', 'b': 'v', 'c': 'x', 'd': 'z', 'e': 'y', 'f': 'w', 'g': 'u', 'h': 't', 'i': 's',
                          'j': 'r',
                          'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'r': 'j', 's': 'i', 't': 'h',
                          'u': 'g', 'w': 'f',
                          'y': 'e', 'z': 'd', 'x': 'c', 'v': 'b', 'q': 'a',
                          'A': 'Q', 'B': 'V', 'C': 'X', 'D': 'Z', 'E': 'Y', 'F': 'W', 'G': 'U', 'H': 'T', 'I': 'S',
                          'J': 'R', 'K': 'P',
                          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'R': 'J', 'S': 'I', 'T': 'H', 'U': 'G',
                          'W': 'F', 'Y': 'E',
                          'Z': 'D', 'X': 'C', 'V': 'B', 'Q': 'S',
                          '1': '5', '2': '9', '3': '8', '4': '7', '5': '6', '6': '4', '7': '3', '8': '2', '9': '1',
                          '.': ',', ',': '.', ':': ';', ';': ':', '?': '!', '!': '?', '-': '_', '_': '-', '(': ')',
                          ')': '(',
                          '%': '$', '$': '%', ' ': '&', '&': ' ', '+': '*', '*': '+'}
        k1 = key.Key(key_to_encrypt)
        mess = 'Given object is not instance of Key'
        self.assertIsInstance(k1, key.Key, mess)

    def test_init_encryption(self):
        key_to_encrypt = {'a': 'q', 'b': 'v', 'c': 'x', 'd': 'z', 'e': 'y', 'f': 'w', 'g': 'u', 'h': 't', 'i': 's',
                          'j': 'r',
                          'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'r': 'j', 's': 'i', 't': 'h',
                          'u': 'g', 'w': 'f',
                          'y': 'e', 'z': 'd', 'x': 'c', 'v': 'b', 'q': 'a',
                          'A': 'Q', 'B': 'V', 'C': 'X', 'D': 'Z', 'E': 'Y', 'F': 'W', 'G': 'U', 'H': 'T', 'I': 'S',
                          'J': 'R', 'K': 'P',
                          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'R': 'J', 'S': 'I', 'T': 'H', 'U': 'G',
                          'W': 'F', 'Y': 'E',
                          'Z': 'D', 'X': 'C', 'V': 'B', 'Q': 'S',
                          '1': '5', '2': '9', '3': '8', '4': '7', '5': '6', '6': '4', '7': '3', '8': '2', '9': '1',
                          '.': ',', ',': '.', ':': ';', ';': ':', '?': '!', '!': '?', '-': '_', '_': '-', '(': ')',
                          ')': '(',
                          '%': '$', '$': '%', ' ': '&', '&': ' ', '+': '*', '*': '+'}
        text_for_encryption = "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin."
        e1 = encryption.Encryption(key_to_encrypt, text_for_encryption)
        mess = 'Given object is not instance of Encryption'
        self.assertIsInstance(e1, encryption.Encryption, mess)

    def test_init_decryption(self):
        key_to_encrypt = {'a': 'q', 'b': 'v', 'c': 'x', 'd': 'z', 'e': 'y', 'f': 'w', 'g': 'u', 'h': 't', 'i': 's',
                          'j': 'r',
                          'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'r': 'j', 's': 'i', 't': 'h',
                          'u': 'g', 'w': 'f',
                          'y': 'e', 'z': 'd', 'x': 'c', 'v': 'b', 'q': 'a',
                          'A': 'Q', 'B': 'V', 'C': 'X', 'D': 'Z', 'E': 'Y', 'F': 'W', 'G': 'U', 'H': 'T', 'I': 'S',
                          'J': 'R', 'K': 'P',
                          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'R': 'J', 'S': 'I', 'T': 'H', 'U': 'G',
                          'W': 'F', 'Y': 'E',
                          'Z': 'D', 'X': 'C', 'V': 'B', 'Q': 'S',
                          '1': '5', '2': '9', '3': '8', '4': '7', '5': '6', '6': '4', '7': '3', '8': '2', '9': '1',
                          '.': ',', ',': '.', ':': ';', ';': ':', '?': '!', '!': '?', '-': '_', '_': '-', '(': ')',
                          ')': '(',
                          '%': '$', '$': '%', ' ': '&', '&': ' ', '+': '*', '*': '+'}
        k1 = key.Key(key_to_encrypt)
        reversed_key = k1.createReverseKey()
        encrypted_text = 'Lmy&nljmsmu.&ftym&Ujyulj&Iqniq&flpy&wjln&hjlgvoyz&zjyqni.'
        e1 = decryption.Decryption(reversed_key, encrypted_text)
        mess = 'Given object is not instance of Decryption'
        self.assertIsInstance(e1, decryption.Decryption, mess)

if __name__ == '__main__':
    unittest.main()
