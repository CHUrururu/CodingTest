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
    # Additional Explanation#
    
    data = [1, 2, 4, 7]일 경우,
    
    target 1 -> 현재 data = [1], 만들 수 있는 숫자 범위: 1
    target 2(target 1 + 원소 1) -> 현재 data = [1, 2], 만들 수 있는 숫자 범위: 1, 2, 3(1 + 2)
    target 4(target 2 + 원소 2) -> 현재 data = [1, 2, 4], 만들 수 있는 숫자 범위: 1, 2, 3, 4, 5(1 + 4), 6(2 + 4), 7(3 + 4)
    target 8(target 4 + 원소 4) -> 현재 data = [1, 2, 4, 7], target 8은 새로 들어온 원소 7로 만들 수 없음
    
    따라서 8은 만들 수 없는 양의 정수 중 최솟값
"""