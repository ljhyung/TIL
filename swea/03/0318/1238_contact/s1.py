import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def bfs(T, cnt):
    queue.append(T)
    visited[T] = 1
    while queue:
        cnt += 1        # 몇번째 연락인지 기록
        res_list = []
        for _ in range(len(queue)):
            temp = queue.popleft()
            res_list.append(temp)   # 연락한 노드 추가
            for i in contect[temp]:
                if visited[i]==0:   # 이미 연락 했는지 체크
                    visited[i] = cnt
                    queue.append(i)
    return max(res_list)    # while문이 다 돌았을 때 마지막 res_list가 가장 마지막에 연락을 돌린 노드들



T = 10
for tc in range(1, T+1):
    queue = deque()
    N, start = map(int, input().split())
    visited = [0 for _ in range(101)]
    contect = [[] for _ in range(101)]          # 연락 가능한 수를 나타낸 배열
    lst = list(map(int, input().split()))
    for i in range(0, N, 2):
        if lst[i+1] not in contect[lst[i]]:     # 겹치는 입력 값이 있는지 체크
            contect[lst[i]] += [lst[i+1]]       # 연락망 추가
    result = bfs(start, 1)
    print(f'#{tc} {result}')


