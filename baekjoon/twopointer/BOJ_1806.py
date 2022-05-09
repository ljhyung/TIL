'''
BOJ
부분합
골드 4
https://www.acmicpc.net/problem/1806
'''

N, S = map(int, input().split())
lst = list(map(int, input().split()))
s, e = 0, 0
minlen = N+1
res = lst[0]
while True:
    if minlen==1:
        break
    if res>=S:
        if (e-s)<minlen:
            minlen = e-s+1
        res -= lst[s]
        s += 1
    else:
        e += 1
        if e==N:
            break
        res += lst[e]
if minlen==N+1:
    minlen = 0
print(minlen)
