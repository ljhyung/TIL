'''
BOJ
소수의 연속합
골드 3
https://www.acmicpc.net/problem/1644
'''

N = int(input())
minlengh = N
lst = [1] * 4000001
lst[0] = lst[1] = 0

s = 0
e = 0
res = 2
for i in range(2, int(4000001**0.5)):
    if lst[i]:
        for j in range(2 * i, 4000001, i):
            lst[j] = 0
sosu = [i for i, j in enumerate(lst) if j == True]
end = len(sosu)
answer = 0
while True:
    if res == N:
        answer += 1
        res -= sosu[s]
        s += 1
    elif res>N:
        res -= sosu[s]
        s += 1
    else:
        e += 1
        if e==end or sosu[e]>N:
            break
        res += sosu[e]



print(answer)