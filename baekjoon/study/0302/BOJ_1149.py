import sys
read = sys.stdin.readline


def house(lst, r, cost, prec):
    global mincost
    if r == N:
        if mincost > cost:
            mincost = cost
            return
    else:
        for c in range(3):
            if c != prec:
                if cost + lst[r][c] < mincost:
                    house(lst, r+1, cost + lst[r][c], c)
                else:
                    continue

def house2(lst):
    r = 1
    while r != N:
        lst[r][0] += min(lst[r-1][1], lst[r-1][2])
        lst[r][1] += min(lst[r - 1][0], lst[r - 1][2])
        lst[r][2] += min(lst[r - 1][0], lst[r - 1][1])
        r += 1
    return min(lst[N-1])




N = int(input())
lst = [list(map(int, read().split())) for _ in range(N)]
# mincost = 1000*10000
# house(lst, 0, 0, N+1)
print(house2(lst))