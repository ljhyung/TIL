def solution(s, times):
    answer = []
    everyday=True
    s=list(map(int,s.split(":")))  # 0:year, 1:month, 2:day, 3:hour, 4:minute, 5:second
    cnt=1
    for time in times:
        time=list(map(int,time.split(":")))    # 0:day, 1:hour, 2:minute, 3:second
        sec = s[5]+time[3]
        min = s[4]+time[2]
        hour = s[3]+time[1]
        day = s[2]+time[0]
        if sec>59:
            sec-=60
            min+=1
        s[5]=sec
        if min>59:
            min-=60
            hour+=1
        s[4]=min
        if hour>23:
            hour-=24
            day+=1
        s[3]=hour
        # print(day,s[2])
        cnt += day-s[2]
        if day-s[2]>1:
            everyday=False
        if day>30:
            day-=30
            s[1]+=1
        s[2]=day
        if s[1]>12:
            s[1]-=12
            s[0]+=1
    answer = [int(everyday),cnt]
    return answer



print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))
print(solution("2021:04:12:16:10:42", ["01:06:30:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"]))