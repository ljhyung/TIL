'''
BOJ
N과 M (8)
실버 3
10분
https://www.acmicpc.net/problem/15657
'''
def dfs(res):
    if len(res)==m:
        print(*res)
        return
    for i in range(n):
        if res and lst[i]>=res[-1]:
            dfs(res+[lst[i]])
        elif not res:
            dfs(res + [lst[i]])

n,m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

dfs([])
