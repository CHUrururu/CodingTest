import sys
input = sys.stdin.readline

N = int(input())

numbers = []
for i in range(N):
    numbers.append((int(input()), i))
    
numbers.sort()

count = 0
for i in range(N):
    # 정렬 전 인덱스와 정렬 후 인덱스 비교
    if (count < numbers[i][1] - i): 
        # 왼쪽으로 가장 많이 이동한 값
        count = numbers[i][1] - i 
        
print(count + 1)
