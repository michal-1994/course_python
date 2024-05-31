from uuid import uuid4

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        self.private_key = 'private_key_' + str(uuid4())
        self.public_key = 'public_key_' + str(uuid4())

    def load_keys(self):
        pass
