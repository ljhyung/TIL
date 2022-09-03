## 플로이드 와샬로는 V의 범위가 20000까지이기에 풀리지 않는다
V, E = map(int, input().split())
S = int(input())
lst = [[float('inf') for _ in range(V)] for _ in range(V)]
for i in range(V):
    lst[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u-1][v-1] = min(lst[u-1][v-1], w)
    # lst[v-1][u-1] = w

for k in range(V):
    for r in range(V):
        for c in range(V):
            if lst[r][c]> lst[r][k] + lst[k][c]:
                lst[r][c] = lst[r][k] + lst[k][c]

answer = lst[S-1]
for i in answer:
    if i==float('inf'):
        print('INF')
    else: print(i)

## 우선순위큐를 이용한 다익스트라

import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline


def dijstra(start):

    distance = [INF] * (V+1)
    Q = []

    heapq.heappush(Q, [0, start])
    distance[start] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        for next_cost, next_vertex in graph[now_vertex]:
            next_cost = next_cost + now_cost
            if next_cost < distance[next_vertex]:
                distance[next_vertex] = next_cost
                heapq.heappush(Q, [next_cost, next_vertex])

    return distance


V, E = map(int, input().split())

K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

answer_arr = dijstra(K)

for i in range(1, len(answer_arr)):
    if i == K:
        print(0)
    elif answer_arr[i] == INF:
        print("INF")
    else:
        print(answer_arr[i])