import sys
input = sys.stdin.readline
N = input().rstrip()
half = len(N) // 2
sum1 = 0
sum2 = 0

for i in N[:half]:
    sum1 += int(i)
    
for j in N[half:]:
    sum2 += int(j)
    
if (sum1 == sum2):
    print('LUCKY')
else:
    print('READY')
