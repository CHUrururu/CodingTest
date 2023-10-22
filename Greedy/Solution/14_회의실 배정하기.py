import sys
input = sys.stdin.readline

N = int(input())
data = [[0] * 2 for _ in range(N)]
end = 0
count = 0

for i in range(N):
    S, E = map(int, input().split())
    data[i][0] = E
    data[i][1] = S
    
data.sort()

for i in range(N):
    if (data[i][1] >= end):
        count += 1
        end = data[i][0]
        
print(count)
