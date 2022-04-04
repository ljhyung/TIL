import sys
sys.stdin = open("input.txt", "r")


def dfs(n):
    global res
    if n == N:
        res += 1
        return
    for i in range(N):
        if v1[i]==v2[n+i]==v3[n-i]==0:
            v1[i]=v2[n+i]=v3[n-i]=1
            dfs(n+1)
            v1[i]=v2[n+i]=v3[n-i]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    v1 = [0] * N * 2
    v2 = [0] * N * 2
    v3 = [0] * N * 2
    res = 0
    dfs(0)

    print(f'#{tc} {res}')