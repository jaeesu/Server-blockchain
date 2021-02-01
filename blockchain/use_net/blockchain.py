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

<<<<<<< HEAD
<<<<<<< HEAD
    
    # make a new block : first_genesis block  +  proof
    #block : 
        #index  |  timestamp  |  transactions  |  proof : nonce |  previous_hash
        #
=======
>>>>>>> 1c5716abe89de272fd6432769e9b1bf2abdc0f9f
=======
>>>>>>> 8ed9043ca93b319da79b201d4e58f4c8f1d468eb
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
<<<<<<< HEAD
<<<<<<< HEAD
    
    #add a new transaction into block
    #add transaction into list & return index
        #sender  |  recipient  |  amount
=======

>>>>>>> 1c5716abe89de272fd6432769e9b1bf2abdc0f9f
=======

>>>>>>> 8ed9043ca93b319da79b201d4e58f4c8f1d468eb
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
<<<<<<< HEAD
<<<<<<< HEAD
    
    #결과값이 첫 4개의 0으로 이루어질 때까지 p'를 찾는 작업 증명과정
    def proof_of_work(self, last_proof) -> int:
=======

    def proof_of_work(self, last_proof):
>>>>>>> 1c5716abe89de272fd6432769e9b1bf2abdc0f9f
=======

    def proof_of_work(self, last_proof):
>>>>>>> 8ed9043ca93b319da79b201d4e58f4c8f1d468eb
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
<<<<<<< HEAD
<<<<<<< HEAD
    
    #작업증명 결과값을 검증하는 코드, 앞의 4자리가 0으로 이루어져 있는가. return값은 boolean
    @staticmethod
    def valid_proof(last_proof, proof) -> bool:
=======

    @staticmethod
    def valid_proof(last_proof, proof):
>>>>>>> 1c5716abe89de272fd6432769e9b1bf2abdc0f9f
=======

    @staticmethod
    def valid_proof(last_proof, proof):
>>>>>>> 8ed9043ca93b319da79b201d4e58f4c8f1d468eb
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

#blockchain 구현////http 요청을 이용해 상호 거래

