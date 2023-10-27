M, N = map(int, input().split())

key = [list(map(int, input().split())) for _ in range(M)]
lock = [list(map(int, input().split())) for _ in range(N)]

def rotate_90(key):
    n = len(key)
    m = len(key[0])
    new_key = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_key[j][n - i - 1] = key[i][j]
            
    return new_key

def check(new_lock):
    lock_length = len(new_lock) // 3
    
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if (new_lock[i][j] != 1):
                return False
    
    return True

def solution(key, lock):
    new_lock = [[0] * (N * 3) for _ in range(N * 3)]
    
    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]
            
    for rotation in range(4):
        key = rotate_90(key)
        
        for x in range((N - M + 1), N * 2):
            for y in range((N - M + 1), N * 2):
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]
                        
                if (check(new_lock) == True):
                    return True
                
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]
                        
    return False

print(solution(key, lock))
