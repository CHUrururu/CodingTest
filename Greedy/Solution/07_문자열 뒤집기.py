import sys
input = sys.stdin.readline

S = input().rstrip()
group = ''
count0 = 0
count1 = 0

for i in S:
    if (i != group):
        group = i
        if (group == '0'):
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))
