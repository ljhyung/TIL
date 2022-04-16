N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

res = [0]*N
for i in range(N):
    for j in range(0,i):
        if lst[i][1]>lst[j][1] and res[i]<=res[j]+1:
            res[i] = res[j]+1
    if res[i]==0:
        res[i]=1
print(N-max(res))