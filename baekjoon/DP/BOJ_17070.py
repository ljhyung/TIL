'''
BOJ
파이프 옮기기 1
골드 5
https://www.acmicpc.net/problem/17070
'''

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst2 = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
lst2[0][0][1] = 1
for i in range(2,N):
    if not lst[0][i]:
        lst2[0][0][i] = lst2[0][0][i-1]
for r in range(1,N):
    for c in range(2,N):
        if lst[r][c]==0 and lst[r-1][c]==0 and lst[r][c-1]==0:
            lst2[2][r][c] = lst2[0][r-1][c-1] +lst2[1][r-1][c-1] +lst2[2][r-1][c-1]
        if lst[r][c]==0:
            lst2[0][r][c] = lst2[0][r][c-1]+lst2[2][r][c-1]
            lst2[1][r][c] = lst2[1][r-1][c] + lst2[2][r-1][c]
print(lst2[0][N-1][N-1] + lst2[1][N-1][N-1] + lst2[2][N-1][N-1])
