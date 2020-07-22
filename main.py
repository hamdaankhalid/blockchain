from blockchain import BlockChain

class Main:
    if __name__ == '__main__':
        chain = BlockChain()
        chain.add_new_transaction(["Hamdaan ", 45, "Jason"])
        chain.mine()
        chain.add_new_transaction(["Jason", 45, "Jackson"])
        chain.mine()
        chain.add_new_transaction(["Missi", 45, "ssippi"])
        chain.mine()

        for i in chain.chain:
            print(i.data, i.timestamp)