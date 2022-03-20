import sys

sys.stdin = open("input.txt", "r")

def bfs(str, stc):
    queue = [[str,stc,0]]
    con = True
    while queue and con:
        a = queue.pop(0)
        if visited[a[0]][a[1]]==0:
            visited[a[0]][a[1]] = 1
            for delta in range(4):
                nr = a[0]+dr[delta]
                nc = a[1]+dc[delta]
                if 0<=nr<N and 0<=nc<N:
                    if lst[nr][nc]==0 and visited[nr][nc]==0:
                        queue.append([nr, nc, a[2]+1])
                    elif lst[nr][nc]==3:
                        con = False
                        print(f'#{tc} 1')
                        return
    if con:
        print(f'#{tc} 0')


for tc in range(1, 11):
    I = int(input())
    N = 16
    lst = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                str = i
                stc = j
    dr = [-1, 0, 1, 0]  # 상우하좌
    dc = [0, 1, 0, -1]
    bfs(str,stc)


