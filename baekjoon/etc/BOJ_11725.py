'''
BOJ
트리의 부모 찾기
실버 2

https://www.acmicpc.net/problem/11725
'''
from collections import deque


def bfs():
    queue = deque()
    queue.append(1)
    while queue:
        p = queue.popleft()
        for i in lst[p]:
            if root[i]==0:
                root[i] = p
                queue.append(i)

n = int(input())
lst = [[] for _ in range(n+1)]
root = [0]*(n+1)
root[1] = 1
for i in range(n-1):
    a,b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
bfs()
res = root[2:]
for i in res:
    print(i)