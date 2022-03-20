import sys
sys.stdin = open("input.txt", "r")


def post_order(T):
    if T<=V and not lst[T]:     # 0일 때 후위순회
        a = post_order(T*2)     # 자식 노드1
        b = post_order(T*2+1)   # 자식 노드2
        lst[T] = a+b
        return lst[T]
    elif T<=V and lst[T]:       # 값이 입력되있는 리프노트면 그대로 반환
        return lst[T]
    else:
        return 0                # 범위를 벗어나면 0을 반환


T = int(input())
for tc in range(1, T+1):
    V, M, L = map(int, input().split())
    lst = [0 for _ in range(V+1)]
    for _ in range(M):
        p, v = map(int, input().split())
        lst[p] = v
    result = post_order(L)
    print(f'#{tc} {result}')