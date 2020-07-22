# Blockchain
Blockchain Implementation in Python

I did this project using the above sources, with my version on activestates implementation of blockchain.
I used Geek for Geeks and blockgeeks article to understand the technology.

Here I will be explaining blockchain to the best of my ability. 
Blockchains is a distributed data structure which follows the 3 major rules: 
1) Immutability of the data that we store in Blocks
2) Decentralize. This means having a peer to peer network. A peer to peer network is a distributed application architecture that consists of computing devices connected to each other, without a central server e.g. Tor.
3)Transparent and consensus, means the transactions are visible (p.s trapsaparent does not mean not private or not secure), and consensus means that immutable blocks are added to chain after some sort of verification.

As the name suggests a blockchain consists of .....blocks.LOL

Blocks Make BlockChains (it's a fancy backlinked list)
We make a chain, the chain has a genesis block with no data, index of zero, and hash of 0.
Blocks will be added to the chain from here on. (NOTE: We can only append in this datastructure and not edit once appended)
These blocks contain a hash of the previous block, data  or transaction, and a hash created for this current block. The hash of this block is made using a combination of the data and the hash of the previous block.
Since all blocks are connected to each other by their previous hash, changing data of any block changes its hash, and thus you will have the change the hashes of the blocks after (this was we create some sort of security). Changing the hash of all the blocks can be computationally timetaking and tedious. However one can still do so...
To tackle this the creator/creators/Nobody knows Satashi Nakamoto Created the first consensus algorithm called Proof Of Work. This algorithm makes it pretty much impossible to be able to change hashes of blocks after editing any of the blocks. 

The Proof Of Work Algorithm was the harder part to understand. I shall try to explain to the best of my ability now.
" Generating just any hash for a set of bitcoin transactions would be trivial for a modern computer, so in order to turn the process into "work," the bitcoin network sets a certain level of "difficulty." " (<- https://www.investopedia.com/terms/p/proof-work.asp )

" The purpose of a consensus mechanism is to bring all the nodes in agreement, that is, trust one another, in an environment where the nodes don’t trust each other.
All the transactions in the new block are then validated and the new block is then added to the blockchain. Note that, the block will get added to the chain which has the longest block height(see blockchain forks to understand how multiple chains can exist at a point of time). Miners(special computers on the network) perform computation work in solving a complex mathematical problem to add the block to the network, hence named, Proof-of-Work. With time, the mathematical problem becomes more complex. "  <- https://www.geeksforgeeks.org/proof-of-work-pow-consensus/

Coding Proof Of Work:
"""
        This Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """

def proof_of_work(self, block):
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

In this project:
P.s. Used SHA256 from hashlib library in this proj

We create blocks, create a list to store the blocks called chain, and a list to store unconfirmed transactions.
The blocks store data, prev hash , current hash, time index, and nonce
Chains are intialised with a genesis block. 
To add transactions to chain, we add transactions to unconfirmed transactions list and then when we call our mine function.
We create a block, use proof of work to create a hash for that block using its computed hash. We then use this proof of work and the block as parameters when
we call the add block function that then verifies the block by checking if the hash matches to our proof of work(done using an is_valid_proof function) and checking if the hash of the block before this block matches this blocks prev_hash attribute. After all this the block is added!

This creates a decentralized, immutable, and transparent data structure 


Articles Referenced:
https://blockgeeks.com/guides/what-is-blockchain-technology/
https://www.geeksforgeeks.org/blockchain-technology-introduction/
https://www.geeksforgeeks.org/introduction-to-blockchain/?ref=rp
https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
