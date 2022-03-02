

def dicemove(i):
    if i == 1:  # 동
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif i == 2: # 서
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif i == 3:  # 북
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif i == 4:  # 남
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]


N, M, r, c, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
dice = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],      # [1][1]이 시작 밑 바닥, [3][1]이 윗면
]

dr = [0, 0, 0, -1, 1]     # 1동, 2서, 3북, 4남
dc = [0, 1, -1, 0, 0]

nr = r
nc = c
for i in command:
    if 0<=nr + dr[i]<N and 0<=nc + dc[i]<M:
        nr = nr + dr[i]
        nc = nc + dc[i]
        dicemove(i)
        if lst[nr][nc] == 0:
            lst[nr][nc] = dice[1][1]    #주사위 바닥면 숫자
        else:
            dice[1][1] = lst[nr][nc]    #주사위 바닥면 = lst[nr][nc]
            lst[nr][nc] = 0
        print(dice[3][1])               #주사위 윗면
