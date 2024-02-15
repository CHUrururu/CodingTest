import sys
input = sys.stdin.readline

S = input().rstrip()
group = ''
count0 = 0
count1 = 0

for num in S:
    if (num != group):
        group = num
        if (group == '0'):
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
