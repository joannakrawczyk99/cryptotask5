class Decryption:
    def __init__(self, reverse_key, encrypted_text):
        self.reverse_key = reverse_key
        self.encrypted_text = encrypted_text

    def decrypt(self):
        text = str(self.encrypted_text)
        decrypted_text = []
        for l in text:
            decrypted_text.append(self.reverse_key.get(l, l))
        decrypted_string = ""
        return decrypted_string.join(decrypted_text)



