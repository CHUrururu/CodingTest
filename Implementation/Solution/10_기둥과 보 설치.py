n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

def possible(answer):
    for x, y, a in answer:
        if (a == 0): # 기둥
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 함
            if (y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer):
                continue
            return False
        
        elif (a == 1): # 보
            # 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 함
            if ([x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)):
                continue
            return False
    
    return True
    
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, a, b = frame
        
        if (b == 1): # 설치
            answer.append([x, y, a])
            if not (possible(answer)):
                answer.remove([x, y, a])
        
        if (b == 0): # 삭제
            answer.remove([x, y, a])
            if not (possible(answer)):
                answer.append([x, y, a])
                
    return sorted(answer)

print(solution(n, build_frame))
