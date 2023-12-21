import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # 재귀 최대 깊이 설정

N, M = map(int, input().split())
data = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

def DFS(n):
    visited[n] = True
    for i in data[n]:
        if not visited[i]:
            DFS(i)

for _ in range(M):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        DFS(i)
    
print(count)
