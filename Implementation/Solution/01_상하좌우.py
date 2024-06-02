N = int(input())
plans = list(input().split())
x, y = 1, 1
dirs = {'L' : [0, -1],
        'R' : [0, 1],
        'U' : [-1, 0],
        'D' : [1, 0]}

for plan in plans:
    nx = x + dirs[plan][0]
    ny = y + dirs[plan][1]
    
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    else:
        x = nx
        y = ny
        
print(x, y)



"""
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

"""
