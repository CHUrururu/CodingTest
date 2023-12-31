S = input()
answer = len(S)

for step in range(1, len(S) // 2 + 1):
    compressed = ""
    prev = S[0:step]
    count = 1
    
    for i in range(step, len(S), step):
        if (prev == S[i:i + step]):
            count += 1
        else:
            compressed += str(count) + prev if count >= 2 else prev
            prev = S[i:i + step]
            count = 1
            
    compressed += str(count) + prev if count >= 2 else prev
    
    answer = min(answer, len(compressed))
    
print(answer)
