import sys
input = sys.stdin.readline

N = int(input())
plans = list(map(str, input().split()))
X, Y = 1, 1

for plan in plans:
    if (plan == 'R'):
        temp = Y + 1
        if (1 <= temp <= 5):
            Y = temp
    elif (plan == 'L'):
        temp = Y - 1
        if (1 <= temp <= 5):
            Y = temp
    elif (plan == 'U'):
        temp = X - 1
        if (1 <= temp <= 5):
            X = temp
    else:
        temp = X + 1
        if (1 <= temp <= 5):
            X = temp
            
print(X, Y)
