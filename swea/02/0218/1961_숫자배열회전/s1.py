import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    result90 = [[0]*N for _ in range(N)]
    result180 = [[0]*N for _ in range(N)]
    result270 = [[0]*N for _ in range(N)]
    lst = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result90[i][j] += lst[N-j-1][i]
            result180[i][j] += lst[N-i-1][N-j-1]
            result270[i][j] += lst[j][N-i-1]
    print(f'#{tc}')
    for k in range(N):
        print(f'{"".join(map(str, result90[k]))} {"".join(map(str, result180[k]))} {"".join(map(str, result270[k]))}')