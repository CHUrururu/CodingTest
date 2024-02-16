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



"""
    # Another Solution #

    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    weight = [0] * (M + 1)

    for x in data:
        weight[x] += 1

    result = 0
    for i in range(1, M + 1):
        N -= weight[i]
        result += weight[i] * N
            

    print(result)
"""
