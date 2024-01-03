# N = 4
# stages = [4, 4, 4, 4, 4]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    failure = []
    answer = []
    
    for i in range(1, N + 1):
        a = stages.count(i)
        b = 0
        for j in stages:
            if (j >= i):
                b += 1
        
        if (a == 0 or b == 0):
            failure.append((0, i))
        else:
            failure.append((a / b, i))

    failure.sort(key = lambda x : (-x[0], x[1]))
    
    for i in failure:
        answer.append(i[1])
    
    return answer

print(solution(N, stages))
