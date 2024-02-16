import sys
input = sys.stdin.readline

N = int(input())
data = sorted(list(map(int, input().split())))
target = 1

for i in data:
    if (target < i):
        break
    target += i
    
print(target)



"""
    # Additional Explanation #
    
    data = [1, 2, 4, 7]일 경우,
    
    target 1 -> 현재 data = [1], 만들 수 있는 숫자 범위: 1
    target 3(target 1 + 원소 2) -> 현재 data = [1, 2], 만들 수 있는 숫자 범위: 1, 2, 3(1 + 2)
    target 7(target 3 + 원소 4) -> 현재 data = [1, 2, 4], 만들 수 있는 숫자 범위: 1, 2, 3, 4, 5(1 + 4), 6(2 + 4), 7(3 + 4)
    target 14(target 7 + 원소 7) -> 현재 data = [1, 2, 4, 7], 만들 수 있는 숫자 범위: 1, 2, 3, 4, 5, 6, 7, 8(1 + 7), 9(2 + 7), 10(3 + 7), 11(4 + 7), 12(5 + 7), 13(6 + 7), 14(7 + 7)
    
    따라서 15는 만들 수 없는 양의 정수 중 최솟값
"""
