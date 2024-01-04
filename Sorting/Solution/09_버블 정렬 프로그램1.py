import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for i in range(N):
    numbers.append((int(input()), i))
    
numbers.sort()

count = 0
for i in range(N):
    if (count < numbers[i][1] - i):
        count = numbers[i][1] - i
        
print(count + 1)
