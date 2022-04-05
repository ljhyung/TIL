import sys
sys.stdin = open("input.txt", "r")

def prim(start):
    D[start] = 0
    for _ in range(N):
        min_i = 0
        min_d = INF
        for i in range(N):
            if MST[i]==0 and min_d>D[i]:
                min_i = i
                min_d = D[i]

        MST[min_i] = 1
        for i in range(N):
            if MST[i]==0 and lst[min_i][i] and D[i]>lst[min_i][i]:
                D[i] = lst[min_i][i]
                P[i] = min_i
    return sum(D)

INF = 10**20
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    lst = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lst[i][j] = E*((x[i]-x[j])**2 + (y[i]-y[j])**2)

    D = [INF]*N
    MST = [0]*N
    P = [0]*N
    res = prim(0)
    print(f'#{tc} {res:.0f}')