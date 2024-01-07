N = input()

numbers = []
for num in N:
    numbers.append(int(num))
    
numbers.sort(reverse = True)

for num in numbers:
    print(num, end = '')
    


"""
    # Another Solution #
    
    import sys
    input = sys.stdin.readline
    print = sys.stdout.write
    
    N = list(input())
    
    # 선택 정렬
    for i in range(len(N)):
        max = i
        for j in range(i + 1, len(N)):
            if (N[j] > N[max]):
                max = j
                
        if (N[i] < N[max]):
            N[i], N[max] = N[max], N[i]
            
    for num in N:
        print(num)
"""
    


"""
    # Another Solution #
    
    N = list(input())
    N_num = list(map(int, N))
        
    N_num.sort(reverse = True)
    
    for num in N_num:
        print(num, end = '')
"""
