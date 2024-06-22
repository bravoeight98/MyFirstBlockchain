import hashlib

class MFB_Block:

    def __init__ (self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 MC to Mike" 
t2 = "Bob sends 4.1 MC to Mike" 
t3 = "Mike sends 3.2 MC to Bob" 
t4 = "Daniel sends 0.3 MC to Anna" 
t5 = "Mike sends 1 MC to Charlie" 
t6 = "Mike sends 5.4 MC to Daniel"