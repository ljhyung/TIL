from math import ceil

day, night, V = list(map(int, input().split()))
cnt = ceil((V-night)/(day-night))
print(cnt)

# 실행시간 때문에 while 문 말고 계산하는걸로 바꿈