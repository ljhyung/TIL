from collections import deque


def bfs():
    while queue:
        h,r,c = queue.popleft()
        for delta in range(6):
            nr = r + dr[delta]
            nc = c + dc[delta]
            nh = h + dh[delta]
            if 0<=nr<N and 0<=nc<M and 0<=nh<H and lst[nh][nr][nc]==0:
                lst[nh][nr][nc] = lst[h][r][c]+1
                queue.append((nh,nr,nc))

def result():
    res = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if lst[h][r][c] == 0:
                    return -1
                else:
                    res = max(res, lst[h][r][c])
    if res == 1:
        return 0
    else:
        return res-1

M,N,H = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dr = [0, 0, 1, -1, 0, 0]
dc = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
queue = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if lst[h][r][c] == 1:
                queue.append((h,r,c))
bfs()
print(result())
