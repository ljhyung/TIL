import sys
sys.stdin = open("input.txt", "r")


def dfs(n, alst, blst):
    global res
    if n>=N:
        if len(alst)==len(blst):
            suma, sumb = 0, 0
            for i in range(N//2):
                for j in range(N//2):
                    suma += lst[alst[i]][alst[j]]
                    sumb += lst[blst[i]][blst[j]]
            tpres = abs(suma-sumb)
            if res>tpres:
                res = tpres
        return
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    alst = []
    blst = []
    res = 20000*N**2
    dfs(0, alst, blst)
    print(f'#{tc} {res}')