import sys
sys.stdin = open("input.txt", "r")

def in_order(T):    #
    global cnt
    if T<=V:
        in_order(T*2)     # 자식1
        lst[T] = cnt
        cnt += 1
        in_order(T*2+1)   # 자식2



T = int(input())
for tc in range(1, T+1):
    V = int(input())
    lst = [0 for _ in range(V+1)]
    cnt = 1
    in_order(1)
    print(f'#{tc} {lst[1]} {lst[V//2]}')    # 루트 값과 V/2의 값 출력