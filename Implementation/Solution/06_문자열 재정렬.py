import sys
input = sys.stdin.readline

S = input().rstrip()
alpha = []
sum = 0

for i in S:
    if (i.isalpha()):
        alpha.append(i)
    else:
        sum += int(i)
        
alpha = sorted(alpha)

for i in alpha:
    print(i, end = '')
    
print(sum)
