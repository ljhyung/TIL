import sys
sys.stdin = open("input.txt", "r")

def dfs(M, cnt):
    global mincnt
    if cnt>mincnt:
        return
    if M>11:
        if mincnt>cnt:
            mincnt = cnt
        return
    dfs(M+1, cnt + lst[M]*day)
    dfs(M+1, cnt + m1)
    dfs(M+3, cnt + m3)
    dfs(M+12, cnt + Year)

T = int(input())
for tc in range(1, T+1):
    day, m1, m3, Year = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    mincnt = 3000*30*12
    dfs(0, cnt)
    print(f'#{tc} {mincnt}')