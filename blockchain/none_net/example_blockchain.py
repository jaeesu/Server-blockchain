from hashlib import sha256

blockchain = []

def make_genesis_block():
    """making the frist block"""
    data = 'Genesis'
    prev_hash = b''
    current_hash = make_hash(data, prev_hash)
    blockchain.append((data, prev_hash, current_hash))

def make_hash(data: str, prev_hash: bytes) -> bytes:
    """making hash"""
    return sha256(data.encode() + prev_hash).digest()

def add_block(data: str):
    """insert the block to block chain"""
    _, _, prev_hash = blockchain[-1]
    current_hash = make_hash(data, prev_hash)
    blockchain.append((data, prev_hash, current_hash))

def show_blockchain():
    """show the block chain"""
    """이전에 해시값을 bytes로 바꿨기 때문에, hex로 16진수로 변환 """
    for i, (data, prev_hash, current_hash) in enumerate(blockchain):
        print(f'블록 {i}\n{data}\n{prev_hash.hex()}\n{current_hash.hex()}')

def verify_blockchain():
    """verifying the block chain"""
    for i in range(1, len(blockchain)):
        data, prev_hash, current_hash = blockchain[i]
        last_data, last_prev_hash, last_current_hash = blockchain[i-1]
        if prev_hash != last_current_hash:
            #1.현 블록의 이전 해시 값과 이전 블록의 현재 해시 값이 일치하는지 확인
            #blockchain[i]와 blockchain[i-1]의 current_hash 값을 비교
            print(f"블록 {i} 이전 해시 != 블록 {i-1} 현 해시.\n"
                    f"{prev_hash.hex()} != \n{last_current_hash.hex()}")
            return False
        if last_current_hash != (temp := make_hash(last_data, last_prev_hash)):
            #2.이전 블록을 해시 함수로 검증, 이 부분 없이는 genesis 블록의 검증이 안됨
            print(f"블록 {i-1} 검증 실패.\n"
                    f"{last_current_hash.hex()} != \n{temp.hex()}")
            return False
        if current_hash != (temp := make_hash(data, prev_hash)):
            #3. 현 블록을 해시 함수로 검증
            print(f"블록 {i}, 검증 실패. \n"
                    f"{current_hash.hex()} != \n{temp.hex()}")
            return False
        #print(f'[Block {i}: {blockchain[i][0]}] has been verified.')
        return True

make_genesis_block()
add_block('나는미남이다')
add_block('진짜미남이다')
add_block('아님말고')
show_blockchain()
print()
print(verify_blockchain())
