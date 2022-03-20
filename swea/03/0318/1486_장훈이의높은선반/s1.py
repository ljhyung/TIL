import sys
sys.stdin = open("input.txt", "r")


def dfs(n, alst):
    global res
    if n>=N:
        sum = 0
        if alst:
            for k in alst:
                sum += lst[k]
            if sum>=B and res>sum-B:
                res = sum-B
        return
    dfs(n+1, alst+[n])
    dfs(n+1, alst)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    alst = []
    res = sum(lst)
    dfs(0, alst)
    print(f'#{tc} {res}')