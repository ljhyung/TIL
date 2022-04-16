N = int(input())
lst = list(map(int, input().split()))
res = [0]*N

for i in range(N):
    for j in range(0,i):
        if lst[i]>lst[j] and res[j]>=res[i]:
            res[i] = res[j] + 1
    if res[i]==0:
        res[i]=1
print(max(res))