'''
https://www.acmicpc.net/problem/15486
퇴사 2
골드5
40분
'''
import sys

input = sys.stdin.readline
N = int(input())
lst = []
# for _ in range(N):
#     lst = [*lst,list(map(int, input().split()))]

money = [0 for _ in range(N+1)]     # 각 날짜에 쌓일 돈 기록용 끝나는 날 다음 날에 +해줬으므로 +1

for i in range(N):
    # lst = [*lst,list(map(int, input().split()))]
    lst.append(list(map(int, input().split())))
    finish = i+lst[i][0]        # 끝나는 날 돈은 받고 일은 못하므로 다음날 받는걸로
    temp = money[i-1] if i!=0 else 0    # 전날 돈
    if money[i]<temp:           # 전날 돈 아무것도 안 하고 온게 오늘까지 일한 돈보다 크면 전날 돈 이어서
        money[i] = temp
    if finish>N:continue        # 일 마치는 날이 기간 벗어나면 컷
    if money[finish] < lst[i][1]+money[i]:  # 끝나는 날 기록된 돈보다 오늘 돈이랑 보수 합친게 크면 갱신
        money[finish] = lst[i][1] + money[i]
if money[-1]<money[-2]:     # 입력이 N까지이므로 마지막날 돈 들어오는거랑 전날이랑 직접 비교
    money[-1]=money[-2]
# print(money)

print(money[-1])