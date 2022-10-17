'''
https://www.acmicpc.net/problem/11000
강의실 배정
골드 5
'''


# heapq 사용한 방법
import heapq
N=int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
heap = []
lst.sort()
heapq.heappush(heap,lst[0][1])  # 첫 회의 끝나는 시간 힙에 push
for i in range(1,len(lst)):
    if lst[i][0] < heap[0]:     # 새로운 회의 시작 시간이 제일 빨리 끝나는 회의보다 작으면 회의 생성 의미로 힙에 새로운 회의 끝나는 시간 push
        heapq.heappush(heap, lst[i][1])
    else:
        heapq.heappop(heap)     # 끝나고 방이 비었으니 끝난 회의 시간은 빼고 새로 시작한 회의 끝나는 시간 push
        heapq.heappush(heap, lst[i][1])

print(len(heap))                # 방 갯수 출력




