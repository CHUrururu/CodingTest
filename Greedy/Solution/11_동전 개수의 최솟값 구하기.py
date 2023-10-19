import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
count = 0

for _ in range(N):
    a = int(input())
    A.append(a)
    
A = sorted(A, reverse = True)

for a in A:
    if (K >= a):
        count += (K // a)
        K -= (K // a) * a
        if (K == 0):
            break
            
print(count)
