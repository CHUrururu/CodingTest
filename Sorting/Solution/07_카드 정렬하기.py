import heapq

N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))
    
count = 0

while (len(cards) != 1):
    card_1 = heapq.heappop(cards)
    card_2 = heapq.heappop(cards)
    
    combi_card = card_1 + card_2
    
    count += combi_card
    
    heapq.heappush(cards, combi_card)
    
print(count)
