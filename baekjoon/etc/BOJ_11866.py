'''
BOJ
요세푸스 문제 0
실버 5
10분
https://www.acmicpc.net/problem/11866
'''
n, k = map(int, input().split())
s=-1
queue = [i+1 for i in range(n)]
res = []
while queue:
    s = (s + k) % len(queue)
    res.append(queue.pop(s))
    s -= 1

print('<', end='')
for i in res[:-1]:
    print(i, end=', ')
print(res[-1], end='>')


