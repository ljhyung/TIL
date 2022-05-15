def find(x):
    if x!=lst[x]:
        x = lst[x]
    return x

N, M = map(int, input().split())
lst = [0]*(N+1)
for i in range(N+1):
    lst[i] = i
for i in range(M):
    a,b = map(int, input().split())
    k = min(lst[a], lst[b], a, b)
    lst[a] = k
    lst[b] = k
for i in range(N+1):
    lst[i] = find(lst[i])
res = set(lst[1:])
print(len(res))
#
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# def bfs(k):
#     queue = deque(lst[k])
#     while queue:
#         a = queue.popleft()
#         visited[a] = 1
#         for s in range(len(lst[a])):
#             if visited[lst[a][s]]==0:
#                 queue.append(lst[a][s])
#
# N, M = map(int, input().split())
# lst = [[] for _ in range(N+1)]
# visited = [0]*(N+1)
# for i in range(M):
#     a,b = map(int, input().split())
#     lst[a]+= [b]
#     lst[b] += [a]
# cnt = 0
# for i in range(1,N+1):
#     if visited[i]==0:
#         bfs(i)
#         cnt += 1
# print(cnt)