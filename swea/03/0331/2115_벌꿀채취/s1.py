import sys
sys.stdin = open("input.txt", "r")


def sol(nlst):
    global res
    for i in range(1<<M):       # 부분집합 구해서 cnt값 구하기
        smcnt = 0
        cnt = 0
        for j in range(M):
            if i&(1<<j):
                smcnt += nlst[j]
                cnt += nlst[j]**2
                if smcnt>C:     # C가 넘는 것은 통과
                    break
        else:
            if res<cnt:
                res = cnt


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    rlst = [[0]*(N-M+1) for _ in range(N)]
    for r in range(N):          # 각 벌통 가격 구하기
        for c in range(N-M+1):
            res = 0
            visited = [0]*M
            sol(lst[r][c:c+M])
            rlst[r][c] = res
    result = 0
    for r in range(N):          # 최대값 고르기, 중복되는 벌꿀 중 고를 수 있는 가장 큰 경우만 남기고 나머진 0으로
        for c in range(N-M):
            if bool(rlst[r][c]):
                only = max(rlst[r][c:c+M])
                onlyidx = rlst[r].index(only)
                for k in range(c,c+M):
                    if k<=N-M:
                        rlst[r][k]=0
                rlst[r][onlyidx] = only # 최대값은 남기기
    reslst = []
    for i in range(N):
        reslst += rlst[i]   # 고를 수 있는 모든 값을 한 리스트에 넣고 정렬 후 큰 값 두개 더하기
    reslst.sort(reverse=True)
    print(f'#{tc} {reslst[0]+reslst[1]}')