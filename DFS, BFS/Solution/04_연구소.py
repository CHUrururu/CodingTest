import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = []
temp = [[0] * M for _ in range(N)]

for _ in range(N):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx >= 0 and nx < N and ny >= 0 and ny < M):
            if (temp[nx][ny] == 0):
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if (temp[i][j] == 0):
                score += 1
                
    return score

def dfs(count):
    global result # 함수 밖에서 전역변수를 선언하였다면 함수 안에서도 사용을 명시해줄 것
    
    # 울타리가 3개 설치된 경우
    if (count == 3):
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]
        
        # 각 바이러스의 위치에서 전파 진행        
        for i in range(N):
            for j in range(M):
                if (temp[i][j] == 2):
                    virus(i, j)
                    
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리 설치
    for i in range(N):
        for j in range(M):
            if (data[i][j] == 0):
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
                
dfs(0)
print(result)
