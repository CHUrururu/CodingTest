from collections import deque

N, M, V = map(int, input().split()) # 정점 수, 간선 수, 탐색 시작 번호
data = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)
    
for i in range(N + 1): # 정점 번호가 작은 것부터 방문하기 위해 정렬
    data[i].sort()
    
def DFS(V):
    visited[V] = True
    
    print(V, end = ' ')
    
    for i in data[V]:
        if not visited[i]:
            DFS(i)
            
visited = [False] * (N + 1)
DFS(V)
            
def BFS(V):
    q = deque()
    q.append(V)
    visited[V] = True
    
    while (q):
        n = q.popleft()
        print(n, end = ' ')
        
        for i in data[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

print()
visited = [False] * (N + 1) # 방문 리스트 초기화
BFS(V)
