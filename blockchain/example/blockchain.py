from block import Block

#블록체인 클래스 : list, all transactions, method - make a genesis_block, method - insert a block, chain validation

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        block = Block(transactions, 0)
        self.chain.append(block)
        return self.chain

    def add_block(self, transactions, previous_hash):
        previous_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def proof_of_work(self, block, difficulty = 2):
        proof = block.generate_hash()

        while proof[:2] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()

        return proof

