# 최단경로 알고리즘
# 두노드를 잇는 가장 짧은 경로를 찾는 문제
# * 종류 
# 1. 단일 출발 및 단일 도착 최단경로 - 그래프 내의 특정 노드 u에서 출발, 또다른 특정 노드 v에 도착하는 가장 짧은 경로를 찾는 문제 
# 2. 단일 출발 최단경로 - 그래프 내의 특정 노드 u와 그래프 내 다른 모드 노드 각각의 가장 짧은 경로를 찾는 문제 
# 3. 전체 쌍 최단 경로 - 그래프 내의 모든 노드쌍에 대한 최단 경로를 찾는 문제 

# * 다익스트라 알고리즘 : 단일 출발 최단경로 문제에 해당한다. 하나의 정점에서 다른 모든 정점 간의 각각 가장 짧은 거리를 구하는 문제이다. 
# * 다익스트라 알고리즘 로직 : 
# 첫 정점을 기준으로 연결되어있는 정점들을 추가해가며, 최단 거리를 갱신하는 기법
# 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사하다. 
# 1. 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 2. 첫정점의 인접 노드간의 거리부터 먼저 계산하면서, 3. 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트한다. 
# 우선순위 큐는 MinHeap (최소값이 루트노드에 위치하는 트리구조) 방식을 활용하여, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 된다. 
# 1) 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장한다. 
#   - 초기에는 첫정점의 거리는 0, 나머지는 무한대로 저장한다. (inf로 표현)
#   - 우선순위 큐에 (첫 정점, 거리 0)만 먼저 넣는다. 
# 2) 우선순위 큐에서 노드를 꺼낸다. 
# - 처음에는 첫 정점만 저장되어 있으므로, 첫정점만 꺼내짐
# - 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다. 
# - 배열에 저장되어 있는 거리보다, 첫 정점에서 해당노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다. 
# - 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다. 
# 3) 2번의 과정을 우선순위 큐에서 꺼낼 노드가 없을 때까지 반복한다. 

# * 시간복잡도  
# 각 노드마다 인접한 간선을 모두 검사하는 과정과 우선순위 큐에 노드/거리 정보를 넣고 삭제하는 과정을 더해야한다. (우선순위큐는 트리구조이므로 logE의 시간이 걸리고, O(E)에서 E는 간선의 갯수를 의미한다. )
# O(E) + (O(E) + O(logE)) = O(E + ElogE) = O(ElogE) 


# 다익스트라 알고리즘 구현 

# 우선순위큐 
import heapq

# 데이터가 리스트형태일 경우, 0번 인덱스를 우선순위로 인지하여, 우선순위가 낮은 순서대로 (pop)뽑을 수 있음
queue = []
heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C']) # 이값이 가장 작으므로 맨 처음에 위치하게 된다. 
heapq.heappush(queue, [7, 'D'])
# print(queue) 

for index in range(len(queue)):
    print(heapq.heappop(queue))
    


# 방향그래프 (간선의 방향성이 있는 그래프)
myGraph = {
    'A': {'B':8, 'C':1, 'D':2},
    'B': {},
    'C': {'B':5, 'D':2}, 
    'D': {'E':3, 'F':5},
    'E': {'F':1},
    'F': {'A':5}
}

def dijksta(graph, start):
    # A부터 각 노드까지의 총 거리를 dict형태로 저장 
    distances = {node: float('inf') for node in graph }
    distances[start] = 0
    # 우선순위 큐 
    queue = []

    # 우선순위 큐에 시작 노드를 추가한다.
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 시작점에서 특정 노드까지의 거리가 우선순위큐에서 나온 거리보다 적으면 스킵처리. (해당 로직을 추가함으로써 알고리즘의 실행 시간을 줄일 수 있다.)
        if distances[current_node] < current_distance:
            continue

        # adjacent : 노드 이름, weight : 노드 간의 거리 
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            # 만약에 시작점에서 현재 노드간의 거리가 작으면 업데이트하기  
            if distance < distances[adjacent]: 
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances
                


# print(dijksta(myGraph, 'A'))


# 최단 경로 출력: 탐색할 그래프의 시작 정점과 다른 정점들간의 최단 거리 및 최단 경로 출력하기 
def dijkstra_print_path(graph, start, end):

    # 시작 정점에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대로 초기화한다.
    distances = {vertex: [float('inf'), start] for vertex in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화 
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성, 그래프의 시작정점과 시작정점의 거리를 최소힙에 추가함 
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        # 큐에서 정점을 하나씩 꺼내어 인접한 정점들의 가중치를 모두 확인해서 업데이트한다. 

        current_distance, current_vertex = heapq.heappop(queue)

        # 더 짧은 경로가 저장되어 있다면 스킵한다. 
        if distances[current_vertex][0] < current_distance:
            continue
    
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # 만약에 시작정점에서 인접정점으로 바로 가는 것보다 현재 정점을 경유해서 가는게 더 빠른 경우 
            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print(path_output)
    return distances

print(dijkstra_print_path(myGraph, 'A', 'F'))
