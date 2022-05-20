'''
PGS
광고 삽입
lv 2

https://programmers.co.kr/learn/courses/30/lessons/72411
'''
def solution(play_time, adv_time, logs):
    def to_sec(time):
        h, m, s = [int(f.lstrip('0') if f.lstrip('0') else 0) for f in time.split(':')]
        stime = h*3600 + m*60 + s
        return stime
    answer = ''
    playtime = to_sec(play_time)
    lst = [0 for _ in range(playtime+1)]
    for log in logs:
        s,e = log.split('-')
        s,e = to_sec(s), to_sec(e)
        lst[s] += 1
        lst[e] += -1
    for i in range(1,playtime+1):
        lst[i] += lst[i-1]
    for i in range(1,playtime+1):
        lst[i] += lst[i-1]
    adv_time = to_sec(adv_time)
    maxpeople = 0
    maxetime = 0
    for i in range(adv_time-1, playtime):
        temp = lst[i] - lst[i-adv_time]
        if i>=adv_time:
            if maxpeople<temp:
                maxpeople = temp
                maxetime = i+1
        else:
            if maxpeople<lst[i]:
                maxpeople = lst[i]
                maxetime = i+1
    maxstime = maxetime - adv_time
    # print(lst[93599], lst[93599+adv_time], lst[93600],lst[93600+adv_time])
    # print(maxstime,maxetime,adv_time)
    rh, rm, rs = str(maxstime//3600), str((maxstime%3600)//60), str((maxstime%3600)%60)
    if len(rh)==1:
        rh = '0'+rh
    if len(rm)==1:
        rm = '0'+rm
    if len(rs)==1:
        rs = '0'+rs
    # if maxstime<0:
    #     rh,rm,rs = '00','00','00'
    answer = f'{rh}:{rm}:{rs}'
    print(answer)
    return answer

# solution("02:03:55"	, "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
# solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00"	, "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])