'''
https://www.acmicpc.net/problem/7662
이중 우선순위 큐
골드4

'''
import heapq
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    heap = []
    heapD = []
    k = int(input())
    sync = dict()            # 최대큐와 최소큐의 동기화를 위한 dict

    for _ in range(k):
        Oper, n = input().split()
        n = int(n)
        if Oper=='I':
            heapq.heappush(heap,n)
            heapq.heappush(heapD,-n)
            sync.setdefault(n,0)
            sync[n]+=1
        else:
            if len(heap)==0:continue
            if len(heapD)==0:continue
            if n==-1:
                while True:
                    temp = heapq.heappop(heap)
                    if sync[temp]:       # 최대에서 이미 빼지 않았는지 체크
                        sync[temp]-=1
                        break
                    if len(heap)==0:        # 비었으면 break
                        break

            else:
                while True:
                    temp = heapq.heappop(heapD)
                    if sync[-temp]:
                        sync[-temp] -= 1
                        break
                    if len(heapD) == 0:
                        break

    temp = sync.copy()
    for i in temp:
        if sync[i]==0:
            del sync[i]
    if sync:
        print(max(sync),min(sync))
    else:
        print('EMPTY')

