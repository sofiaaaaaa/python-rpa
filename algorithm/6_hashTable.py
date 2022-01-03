# Hash Table 
# 키에 데이터를 저장하는 데이터 구조 
# 파이썬에서는 dict 타입이 해쉬 테이블로 구현되어있다. 
# 배열로 미리 hash table 사이즈만큼 생성후 사용한다. (공간과 탐색 시간을 맞바꾸는 기법 )

# hash : 임의 값을 고정길이로 변환하는 것 
# hash table : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조 
# hash function : 키에 대해 산술연산을 사용해서 데이터 위치를 찾을 수 있는 함수 
# hash value 또는 hash address: key를 해싱 함수로 연산해서 해쉬값을 알아내고, 이를 기반으로 해쉬 테이블에서 해당 key에 대한 데이터 위치를 일관성있게 찾을 수 있다. 
# slot : 한개의 데이터를 저장할 수 있는 공간 
# 저장할 데이터에 대해 key를 추출할 수 있는 별도 함수도 존재할 수 있다. 


# * 해쉬테이블 제작과정
# 1. 0 열개 있는 배열 만들기 => 해쉬 테이블 만들기
hash_table = list([0 for i in range(10)])
# 2. 해쉬함수 제작
def hash_func(key):
    return key % 5

# 3. 해쉬 테이블 저장 
data1 = 'a'
data2 = 'b'
data3 = 'c'

# ord() 문자의 ASCII 코드 리턴 
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))

print(ord(data1[0]), hash_func(ord(data1[0])) )

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data('A', '11111')
storage_data('B', '22222')
storage_data('C', '33333')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data('A'))

# 해쉬 테이블의 장단점 
# * 장점
# 데이터 저장/읽기 검색속도가 빠르다.
# 키에 대한 데이터가 있는지 확인이 쉽다. 
# * 단점 
# 일반적으로 저장공간이 많이 필요하다.
# 여러키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조가 필요하다. 

# 주요 용도
# 1. 검색을 많이 하는 경우 
# 2. 저장, 삭제, 읽기가 빈번한 경우 
# 3. 캐쉬 구현시 (중복확인이 쉽다.)


# 해쉬 테이블을 리스트변수를 사용해서 만들기

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data("aa", "111")
save_data("bb", "222")
read_data("aa")


# * 충돌 해결 알고리즘  Hash Collision
# 1. Chaining 기법 
#    open hashing 기법 중 하나. 해쉬 테이블 저장공간 외의 공간을 활용한다. 
#    충돌이 일어나면 링크드 리스트 자료 구조를 이용해서 데이터를 뒤에 연결시켜 저장한다.

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return 
            
            hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = list([index_key, value])

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None



save_data("aa", "111")
save_data("bb", "222")
read_data("aa")

# 2. Linear Probing 기법 
#    closing hashing 기법. 해쉬 테이블 저장공간 안에서 해결. 
#    충돌이 일어나면, hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장한다.  


def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value # 값 업데이트 
                return 
    else: 
        hash_table[hash_address] = [index_key, value]
     

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
           if hash_table[index] == 0:
               return None
           elif hash_table[index][0] == index_key: 
               return hash_table[index][1]
    else:
        return None


# 동일한 해쉬값 조회하기 
print(hash('aa')%8)
print(hash('bb')%8)


save_data("aa", "111")
save_data("bb", "222")
read_data("aa")


# 해쉬 함수와 키 생성 함수 
# * 파이썬의 hash()함수는 실행할 때마다 값이 달라질 수 있음
# * 유명한 hash함수 : SHA(Secure Hash Algorithm, 안전한 해시 알고리즘 )
#    => 어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로 해쉬함수로 활용가능함 
#   SHA-1 , SHA-256


# SHA-1 함수 
import hashlib

data = 'test'.encode() # b'test' 와 동일 
hash_object = hashlib.sha1()
hash_object.update(data) # byte로 변환한 값을 hash값 변환
hex_dig = hash_object.hexdigest() # 16진수로 변환 
print(hex_dig)


# SHA-256 함수 

data = 'test'.encode() # b'test' 와 동일 
hash_object = hashlib.sha256()
hash_object.update(data) # byte로 변환한 값을 hash값 변환
hex_dig = hash_object.hexdigest() # 16진수로 변환 
print(hex_dig)



def get_key(data): 
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) # 16진수 문자를 10진수 숫자로 변환 

def hash_function(key):
    return key % 8

def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            elif hash_table[index][0] == index_key:
                hash_table[index][1] = value # 값 업데이트 
                return 
    else: 
        hash_table[hash_address] = [index_key, value]
     

def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
           if hash_table[index] == 0:
               return None
           elif hash_table[index][0] == index_key: 
               return hash_table[index][1]
    else:
        return None
