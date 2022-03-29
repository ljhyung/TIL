import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dr = [1, 1, -1, -1] # 좌하, 우하, 우상, 좌상
    dc = [-1, 1, 1, -1]
