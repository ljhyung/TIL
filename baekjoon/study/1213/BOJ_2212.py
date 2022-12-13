'''
https://www.acmicpc.net/problem/2212
센서
골드5
30분
'''

N = int(input())
K = int(input())
lst = list(map(int, input().split()))
lst = list(set(lst))
lst.sort()
answer=0
dis = []
for i in range(len(lst)-1):
    dis.append([lst[i+1]-lst[i],i])
dis.sort(reverse=True)
dis=dis[:K-1]
dis.sort(key=lambda x:x[1])
head=0
for i in range(K-1):
    if i>=len(dis):
        break
    answer += lst[dis[i][1]]-lst[head]
    head=dis[i][1]+1
answer+=lst[-1]-lst[head]
print(answer)
