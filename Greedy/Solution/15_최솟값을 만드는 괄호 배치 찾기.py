ex = input().split('-')
sum = []

for i in ex:
    temp = 0
    if ('+' in i):
        num = i.split('+')
        for j in num:
            temp += int(j)
    else:
        temp += int(i)
    sum.append(temp)
       
answer = sum[0]
        
for i in sum[1:]:
    answer -= i
    
print(answer)
