import sys
sys.stdin = open("input.txt", "r")

def bfs(str, stc):
    queue = [[str,stc,0]]   # 출발지와 거리
    con = True      # 목적지 도착 여부
    while queue and con:
        a = queue.pop(0)
        if visited[a[0]][a[1]]==0:  # 방문 체크
            visited[a[0]][a[1]] = 1
            for delta in range(4):  # 4방향 확인
                nr = a[0]+dr[delta]
                nc = a[1]+dc[delta]
                if 0<=nr<N and 0<=nc<N: # 범위 밖인지 확인
                    if lst[nr][nc]==0 and visited[nr][nc]==0:   # 큐에 추가
                        queue.append([nr, nc, a[2]+1])
                    elif lst[nr][nc]==3:    # 목적지 도착
                        con = False
                        print(f'#{tc} {a[2]}')
                        return
    if con:
        print(f'#{tc} 0')

def dfs(str, stc, cnt):
    global result
    if lst[str][stc] == 3:
        result = cnt-1  # 도착 시 거리
        return
    else:
        for delta in range(4):
            nr = str + dr[delta]
            nc = stc + dc[delta]
            if 0 <= nr < N and 0 <= nc < N and lst[nr][nc] != 1 and visited[nr][nc]==0:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt +1)
                visited[nr][nc] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 2:
                str = i
                stc = j
    dr = [-1, 0, 1, 0]  # 상우하좌
    dc = [0, 1, 0, -1]

    ## bfs
    # bfs(str, stc)

    # dfs
    result = 0
    visited[str][stc] = 1   # 출발 부분 방문 체크
    dfs(str, stc, 0)
    print(f'#{tc} {result}')

