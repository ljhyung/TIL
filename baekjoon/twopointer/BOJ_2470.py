N = int(input())
lst = list(map(int, input().split()))
lst.sort()
st = 0
en = N-1
resst = 0
resen = N-1
minnum = abs(lst[st]+lst[en])
while st<en:
    a = lst[st]+lst[en]
    if a==0:
        resst = st
        resen = en
        break
    if abs(a)<minnum:
        minnum = abs(a)
        resst = st
        resen = en
    if a<0:
        st += 1
    elif a>0:
        en -= 1

print(lst[resst], lst[resen])
