import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(i, j):
    result = [lst[i][j]]
    while queue:
        r, c = queue.popleft()
        visited[r][c]=1
        for delta in range(4):
            nr = r+dr[delta]
            nc = c+dc[delta]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and abs(lst[r][c]-lst[nr][nc])==1:
                queue.append([nr,nc])
                result.append(lst[nr][nc])
    return min(result), len(result)


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_num = N
    max_len = 0
    lst = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                queue.append([i,j])
                tm, tl = bfs(i, j)
                if max_len<tl or max_len == tl and min_num>tm:
                    max_len = tl
                    min_num = tm
    print(f'#{tc} {min_num} {max_len}')