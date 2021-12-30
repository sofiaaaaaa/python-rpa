# 큐 
# 가장 먼저 넣은 데이터를 가장 먼저 꺼내는 구조 
# 선입선출 FIFO 또는  LILO 방식  스택과 반대 순서
# https://visualgo.net/en/list 참조 

# dequeue : 출력시 head 요소 제거
# enqueue : 입력시 tail 에 추가

# 파이썬 큐 라이브러리
# Queue() 일반적인 큐 구조
# LifoQueue() 스택 구조 (후입선출)
# PriorityQueue() 데이터마다 우선순위가 있어서 우선순위가 높은 순으로 데이터 출력됨

# 큐는 멀티태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 사용된다.  

# Queue()로 큐 만들기
import queue

data_queue = queue.Queue() # Queue클래스 
data_queue.put("a")
data_queue.put("1")

# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.get())
# print(data_queue.qsize())


# LifoQueue()로 큐 만들기 
data_queue = queue.LifoQueue() 
data_queue.put("a")
data_queue.put("1")
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.get())
# print(data_queue.qsize())


# PriorityQueue() 로 큐 만들기 
data_queue = queue.PriorityQueue() 
data_queue.put((10, "1")) # 튜플로 입력 (우선순위, 데이터)
data_queue.put((4,"2"))
data_queue.put((1,"3"))
# print(data_queue.qsize())
# print(data_queue.get())
# print(data_queue.get())
# print(data_queue.qsize())


# enqueue, dequeue 기능 구현
queue_list = list()
def enqueue(data):
    queue_list.append(data)


def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(dequeue())