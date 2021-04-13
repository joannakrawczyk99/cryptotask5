class Key:
    """
        Class Key is for operations conneted with key.
        ...
        Attributes
        ----------
        key:
            a basic key for monoalphabetic cipher

        Methods
        -------
         createReverseKey():
            creates reverse key for decryption
        """

    def __init__(self, key):
        self.key = key

    def createReverseKey(self):
        """
        Creating reverse key for decryption
        :return: reversed key
        """
        reversed_key = {}
        for i, j in self.key.items():
            reversed_key[j] = i
        return reversed_key