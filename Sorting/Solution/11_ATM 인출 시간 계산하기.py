N = int(input())
time = list(map(int, input().split()))
time.sort()
    
time_sum = 0

while (time):
    time_sum += sum(time)
    time.pop()
    
print(time_sum)
    


"""
    # Another Solution #
    
    N = int(input())
    time = list(map(int, input().split()))
    time_S = [0] * N
    
    # 삽입 정렬
    for i in range(1, N):
        insert_point = i
        insert_value = time[i]
        
        for j in range(i - 1, -1, -1):
            if (time[j] < time[i]):
                insert_point = j + 1
                break
            
            if (j == 0):
                insert_point = 0
        
        for j in range(i, insert_point, -1):
            time[j] = time[j - 1]
        
        time[insert_point] = insert_value
        
    time_S[0] = time[0]
    
    for i in range(1, N):
        time_S[i] = time_S[i - 1] + time[i]
        
    sum = 0
    
    for i in range(N):
        sum += time_S[i]
        
    print(sum)
"""
