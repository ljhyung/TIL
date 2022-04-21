
def suyeul(n):
    if n==M:
        print(*res)
        return
    for i in range(N):
        if visited[i]==0:
            visited[i]=1
            res.append(lst[i])
            suyeul(n+1)
            res.pop()
            visited[i]=0

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = []
visited = [0]*N
suyeul(0)