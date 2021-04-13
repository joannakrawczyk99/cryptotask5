class Key:

    def __init__(self, key):
        self.key = key

    def createReverseKey(self):
        reverse_key = {}
        for i, j in self.key.items():
            reverse_key[j] = i
        return reverse_key