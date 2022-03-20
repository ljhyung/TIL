import sys
sys.stdin = open("input.txt", "r")

def make_heap(T):
    if T<=V:
        inheap[T] = lst[T-1]    # 추가 힙에 값 넣기
        fight(T)    # 부모랑 비교
        make_heap(T+1)

def fight(T):   # 자식부모 비교함수
    if T//2 and inheap[T] < inheap[T//2]:
        inheap[T], inheap[T//2] = inheap[T//2], inheap[T]
        fight(T//2)

def heap_sum(T):    # 조상 합 구하기
    global result
    if T//2:
        result += inheap[T//2]
        heap_sum(T//2)

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    lst = list(map(int, input().split()))
    inheap = [0 for _ in range(V+1)]        # 힙 표현할 배열
    make_heap(1)
    result = 0
    heap_sum(V)
    print(f'#{tc} {result}')