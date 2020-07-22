from datetime import datetime
import hashlib
import json


class Block:
    # block contains: current hash, prev hash, and data
    def __init__(self, index, data, prev_hash, nonce = 0):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.timestamp = datetime.now().isoformat(' ', 'seconds')
        self.hash = self.calculate_hash()
        self.nonce = nonce

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

# test
# data = "Hi I am Hamdaan"
# prev_hash = 'a4337bc45a8fc544c03f52dc550cd6e1e87021bc896588bd79e901e2'
# test = Block(data, prev_hash)
# print(test.calculate_hash())
