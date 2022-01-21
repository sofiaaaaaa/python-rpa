# Depth-First Search 깊이 우선 탐색 
# BFS에서 need_visit를 스택으로 구현하는게 차이점. 


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

def dfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)
    count = 0
    while need_visit:
        count += 1
        node = need_visit.pop() # 맨끝에 있는 인덱스를 빼온다. 
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node]) # 리스트를 뒤에 붙여준다.

    print(count)
    return visited

print(bfs(graph, 'A'))
