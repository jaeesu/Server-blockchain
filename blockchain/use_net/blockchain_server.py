<<<<<<< HEAD
####https://medium.com/caulink/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-part-2-633bb0555221
=======
>>>>>>> 1c5716abe89de272fd6432769e9b1bf2abdc0f9f
#blockchain as api
#flask : micro - framework
#python - endpoint structure -> http 요청을 사용해 웹 기반으로 블록체인에 명령을 내림
###1./transactions/new : 블록에 새로운 거래를 만듦
###2./mine : 서버에게 새로운 블록을 채굴하라고 명령
###3./chain : 전체 블록체인을 받아내는 방법

#server : 블록체인 네트워크에서 단일 노드 형성


from blockchain import Blockchain

from textwrap import dedent
from flask import Flask, jsonify, request
from uuid import uuid4

#instantiate our node
app = Flask(__name__)

#generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-','')

#instantiate the blockchain
blockchain = Blockchain()

#채굴의 endpoint ->
#1.pow를 계산
#2.채굴자에게 거래를 추가한 것에 대한 보상으로 1코인을 준다.
#3.새 블록을 체인에 추가

@app.route('/mine', methods=['GET'])
def mine():
    # we run the pow to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    #블록 채굴에 대한 보상 설정, 송신자를 0으로 표현한 것은 블록 채굴에 대한 보상이기 때문
    blockchain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1
    )

    #insert new block into chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200
#새로운 블록 채굴 시, 그에 대한 보상을 받음
#채굴을 통해 받은 코인은 sender가 없다. 채굴된 블록에 대한 보상의 수신자가 우리 노드의 주소


#거래의 endpoint : sender, recipient, amount -> 거래 추가를 위한 함수 구현
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    #필요한 값이 모두 존재하는지 확인
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    #새로운 거래 추가
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

if __name__=='__main__':
    app.run(host="0.0.0.0", port="5000")
