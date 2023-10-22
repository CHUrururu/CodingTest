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



"""
    # Another Solution #
    answer = 0
    A = list(map(str, input().split('-')))

    def mySum(i): # -로 나뉜 그룹들의 합을 구하는 함수
        sum = 0
        temp = str(i).split('+')
        for i in temp:
            sum += int(i)
        return sum

    for i in range(len(A)):
        temp = mySum(A[i])
        if i == 0:
            answer += temp # 가장 앞에 있는 값만 더하기
        else:
            answer -= temp # 뒷부분의 값은 합쳐서 빼기

    print(answer)
"""
