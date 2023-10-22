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
