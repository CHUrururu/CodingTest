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



"""
    # Another Solution #
    
    from queue import PriorityQueue

    N = int(input())
    plusPq = PriorityQueue()
    minusPq = PriorityQueue()
    one = 0
    zero = 0

    for i in range(N): # 4가지로 데이터 분리 저장
        data = int(input())
        if (data > 1):
            plusPq.put(data * -1) # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
        elif (data == 1):
            one += 1
        elif (data == 0):
            zero += 1
        else:
            minusPq.put(data)

    sum = 0

    while (plusPq.qsize() > 1): # 양수 처리
        first = plusPq.get() * -1
        second = plusPq.get() * -1
        sum += (first * second)

    if (plusPq.qsize() > 0):
        sum += (plusPq.get() * -1)

    while (minusPq.qsize() > 1): # 음수 처리
        first = minusPq.get()
        second = minusPq.get()
        sum += (first * second)

    if (minusPq.qsize() > 0):
        if (zero == 0):
            sum += minusPq.get()

    sum += one

    print(sum)
"""
