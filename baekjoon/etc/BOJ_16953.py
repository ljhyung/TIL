'''
BOJ
A → B
실버 1
10분
https://www.acmicpc.net/problem/16953
'''
from collections import deque


def bfs(a):
    queue = deque()
    queue.append((a,1))
    while queue:
        c,cnt = queue.popleft()
        if 2*c<=b:
            if 2*c == b:
                return cnt+1
            queue.append((2*c,cnt+1))
        if 10*c+1<=b:
            if 10*c+1 == b:
                return cnt+1
            queue.append((10*c+1, cnt +1))
    return -1

a,b = map(int, input().split())
cnt = 1
res = bfs(a)
print(res)