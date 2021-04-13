class Encryption:
    """
        Class Encryption is for operations conneted with encrypting the text.
        ...
        Attributes
        ----------
        key:
            basic key for monoalphabetic cipher

        text_for_encryption:
            text that will be encrypted

        Methods
        -------
         encrypt():
            encrypts the text
        """
    def __init__(self, key, text_for_encryption):
        self.key = key
        self.text_for_encryption = text_for_encryption

    def encrypt(self):
        """
        Encrypting the text.
        :return: encrypted text in string
        """
        text = str(self.text_for_encryption)
        encrypted_text = []
        for i in text:
            encrypted_text.append(self.key.get(i, i))
        encrypted_string = ""
        return encrypted_string.join(encrypted_text)
