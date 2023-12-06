from itertools import combinations

N = int(input())
board = []
teachers = []
spaces = []
for i in range(N):
    board.append(list(input().split()))
    for j in range(N):
        if (board[i][j] == 'T'):
            teachers.append((i, j))
        if (board[i][j] == 'X'):
            spaces.append((i, j))
            
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if (direction == 0):
        while (y >= 0):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            y -= 1
    
    # 오른쪽 방향으로 감시        
    if (direction == 1):
        while (y < N):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            y += 1
    
    # 위쪽 방향으로 감시        
    if (direction == 2):
        while (x >= 0):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            x -= 1
    
    # 아래쪽 방향으로 감시        
    if (direction == 3):
        while (x < N):
            if (board[x][y] == 'S'):
                return True
            if (board[x][y] == 'O'):
                return False
            x += 1
            
    return False

# 감시 진행
def process():
    for x, y in teachers:
        for i in range(4):
            if (watch(x, y, i)):
                return True
            
    return False

hide = False

# 장애물을 설치할 수 있는 모든 조합 확인
for data in combinations(spaces, 3):
    for x, y in data:
        board[x][y] = 'O'
        
    # 학생이 발견되지 않는 경우 '숨기 성공'
    if not (process()):
        hide = True
        break
        
    for x, y in data:
        board[x][y] = 'X'
        
if (hide):
    print('YES')
else:
    print('NO')
