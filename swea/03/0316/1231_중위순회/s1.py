import sys
sys.stdin = open("input.txt", "r")


def in_order(start):
    if start <= N:
        in_order(int(start)*2)
        print(lst[int(start)][1], end='')
        in_order(int(start)*2+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = [0] + [list(input().split()) for _ in range(N)]
    in_order(1)
    print()
