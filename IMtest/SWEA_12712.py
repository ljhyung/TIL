

T = int(input())
dr1 = [-1, 0, 0, 1]
dc1 = [0, -1, 1, 0]
dr2 = [-1, -1, 1, 1]
dc2 = [-1, 1, -1, 1]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    maxres = 0
    for r in range(N):
        for c in range(N):
            res1 = lst[r][c]
            res2 = lst[r][c]
            for delta in range(4):
                for K in range(1, M):
                    if 0<=r+dr1[delta]*K<N and 0<=c+dc1[delta]*K<N:
                        res1 += lst[r+dr1[delta]*K][c+dc1[delta]*K]
                    if 0<=r+dr2[delta]*K<N and 0<=c+dc2[delta]*K<N:
                        res2 += lst[r+dr2[delta]*K][c+dc2[delta]*K]
            if maxres < res1:
                maxres = res1
            if maxres < res2:
                maxres = res2
    print(f'#{tc} {maxres}')