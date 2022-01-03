# Linked List 

# 연결 리스트 
# 배열은 순차적으로 연결된 공간에 데이터를 나열하는 데이터구조 
# 링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결하여 관리하는 데이터구조 (배열의 단점을 보완함)
# C언어에서는 주요 데이터구조이지만, 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원하고 있다. 

# 기본구조와 용어 
# * Node : 데이터 저장 단위 (데이터값, (주소)포인터) 로 구성 
# * Pointer : 각 노드 안에서 다음이나 이전의 노드와의 연결정보를 가지고 있는 공간 

# 파이썬에서 링크드 리스트 구현시 파이썬 클래스를 활용한다. 

# 장점 (C언어에서의 배열과 링크드리스트)
# * 미리 데이터 공간을 할당하지 않아도 됨.
# 단점 
# * 연결을 위한 별도 데이터 공간이 필요하므로, 저장공간 효율이 높지 않음
# * 연결정보를 찾는 시간이 필요하므로 접근 속도가 느림
# * 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야하는 부가적인 작업이 필요함 


# 포인트를 활용하여 Node와 Node 연결하기 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

# 링크드 리스트로 데이터 추가하기
node1 = Node(1)
head = node1
for index in range(1, 10):
    add(index)

# 링크드 리스트 데이터 출력하기 (검색하기)
node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)


# 노드 중간에 새로운 노드를 입력하고 싶을 때 
node3 = Node(1.5)
search = True

while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next


# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next 
    
    def delete(self, data):
        if self.head == '':
            print("해당값을 가진 노드가 없습니다.")
            return
        
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp

                else:
                    node = node.next

linkedList1 = NodeMgmt(0)
linkedList1.desc()

print(linkedList1.head)
linkedList1.delete(0)
print(linkedList1.head)

for data in range(1,10):
    linkedList1.add(data)
linkedList1.desc()

linkedList1.delete(4)
linkedList1.desc()


# 더블링크드리스트 
# 이전링크주소 | 데이터 | 다음링크주소 로 이루어진 노드.
# 앞뒤로 검색이 가능한 이점이 있다. 

class DoubleNode:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleNodeMgmt:
    def __init__(self, data):
        self.head = DoubleNode(data)
        self.tail = head

    def insert(self, data):
        if self.head == None:
            self.head = DoubleNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = DoubleNode(data)
            node.next = new
            new.prev = node
            self.tail = new
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_from_head(self, data):
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    def search_from_tail(self, data):
        if self.tail == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = DoubleNode(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.next = node
            new.prev = before_new
            node.prev = new 
            return True



double_linked_list = DoubleNodeMgmt(0)
for data in range(1,10):
    double_linked_list.insert(data)

double_linked_list.desc()


node_3 = double_linked_list.search_from_head(10)
print(node_3.data)

# 2 앞에 1.5입력 
double_linked_list.insert_before(1.5, 2)

        