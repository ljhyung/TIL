'''
https://www.acmicpc.net/problem/14719
빗물
골드5
30분
'''

H, W = map(int, input().split())

lst = [[0]*H for _ in range(W)]
res = 0
height = list(map(int, input().split()))
for i in range(W):
    for j in range(height[i]):
        lst[i][j]=1

for c in range(H):
    tempRes = 0
    cnt=-1
    flag=False              # 벽이면 false
    # if lst[0][c] == 1:
    #     flag = False
    # else:
    #     flag=True
    for r in range(W):
        if lst[r][c]==1:    # 벽이면
            if flag:        # 쌓일 물이 있으면
                if cnt<0:   # 처음이면 음수 상태 해제
                    cnt=0
                    flag=False  # flag 설정
                    continue
                tempRes += cnt  # 처음 아니면 flag가 True 전이 빈 곳이었다가 벽을 만나고 음수 상태가 아니므로 물 추가

            flag=False
            cnt = 0         # 벽 설정 후 cnt 초기화
        else:               # 빈 곳이면 flag True
            flag=True
            if cnt<0:continue   # 처음이면 그냥 넘김
            cnt += 1
    res += tempRes

print(res)
