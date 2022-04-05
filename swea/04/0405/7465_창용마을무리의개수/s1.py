import sys
sys.stdin = open("input.txt", "r")


def find_set(x):
    while x!=P[x]:
        x=P[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    P = [i for i in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        a = find_set(a)
        b = find_set(b)
        P[b] = a
    res = set()
    for i in P:
        res.add(find_set(i))
    print(f'#{tc} {len(res)-1}')