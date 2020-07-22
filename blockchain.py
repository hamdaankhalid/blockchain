from block import Block

class BlockChain:
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """This generates genesis block and appends it to
                the chain. The block has index 0, previous_hash as 0
                """
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)
    # this property is pretty self explanatory
    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        block.nonce
        computed_hash = block.calculate_hash()
        while not computed_hash.startswith('0'* BlockChain.difficulty):
            block.nonce += 1
            computed_hash = block.calculate_hash()
        return computed_hash

    def is_valid_proof(selfself, block, block_hash):
        return block_hash.startswith('0'*BlockChain.difficulty) and block_hash == block.calculate_hash()

    def add_block(self, block, proof):
        """
        :param block:
        :param proof:
        :return: boolean

        this function adds a block, after verification if the proof is valid, and the previous hash
        attribute of the given block matches the computed hash of the previous block
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.prev_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """interface to add the pending transactions from unconfirmed transactions
         to the blockchain by adding them to the block
        and figuring out Proof Of Work  """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block(index=last_block.index+1,
                          data=self.unconfirmed_transactions,
                          prev_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index
