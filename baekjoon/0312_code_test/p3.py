def func(r,c):      # 격자 최소 이동 횟수 중간에 대각선 지역은 1번만 통과
    lst1 = [[0] * (c+1) for _ in range(r+1)]
    for k in range(r+1):
        lst1[k][0] = 1
    for k in range(c+1):
        lst1[0][k] = 1
    for j in range(1,c+1):
        for i in range(1, r+1):
            lst1[i][j] += (lst1[i-1][j]+lst1[i][j-1])
    return lst1[r][c]

def solution(width, height, diagonals):
    answer = 0
    for dia in diagonals:
        r = dia[0]
        c = dia[1]
        answer += (func(r,c-1)*func(width-r+1, height-c) + func(r-1,c)*func(width-r, height-c+1))
    return answer%10000019

a = solution(4,3,[[2,2]])
print(a)
