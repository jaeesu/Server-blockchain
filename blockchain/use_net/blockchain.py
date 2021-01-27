#blockchain
#list, generate block, generate hash, last_block_return
#block : index, timestamp, transaction, proof, prev_hash -> immutability
#pow : 어떻게 새 블록이 생성되고 채굴되는지를 보여주는 알고리즘 -> 문제를 푸는 숫자, 답을 찾는 것
#숫자를 찾기는 어렵지만 네트워크 내의 누구에 의해서라도 증명은 쉬워야함


#pow in bitcoin -> hashcash : 채굴자들이 새로운 블록을 생성하기 위해 경쟁적으로 푸는 알고리즘, 난이도는 string에서 보여지는 문자의 개수로 정해진다.(0의 개수) : 채굴자들은 해답에 대한 보상으로 코인을 받는다.

import hashlib
import json
from time import time
from uuid import uuid4


class Blockchain(object):
    def __init__(self):
        self.chain=[]
        self.current_transactions=[]
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index':len(self.chain) + 1,
            'timestamp':time(),
            'transactions':self.current_transactions,
            'proof':proof,
            'previous_hash':previous_hash or self.hash(self.chain[-1])
        }

        #init_transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount
        })

        return self.last_block['index'] + 1
    
    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

#blockchain 구현////http 요청을 이용해 상호 거래

