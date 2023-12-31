from collections import deque

N, M = map(int, input().split())
data = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    num = input()
    for j in range(M):
        data[i][j] = int(num[j])
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
        
def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while (q):
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx and nx < N and 0 <= ny and ny < M):
                if (not visited[nx][ny] and data[nx][ny] != 0):
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    data[nx][ny] = data[x][y] + 1
                    
    return data[N - 1][M - 1]

print(BFS(0, 0))
