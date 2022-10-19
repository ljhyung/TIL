'''
https://www.acmicpc.net/problem/1368
물대기
골드2
2시간
'''
import heapq
from collections import deque

N = int(input())
dig = [int(input()) for _ in range(N)]
heap = []
for i in range(N):
    heapq.heappush(heap,[dig[i],i])
connect = [list(map(int, input().split())) for _ in range(N)]
answer = 0
# path = [[0]*N for _ in range(N)]


def prim():     # prim에서 kruskal로 바뀌었다
    global answer
    visited = [0 for _ in range(N)]

    # heap = []
    #
    # for i in range(1,N):
    #     heapq.heappush(heap, [connect[0][i],0,i])
    cnt = 1

    while heap:
        cost,now = heapq.heappop(heap)
        if visited[now]:continue
        visited[now]=1
        cnt += 1
        answer += cost
        for i in range(N):
            # if i==next or visited[i]:continue
            if i==now:continue
            if dig[i]>connect[now][i]:
                heapq.heappush(heap, [connect[now][i], i])


prim()      # mst 형성, path에 저장

print(answer)


# print(path)
#
# answer = float('inf')
# visited = [0 for _ in range(N)]
# checkW = [0 for _ in range(N)]
# res = 0
# for i in range(N):
#     temp = float('inf')
#     for j in range(N):
#         if path[i][j]:
#             temp = min(temp, connect[i][j])
#     if dig[i]<=temp:
#         res += dig[i]
#         checkW[i] = dig[i]
#         visited[i]=1
#
# print(visited)
#
# def bfs(s,visited,ress,check):
#     global answer
#     visitedd = visited[:]
#     checkk = check[:]
#     if visitedd[s]==0:
#         visitedd[s] = 1
#         ress = dig[s]
#         checkk[s]=dig[s]
#     queue = deque()
#     queue.append(s)
#     cnt = 1
#     while cnt<N:
#         now = queue.popleft()
#         for next in range(N):
#             if path[now][next] and visitedd[next]==0:
#                 queue.append(next)
#                 cnt += 1
#                 visitedd[next]=1
#                 ress += min(dig[next],connect[now][next])
#                 checkk[next]=min(dig[next],connect[now][next])
#             elif path[now][next] and visitedd[next] and connect[now][next]<checkk[now]:
#                 ress -= checkk[now]
#                 checkk[now] = connect[now][next]
#                 ress += checkk[now]
#     answer = min(answer, ress)
#
# for i in range(N):
#     bfs(i,visited,res,checkW)
#
# print(answer)

