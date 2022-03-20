import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def bfs(r, c, l):
    cnt = 1
    queue = deque()
    queue.append((r,c))
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        if visited[r][c]==l:
            break
        for k in pipe[lst[r][c]]:
            nr, nc = r + dr[k], c + dc[k]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc]==0 and match[k] in pipe[lst[nr][nc]]:
                queue.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
    return cnt

pipe = [        # 파이프 종류
    [],
    [1,2,3,4],  # up=1, down=2, left=3, right=4
    [1,2],
    [3,4],
    [1,4],
    [2,4],
    [2,3],
    [1,3],
]
match = [0,2,1,4,3]   # 연결된지 확인용
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    result = bfs(R,C,L)
    print(f'#{tc} {result}')