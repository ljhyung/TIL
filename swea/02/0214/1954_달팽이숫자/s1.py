import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

dr = [0, 1, 0, -1]      # 우, 하, 좌, 상
dc = [1, 0, -1, 0]

for i in range(tc):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    cnt = 1                             # 리스트에 숫자를 넣는 겸 종료 조건
    r, c = 0, 0                         # 현재 위치
    nr, nc = r, c                       # 나아갈 위치
    delta = 0                           # 방향 전환용 변수
    while cnt <= N**2:
        if 0 <= nr < N and 0 <= nc < N and not lst[nr][nc]:     # 인덱스 범위를 벗어나지 않고 값이 이미 채워졌는지 체크
            r, c = nr, nc               # 조건 만족하면 현재 위치를 이동
            lst[r][c] = cnt             # 숫자 넣고 증가
            cnt += 1
        else:
            delta = (delta + 1)%4       # 인덱스를 벗어나거나 값이 채워진 경우 방향 전환
        nr = r + dr[delta]
        nc = c + dc[delta]
    print(f'#{i+1}')
    for result in lst:
        print(*result)

# 이 코드도 되는데 nr, nc들을 증가시키고 체크하는 부분을 더 깔끔하게 했다
        # if 0 <= nr < N and 0 <= nc < N and not lst[nr][nc]:
        #     r, c = nr, nc
        #     lst[r][c] = cnt
        #     cnt += 1
        #     nr += dr[delta]
        #     nc += dc[delta]
        # else:
        #     delta = (delta + 1)%4
        #     nr, nc = r, c
        #     nr += dr[delta]
        #     nc += dc[delta]

