N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
lst = list(set(lst))
res = []
for i in range(1,51):
    temp = []
    for j in lst:
        if len(j)==i:
            temp.append(j)
    temp.sort()
    res += temp
for r in res:
    print(r)