n = int(input())
lst = list(map(int, input().split()))
lst.sort()

x = int(input())
st = 0
en = n-1
cnt = 0
while st<en:
    a = lst[st]+lst[en]
    if a==x:
        cnt += 1
        st += 1
        en -= 1
    if a<x:
        st += 1
    if a>x:
        en -= 1
print(cnt)
