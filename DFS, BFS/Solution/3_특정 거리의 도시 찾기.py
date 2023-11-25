import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
list = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    list[s].append(e)
    
d = [-1] * (N + 1)
d[X] = 0

q = deque([X])

while (q):
    now = q.popleft()
    
    for next in list[now]:
        if (d[next] == -1):
            d[next] = d[now] + 1
            q.append(next)
            
check = False

for i in range(1, N + 1):
    if (d[i] == K):
        print(i)
        check = True
        
if (check == False):
    print(-1)
