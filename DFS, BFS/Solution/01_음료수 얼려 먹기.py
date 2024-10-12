N, M = map(int, input().split())
frame = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
        
    if not visited[x][y]:
        visited[x][y] = True
        if frame[x][y] == 0:
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
            
    return False

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
