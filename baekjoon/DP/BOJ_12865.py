'''
BOJ
평범한 배낭
골드 5

https://www.acmicpc.net/problem/12865
'''

N, K = map(int,input().split())
lst = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp = [[0,0]]

for i in range(N):
    dp.append(list(map(int,input().split())))

for i in range(1, N+1):
    for j in range(1,K+1):
        w = dp[i][0]
        v = dp[i][1]

        if j<w:
            lst[i][j] = lst[i-1][j]
        else:
            lst[i][j] = max(lst[i-1][j], lst[i-1][j-w] + v)

print(lst[N][K])