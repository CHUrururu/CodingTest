N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화
max_val = -int(1e9)
min_val = int(1e9)

def dfs(i, now):
    global max_val, min_val, add, sub, mul, div
    
    # 모든 연산자를 다 사용한 경우, 최댓값, 최솟값 업데이트
    if (i == N):
        max_val = max(max_val, now)
        min_val = min(min_val, now)
    else:
        if (add > 0):
            add -= 1
            dfs(i + 1, now + A[i])
            add += 1
        if (sub > 0):
            sub -= 1
            dfs(i + 1, now - A[i])
            sub += 1
        if (mul > 0):
            mul -= 1
            dfs(i + 1, now * A[i])
            mul += 1
        if (div > 0):
            div -= 1
            dfs(i + 1, int(now / A[i]))
            div += 1
        
dfs(1, A[0])

print(max_val)
print(min_val)
