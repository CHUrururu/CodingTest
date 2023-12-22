import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())

# 소수 판별
def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if (num % i == 0):
            return False
    return True

def DFS(n):
    if (len(str(n)) == N):
        print(n)
    else:
        for i in range(1, 10):
            if (i % 2 == 0): # 끝자리가 짝수인 경우 2를 약수로 가짐
                continue
            if (isPrime(10 * n + i)):
                DFS(10 * n + i)
                
DFS(2)
DFS(3)
DFS(5)
DFS(7)
