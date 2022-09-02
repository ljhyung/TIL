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
