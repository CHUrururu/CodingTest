# 2차원 리스트 90도 회전

# 회전 후의 행 번호 = 회전 전의 열 번호
# 회전 후의 열 번호 = N - 1 - 회전 전의 행 번호

def rotate_90(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = list_2d[i][j]
    return new
