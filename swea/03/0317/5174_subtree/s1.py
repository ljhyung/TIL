import sys
sys.stdin = open("input.txt", "r")

def pre_order(T):
    global cnt
    if T:
        cnt += 1    # 숫자 세주기
        pre_order(lst[T][0])
        pre_order(lst[T][1])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    raw = list(map(int, input().split()))
    lst = [[0, 0] for _ in range(E+2)]
    for i in range(0, E*2, 2):      # 자식 노드 채워넣기
        if not lst[raw[i]][0]:
            lst[raw[i]][0] = raw[i+1]
        else:
            lst[raw[i]][1] = raw[i + 1]
    cnt = 0
    pre_order(N)
    print(f'#{tc} {cnt}')