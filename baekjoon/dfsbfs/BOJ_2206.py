'''
BOJ
벽 부수고 이동하기
골드 4
https://www.acmicpc.net/problem/2206
'''
from collections import deque


def bfs(r,c):
    global N,M
    queue = deque()
    queue.append((0,r,c))
    visited[0][r][c] = 1
    while queue:
        b,r,c = queue.popleft()
        if r==N-1 and c==M-1:
            return visited[b][r][c]
        for delta in range(4):
            nr = r+dr[delta]
            nc = c+dc[delta]
            if 0 > nr or nr >= N or 0 > nc or nc >= M:
                continue
            if lst[nr][nc]==1 and b==0:
                visited[1][nr][nc] = visited[b][r][c] + 1
                queue.append((1, nr, nc))
            elif lst[nr][nc]==0 and visited[b][nr][nc]==0:
                visited[b][nr][nc] = visited[b][r][c]+1
                queue.append((b,nr,nc))
    return -1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
res = bfs(0,0)
print(res)