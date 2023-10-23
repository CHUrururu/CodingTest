import sys
input = sys.stdin.readline

price = 1000 - int(input())
coin_types = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_types:
    count += (price // coin)
    price %= coin
    if (price == 0):
        break

print(count)
