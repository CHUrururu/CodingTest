import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
data = sorted(list(map(int, input().split())))

first_max = data[-1]
second_max = data[-2]

count = (M // (K + 1)) * K
count += M % (K + 1)

result = count * first_max
result += (M - count) * second_max

print(result)



"""
    # Another Solution #
    
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    data = sorted(list(map(int, input().split())))

    first_max = data[-1]
    second_max = data[-2]
    result = 0

    while (True):
        for _ in range(K):
            if (M == 0):
                break        
            result += first_max
            M -= 1

        if (M == 0):
            break
    
        result += second_max
        M -= 1
    
    print(result)
"""
