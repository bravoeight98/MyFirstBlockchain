import hashlib

class MFB_Block:

    def __init__ (self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list