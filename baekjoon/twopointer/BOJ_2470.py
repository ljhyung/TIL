def solve():
    minnum = abs(lst[0]+lst[N-1])
    st=0
    en=N-1
    for i in range(N):
        for j in range(N - 1, i, -1):
            a = abs(lst[i] + lst[j])
            if a == 0:
                return lst[i], lst[j]
            elif a<minnum:
                minnum = a
                st = i
                en = j
    return lst[st], lst[en]

N = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(solve())
