# Stack 
# 가장 나중에 쌓은 데이터를 먼저 빼낼 수 있는 데이터구조 LIFO구조 
# 스택은 컴퓨터 내부의 프로세스 구조의 함수 동작 방식으로 활용된다. 

# 주요 기능 
# push 
# pop 


# 재귀함수 (함수의 동작방식이 스택과 유사하다)
def recursive(data):
    if data < 0: 
        print("ended")
    else:
        print("data")
        recursive(data - 1)
        print("returned", data)

recursive(4)

# 스택 장점 : 
# * 구조가 단순해서 구현이 쉽다. 
# * 데이터 저장/읽기 속도가 빠르다.
# 스택 단점 : 
# * 데이터 최대갯수를 미리 정해야한다. 파이썬은 재귀함수를 1000번까지만 호출 가능하다. 
# * 저장공간의 낭비가 발생할 수 있다. 미리 최대 갯수만큼 저장 공간을 확보해야함

data_stack = list()
data_stack.append(1)
data_stack.append(2)

print(data_stack.pop())


stack_list = list()

def push(data):
    stack_list.append(data)

def pop(data):
    data = stack_list[-1]
    del stack_list[-1]
    return

for index in range(10):
    push(index)

print(pop())

