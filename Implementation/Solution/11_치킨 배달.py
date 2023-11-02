from itertools import combinations

N, M = map(int, input().split())
chicken, house = [], []

for r in range(N):
    data = list(map(int, input().split()))
    for c in range(N):
        if (data[c] == 1): # 집
            house.append((r, c))
            
        if (data[c] == 2): # 치킨집
            chicken.append((r, c))
            
candidates = list(combinations(chicken, M))

def city_chicken_distance(candidate): 
    result = 0
    
    for hx, hy in house:
        temp = 1e9
        
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        
        result += temp
        
    return result

result = 1e9
for candidate in candidates:
    result = min(result, city_chicken_distance(candidate))
    
print(result)
