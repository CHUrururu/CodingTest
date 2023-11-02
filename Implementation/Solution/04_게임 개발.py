import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visit = [[0] * M for _ in range(N)]
x, y, d = map(int, input().split())
array = []

visit[x][y] = 1
count = 1

for _ in range(N):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = 0

while (1):
    d -= 1
    if (d == -1):
        d = 3
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    if (visit[nx][ny] == 0 and array[nx][ny] == 0):
        x = nx
        y = ny
        visit[x][y] = 1
        count += 1
        check = 0
        continue
    else:
        check += 1
        
    if (check == 4):
        nx = x - dx[d]
        ny = y - dy[d]
    
        if (array[nx][ny] == 0):
            x = nx
            y = ny
            check = 0
        else:
            break
        
print(count)
