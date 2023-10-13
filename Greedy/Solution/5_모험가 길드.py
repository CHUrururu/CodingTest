import sys
input = sys.stdin.readline

N = int(input())
data = sorted(list(map(int, input().split())))
member = 0
group = 0

for i in data:
    member += 1
    if (member >= i):
        group += 1
        member = 0
        
print(group)