class Decryption:
    """
        Class Decryption is for operations conneted with decrypting the text.
        ...
        Attributes
        ----------
        reverse_key:
            reversed key for monoalphabetic cipher

        encrypted_text:
            text that will be decrypted

        Methods
        -------
         decrypt():
            decrypts the text
        """
    def __init__(self, reverse_key, encrypted_text):
        self.reverse_key = reverse_key
        self.encrypted_text = encrypted_text

    def decrypt(self):
        """
        Decrypting the encrypted text.
        :return: decrypted text in string
        """
        text = str(self.encrypted_text)
        decrypted_text = []
        for l in text:
            decrypted_text.append(self.reverse_key.get(l, l))
        decrypted_string = ""
        return decrypted_string.join(decrypted_text)



