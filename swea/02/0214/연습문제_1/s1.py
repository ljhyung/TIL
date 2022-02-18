import sys
sys.stdin = open("input.txt", "r")


tc = int(input())

dr = [-1, 0, 1, 0]      # 상, 우, 하, 좌
dc = [0, 1, 0, -1]
nr, nc = 0, 0

for i in range(tc):
    total = 0
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for k in range(4):                          # 상우하좌 확인
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N:         # 인덱스 벗어나는지 확인
                    total += abs(lst[r][c]-lst[nr][nc]) # 차이의 절댓값 합친다
    print(f'#{i+1} {total}')