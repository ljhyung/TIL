import sys
sys.stdin = open("input.txt", "r")


def sol(s):
    global t, carrot, N
    cnt = 0
    while cnt<t:
        carrot[(lst[s-1])%N] += 1
        carrot[(lst[s-1] - 2) % N] += 1
        s = lst[s-1]
        cnt += 1

T = int(input())
for tc in range(1, T+1):
    s, t = map(int, input().split())
    lst = list(map(int, input().split()))
    N = len(lst)
    carrot = [0 for _ in range(N)]
    sol(s)
    res = []
    m = max(carrot)
    for i in range(N):
        if carrot[i] == m:
            res.append(i+1)
    temp = ' '.join(map(str, res))
    print(f'#{tc} {temp}')

