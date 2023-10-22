from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
zero = 0
one = 0
pos = PriorityQueue()
neg = PriorityQueue()
result = 0

for _ in range(N):
    num = int(input())
    if (num == 0):
        zero += 1
    elif (num == 1):
        one += 1
    elif (num > 1):
        pos.put(num)
    else:
        neg.put(num)

while (not neg.empty()):
    if (neg.qsize() % 2 == 0):
        num1 = neg.get()
        num2 = neg.get()
        result += (num1 * num2)
    else:
        for _ in range(neg.qsize() // 2):
            num1 = neg.get()
            num2 = neg.get()
            result += (num1 * num2)
        if (zero == 0):
            result += neg.get()
        else:
            result += (neg.get() * 0)

while (not pos.empty()):
    if (pos.qsize() % 2 == 0):
        num1 = pos.get()
        num2 = pos.get()
        result += (num1 * num2)
    else:
        result += pos.get()
        for _ in range(pos.qsize() // 2):
            num1 = pos.get()
            num2 = pos.get()
            result += (num1 * num2)

result += one

print(result)
