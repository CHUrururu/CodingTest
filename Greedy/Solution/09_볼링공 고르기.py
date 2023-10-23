import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = list(map(int, input().split()))
count = 0

for i in range(N - 1):
    for j in K[i + 1:]:
        if (K[i] != j):
            count += 1
            
print(count)
