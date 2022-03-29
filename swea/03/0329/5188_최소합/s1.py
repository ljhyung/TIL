import sys
sys.stdin = open("input.txt", "r")

dr = [0, 1]
dc = [1, 0]

def  sol(r,c):
    sumlst[r][c] = lst[r][c]
    for i in range(N):
        for j in range(N):
            for delta in range(2):
                nr = i+dr[delta]
                nc = j+dc[delta]
                if 0<=nr<N and 0<=nc<N:
                    sumlst[nr][nc] = min(sumlst[nr][nc], sumlst[i][j]+lst[nr][nc])  # 위에서 온 값과 왼쪽에서 온 값 중 최소


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    sumlst = [[260]*N for _ in range(N)]    # 경로에 도착할 때까지 걸리는 최소를 저장할 배열
    sol(0, 0)
    print(f'#{tc} {sumlst[N-1][N-1]}')