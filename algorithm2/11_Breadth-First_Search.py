# 너비 우선 탐색 (Breadth-First Search)

# * BFS와 DFS란?
# 대표적인 그래프 탐색 알고리즘 
# 너비 우선 탐색 (Breadth-First Search) : 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식 
# 한단계씩 내려가면서, 해당노드와 같은 레벨에 있는 노드들을 먼저 순회함
# 깊이 우선 탐색 (Depth First Search) : 정점의 자식들을 먼저 탐색하는 방식
# 한 노드의 자식노드를 타고 끝까지 순회한 후에 다시 돌아와서 다른 형제노드의 자식노드들을 타고 내려가며 순회하며 탐색하는 방식이다. 

# python에서는 list, dict 형태로 만든다. 
# 노드가 key값이 되고, 노드에 연결된 다른 형제, 부모, 자식 노드들을 리스트화하여 값으로 저장하는 형태이다. 
# Vistied queue (The visitied list) : 방문한 노드들을 저장하는 리스트이며, queue는 선입선출방식으로 이용한다. 
# need visit queue (The list to need to list) : 노드에 관계된 다른 노드들을 해당 리스트에 저장하고, 선입선출 방식으로 꺼내어 
# 위의 리스트에 있는지 확인하고, 없으면 위의 리스트에 저장한다. 

# * 시간복잡도 계산 : while문에 의해 O(V+E)
# 노드수 : V
# 간선수 : E 


# graph dictionary

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop(0) # 특정 인덱스를 빼온다. 
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node]) # 리스트를 뒤에 붙여준다.

    print(count)
    return visited

print(bfs(graph, 'A'))
