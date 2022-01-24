# N = int(input())          # 재귀함수로 구한거
# nm = []
#
# def check(n, m):
#     cnt = 0
#     result = 0
#     if n == m:
#         return 1
#     elif n == 1:
#         return m
#     else:
#         return check(n, n) + sum([check(n-1, i) for i in range(n,m)])
#
# for j in range(N):
#     nm.append(list(map(int, input().split())))
#     print(check(nm[j][0], nm[j][1]))

# nCm 으로 구한거

import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)
