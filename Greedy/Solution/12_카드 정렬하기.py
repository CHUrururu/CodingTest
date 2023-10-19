from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
result = 0

for i in range(N):
    pq.put(int(input()))

while (pq.qsize() > 1):
    A = pq.get()
    B = pq.get()
    pq.put(A + B)
    result += (A + B)

print(result)



"""
    # Another Solution #
    
    from queue import PriorityQueue

    N = int(input())
    pq = PriorityQueue()

    for _ in range(N):
        data = int(input())
        pq.put(data)

    data1 = 0
    data2 = 0
    sum = 0

    while (pq.qsize() > 1):
        data1 = pq.get()
        data2 = pq.get()
        temp = data1 + data2
        sum += temp
        pq.put(temp)

    print(sum)
"""
