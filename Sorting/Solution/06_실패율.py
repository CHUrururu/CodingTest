# N = 4
# stages = [4, 4, 4, 4, 4]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    answer = []
    b = len(stages)
    
    for stage in range(1, N + 1):
        a = stages.count(stage)
        
        if (b != 0):
            failure = a / b
            b -= a
        else:
            failure = 0
            
        answer.append((failure, stage))
           
    answer.sort(key = lambda x : -x[0])
    answer = [i[1] for i in answer] 
    
    return answer

print(solution(N, stages))
