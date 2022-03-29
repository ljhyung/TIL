import sys
sys.stdin = open("input.txt", "r")


def greed(s):   # 그리디로 했는데 최적해가 안 나와서 다른 방법으로
    global cnt
    while s<24:
        mintime = 24
        minwork = -1
        for i in range(len(lst)):
            if lst[i][0]==s and lst[i][1]<=mintime:
                minwork = i
                mintime = lst[i][1]
        if minwork>=0:
            cnt += 1
            s = mintime
        else:
            s += 1

def sol(n,smcnt):
    global cnt
    if n==24 or n>nlst[-1][0]:
        cnt = max(cnt, smcnt)
        return
    for i in range(N):      # 가능한 경우 모두 체크
        if nlst[i][0]>=n:
            sol(nlst[i][1], smcnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    nlst = sorted(lst, key= lambda x: x[0]) # 작업 시작 시간이 이른 작업순으로 정렬
    cnt = 0
    # greed(0)
    sol(0, 0)
    print(f'#{tc} {cnt}')