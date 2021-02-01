#pow : 어떻게 새 블록이 생성되고 채굴되는지 보여주는 알고리즘

from hashlib import sha256

x=5
y=0

while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
    y += 1

print(f'The solution is y = {y}')
