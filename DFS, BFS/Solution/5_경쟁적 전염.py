from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = []
virus = []
for i in range(N):
    data.append(list(map(int, input().split())))
    for j in range(N):
        if (data[i][j] != 0):
            virus.append((data[i][j], 0, i, j)) # (바이러스 종류, 시간, x 좌표, y 좌표)
            
virus.sort()
q = deque(virus)

S, X, Y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while (q):
    v, t, x, y = q.popleft()
    
    if (t == S):
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx >= 0 and nx < N and ny >= 0 and ny < N):
            if (data[nx][ny] == 0):
                data[nx][ny] = v
                q.append((v, t + 1, nx, ny))
                
print(data[X - 1][Y - 1])
