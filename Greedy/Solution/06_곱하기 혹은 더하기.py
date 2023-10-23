import sys
input = sys.stdin.readline

S = input().rstrip()
result = int(S[0])

for i in S[1:]:
    num = int(i)
    if (result <= 1 or num <= 1):
        result += num
    else:
        result *= num
        
print(result)
