'''
https://www.acmicpc.net/problem/13905
세부
골드4

'''
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
s,e = map(int, input().split())
lst = [[] for _ in range(n+1)]

for _ in range(m):
    h1,h2,k = map(int, input().split())
    lst[h1].append([h2,k])
    lst[h2].append([h1,k])

visited = [0 for _ in range(n+1)]

def bfs():
    queue = deque()
    queue.append([s, float('inf')])
    visited[s] = float('inf')
    while queue:
        house, pepero = queue.popleft()
        if visited[house]>pepero:continue
        for next_house, bridge in lst[house]:
            next_pepero = min(bridge,pepero)
            if visited[next_house]<next_pepero:
                visited[next_house] = next_pepero
                queue.append([next_house,next_pepero])

bfs()
# print(lst)
print(visited[e])