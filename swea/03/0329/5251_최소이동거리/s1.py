import sys
sys.stdin = open("input.txt", "r")

def sol(n, d):
    global mind
    if d>mind:      # 가지치기
        return
    if n == N and mind>d:
        mind = d
        return
    for i in range(N+1):    # 가능한 모든 경로 탐색
        if lst[n][i]:
            sol(i, d+lst[n][i])


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    lst = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        r,c,d = map(int, input().split())
        lst[r][c] = d
    mind = 10*1000000
    sol(0, 0)
    print(f'#{tc} {mind}')