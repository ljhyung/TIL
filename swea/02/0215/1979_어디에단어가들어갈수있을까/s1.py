import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(tc):
    result = 0
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if lst[j][k]:
                for delta in range(4):
                    cnt = 0
                    nr, nc = j, k
                    while 0<=nr<N and 0<=nc<N and lst[nr][nc]:
                        cnt += 1
                        nr += dr[delta]
                        nc += dc[delta]
                    if cnt == K:
                        result += 1
    print(f'#{i+1} {result}')