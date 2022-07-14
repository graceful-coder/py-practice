# Create a BLOCKCHAIN
# Each Block will have:
#  1) List of Transactions 
#  2) Previous Hash 
#  3) A Hash i.e. a digital signature based on the list of transactions & previous hash

class Block:

    __previousHash = 0
    __transactions = ()

    __blockHash = 0

    def __init__(self, previousHash, transactions):
        self.__previousHash = previousHash
        self.__transactions = transactions

        contents = (hash(transactions), previousHash)

        self.__blockHash = hash(contents)

    def getPreviousHash(self):
        return self.__previousHash

    def getTransactions(self):
        return self.__transactions

    def getBlockHash(self):
        return self.__blockHash


# Create three blocks that are chained together!


# Creating the Genesis Block

blockchain = []
genesisTransactions = ("satoshi sent Veronica 10 bitcoin", "hal finney sent Veronica 10 bitcoin")
genesisBlock = Block(0, genesisTransactions)

print("The digital signature i.e. the hash of the genesisBlock is ", genesisBlock.getBlockHash())

# Create blocks 2 and 3 which are each linked together by the previous block's hash

block2transactions = ("satoshi sent btc to starbucks", "satoshi rocks")

block2 = Block(genesisBlock.getBlockHash(), block2transactions)

print("The digital signature/hash of block2 is ", block2.getBlockHash())

block3transactions = ("Veronica sent Jordan 10 btc", "Veronica sent 0.5 btc to starbucks")

block3 = Block(block2.getBlockHash(), block3transactions)

print("The digital signature/hash of block3 is ", block3.getBlockHash())