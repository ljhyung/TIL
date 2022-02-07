M = int(input())
N = int(input())
check = False
lst = []
for i in range(M, N+1):
    if i > 1:
        for k in range(2, i):
            if i%k == 0:
                check = True
                break
        if not check:
            lst.append(i)
        check = False

if not lst:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
    print(lst)
