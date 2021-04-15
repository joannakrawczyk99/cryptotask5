import unittest

import decryption
import encryption
import key


class MyTestCase(unittest.TestCase):
    def test_init_key(self, key_to_encrypt=None):
        k1 = key.Key(key_to_encrypt)
        mess = 'Given object is not instance of Key'
        self.assertIsInstance(k1, key.Key, mess)

    def test_init_encryption(self, key_to_encrypt=None, text_for_encryption=None):
        e1 = encryption.Encryption(key_to_encrypt, text_for_encryption)
        mess = 'Given object is not instance of Encryption'
        self.assertIsInstance(e1, encryption.Encryption, mess)

    def test_init_decryption(self, reversed_key=None, encrypted_text=None):
        e1 = decryption.Decryption(reversed_key, encrypted_text)
        mess = 'Given object is not instance of Decryption'
        self.assertIsInstance(e1, decryption.Decryption, mess)

if __name__ == '__main__':
    unittest.main()
