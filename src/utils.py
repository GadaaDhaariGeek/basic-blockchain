import hashlib
from datetime import datetime

# upper limit on nonce value
global NONCE_MAX_VALUE
NONCE_MAX_VALUE = 2**24
print(f"nonce upper limit: {NONCE_MAX_VALUE}")

class Block:
    """
    class representing a block. 
    It has all the attributes of a block, where data, node_id and previous block's hash is provided, 
    while creating a block.
    """
    def __init__(self, data, node_id, previous_block_hash):
        """initialization of a block.

        Args:
            data (str): String data
            node_id (int): node id of the node which created this block
            previous_block_hash (hash str): has string of previous block 
        """
        self.current_timestamp = datetime.now()
        self.nonce = 0
        self.node_id = node_id
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.hash = self._calculate_block_hash()
        
    def _calculate_block_hash(self):
        """ method to calculate the hash of the block using the block's data, previous block's hash and nonce.

        Returns:
            string: hash string of the block
        """
        sha1 = hashlib.sha1()
        sha1.update(
            str(self.data).encode('utf-8') + \
            str(self.previous_block_hash).encode('utf-8') + \
            str(self.nonce).encode('utf-8')
        )
        return sha1.hexdigest()

    def proof_of_work(self, k):
        """Method to find nonce value for which PoW equation (1) holds true.

        Args:
            k (int): difficulty = 2^k.  

        Returns:
            bool: whether the nonce found or not with given bounds of nonce range. 
        """
        lhs = self.hash
        rhs = "0"*k
        while lhs[:k] != rhs:
            self.nonce += 1
            if self.nonce > NONCE_MAX_VALUE:
                return False
            lhs = self._calculate_block_hash()
        self.hash = lhs
        # print(f"Nonce found: {self.nonce}, Hash: {self.hash}")   
        return True

class BlockChain:
    """Class to represent a blockchain.
    It will have a chain with blocks in it. 
    First block is genesis block, created right after the blockchain is instantiated.
    """
    def __init__(self):
        self.chain = []
        res, block = self.add_block("First Block", "-1", "0", 4)
        if res:
            self.chain.append(block)

    def add_block(self, data, node_id, previous_block_hash, k):
        """Method to create a block, calculate the correct nonce for it (mining).
        If correct nonce found, add the nonce and append the block into the blockchain.

        Args:
            data (str): data orf block
            node_id (int): id of the node which is creatin this block
            previous_block_hash (str): previous block's hash
            k (int): parameter to adjust the difficulty (d)

        Returns:
            (bool, Block): whether the correct nonce was found and block is added or not.
        """
        block = Block(data, node_id, previous_block_hash)
        res = block.proof_of_work(k)
        if res:
            self.chain.append(block)
        return res, block

class Node:
    """class to represent a node. 
    this node has its node id, and a blockchain on which it will try to propose a block.
    """
    def __init__(self, blockchain_obj, node_id):
        self.id = node_id
        self.blockchain = blockchain_obj
        
    def propose_block(self, data, k):
        """Method to propose a block for the given blockchain

        Args:
            data (str): string data
            k (int): parameter to adjust the difficulty (d)

        Returns:
            bool: whether it was able to propose the block
        """
        previous_block_hash = self.blockchain.chain[-1].hash
        res, _ = self.blockchain.add_block(data, self.id, previous_block_hash, k)
        return res
        # return True