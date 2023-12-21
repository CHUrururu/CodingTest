from collections import deque

N, L, R = map(int, input().split())

data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def process(x, y, index):
    # 연합을 이루고 있는 칸의 좌표 저장
    united = []
    united.append((x, y))
    
    q = deque()
    q.append((x, y))
    
    union[x][y] = index
    # 연합의 인구수
    sum = data[x][y]
    # 연합을 이루고 있는 칸의 개수
    count = 1
    
    while (q):
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx and nx < N and 0 <= ny and ny < N and union[nx][ny] == -1):
                if (L <= abs(data[nx][ny] - data[x][y]) <= R):
                    q.append((nx, ny))
                    union[nx][ny] = index
                    sum += data[nx][ny]
                    count += 1
                    united.append((nx, ny))
                    
    for i, j in united:
        data[i][j] = sum // count
        
    return

# 인구 이동 발생 횟수
total_count = 0 

while (True):
    # 연합국 번호
    index = 0
    # 연합 여부 번호 표시
    union = [[-1] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if (union[i][j] == -1):
                process(i, j, index)
                index += 1
            
    if (index == N * N):
        break
            
    total_count += 1
    
print(total_count)
