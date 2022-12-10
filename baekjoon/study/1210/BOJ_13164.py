'''
https://www.acmicpc.net/problem/13164
행복 유치원
골드5
30분
'''
# from itertools import combinations
#
# N, K = map(int, input().split())
# lst = list(map(int, input().split()))
# a = list(range(0,len(lst)-1))
# answer = float('inf')
# for walls in combinations(a,K-1):
#     head = 0
#     tempCost = 0
#     for wall in walls:
#         tempCost += lst[wall]-lst[head]
#         if tempCost>=answer:
#             break
#         head = wall+1
#     tempCost += lst[-1]-lst[head]
#     answer = min(answer,tempCost)
#
# print(answer)


N, K = map(int, input().split())
lst = list(map(int, input().split()))
wall = []
temp = []
for i in range(N-1):
    temp.append([lst[i+1]-lst[i],i])
temp.sort(reverse=True)
answer=0
for i in range(K-1):
    wall.append(temp[i][1])
wall.sort()
head=0
for i in wall:
    answer+= lst[i]-lst[head]
    head=i+1
answer += lst[-1]-lst[head]

print(answer)