'''
https://www.acmicpc.net/problem/1965
상자넣기
실버2

'''

n = int(input())
lst = list(map(int,input().split()))
answer = [1 for _ in range(n)]
for i in range(n):
    for k in range(i):
        if lst[i]>lst[k] and answer[i]<answer[k]+1:
            answer[i]=answer[k]+1


print(max(answer))