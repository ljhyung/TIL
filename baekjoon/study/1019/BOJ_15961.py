'''
https://www.acmicpc.net/problem/15961
회전 초밥
골드4
30분
'''

N, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(N)]
head = 0
tail = k-1
res = 0
bonus = 0
visited = [0 for _ in range(d+1)]

for i in range(k):
    visited[lst[i]] += 1
for i in range(d+1):
    if visited[i]:res+=1
if visited[c]==0:
    bonus = 1
tempRes = res
res += bonus
for i in range(N):

    visited[lst[head+i]]-=1
    if visited[lst[head+i]]==0: # 초밥 종류가 없어지면
        tempRes-=1

    visited[lst[(tail+1+i)%N]]+=1
    if visited[lst[(tail+1+i)%N]]==1:   # 먹은 초밥이 새 초밥이면
        tempRes+=1

    if visited[c] == 0:         # 보너스 체크
        bonus=1
    else:
        bonus=0

    res = max(res, tempRes+bonus)

print(res)