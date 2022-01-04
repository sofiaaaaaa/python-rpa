# 트리 구조 

# 1. 노드 클래스 만들기 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2. 이진 탐색트리에 데이터 넣기 
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current.node.value:
                if self.current_node.left != None:
                    self.currenct_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.currenct_node = self.currenct_node.right
                else:
                    self.current_node.right = Node(value)
                    break        
