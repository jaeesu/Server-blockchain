from hashlib import sha256

prev_hash = b'Genesis'
for _ in range(3):
    print(prev_hash.hex())
    prev_hash = sha256(prev_hash).digest()
print(prev_hash.hex())


#중간의 해시값을 하나라도 조작하면 줄줄이 산으로 간다 -> 이 원리를 보안에 이용하는 것이 블록체인
