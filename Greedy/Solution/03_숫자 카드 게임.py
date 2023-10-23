import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

min = list(map(min, data))
    
print(max(min))
