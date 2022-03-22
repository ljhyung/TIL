import sys
from collections import deque

sys.stdin = open("input.txt", "r")


def bfs(S, G):
    queue.append([S,0])
    visited[S] = 1
    while queue:
        temp = queue.popleft()
        if temp[0]==G:          # 도착지이면 거리 반환
            return temp[1]
        for i in lst[temp[0]]:  # 현재 위치와 연결된 노드 검색
            if visited[i]==0:   # 아직 체크하지 않은 곳이면 체크 후 큐에 추가
                visited[i]=1
                queue.append([i, temp[1]+1])
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    queue = deque()
    for i in range(E):
        p, c = map(int, input().split())
        lst[p].append(c)
        lst[c].append(p)
    S, G = map(int, input().split())
    res = bfs(S, G)
    print(f'#{tc} {res}')