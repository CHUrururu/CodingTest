import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split()) # 사람 수, 친구 관계 수
arrive = False
R = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M): # 인접 리스트
    s, e = map(int, input().split())
    R[s].append(e)
    R[e].append(s)

def DFS(now, depth):
    global arrive
    
    if (depth == 5): # 깊이가 5일 경우 종료
        arrive = True
        return
    
    visited[now] = True
    
    for i in R[now]:
        if not visited[i]:
            DFS(i, depth + 1)
            
    visited[now] = False
    
for i in range(N):
    DFS(i, 1)
    
    if (arrive):
        break
    
if (arrive):
    print(1)
else:
    print(0)    
