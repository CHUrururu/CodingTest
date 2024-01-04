N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
numbers.sort()

for number in numbers:
    print(number)
    


"""
    # Another Solution #
    
    N = int(input())
    
    numbers = []
    for_ in range(N):
        numbers.append(int(input()))
        
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if (numbers[j] > numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
    for number in numbers:
        print(number)
"""
