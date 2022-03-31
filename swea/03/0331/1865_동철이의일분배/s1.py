import sys
sys.stdin = open("input.txt", "r")

def bfs(n, cnt):
    global res
    if res>cnt or cnt == 0:
        return
    if n==N:
        if res<cnt:
            res = cnt
        return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            bfs(n+1, cnt*lst[n][i]/100)
            visited[i]=0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    res = 0
    bfs(0, 1)
    print(f'#{tc} {res*100:.6f}')