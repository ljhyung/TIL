N = int(input())
for big_i in range(N):
    info2 = []
    info = list(map(int, input().split()))
    for k in range(info[3]):
        info2.append(list(map(int, input().split())))
    for i in range(1, info[0]+1): # 1팀부터 체크
        sc_set = {}
        for log_i in range(info[3]):  # 엔트리 갯수만큼
            if info2[log_i][0] == i:  # 1팀이면
                if sc_set.get(f'info2[{log_i}][1]') < info2[log_i][2]:
                    sc_set.update(info2[log_i][1] = f'{info2[log_i][2]}')


# 팀의 개수 info[0], 문제의 개수 info[1], 내팀 id info[2], 로그엔트리수 info[3]
# info2[0] [0] = 팀 id, [1] 문제번호, [2] 획득한 점수

# 1 1 30 info2[0][0]
# 2 3 30 info2[1][0]
# 1 2 40
# 1 2 20
# 3 1 70
#info = [3, 4, 3, 5]
# info2 = [[1,1,30], [2,3,30]]