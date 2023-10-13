import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0

while (N != 1):
    if (N % K == 0):
        N = N // K
        count += 1
    else:
        N -= 1
        count += 1
        
print(count)


"""
    # Another Solution #

    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    result = 0

    while (True):
        target = (N // K) * K
        result += (N - target)
        N = target
        
        if (N < K):
            break
            
        result += 1
        N //= K
        
    result += (N - 1)
    print(result)
"""