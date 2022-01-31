N = int(input())
switch = list(map(int, input().split()))
st_num = int(input())
for i in range(st_num):
    s, num = map(int, input().split())
    if s == 1:
        for j in range(num-1, N, num):
            switch[j] = int(not switch[j])
    else:
        switch[num - 1] = int(not switch[num - 1])
        for g_rl_check in range(1, min(N-num+1,num)):
            if switch[num -1 - g_rl_check] != switch[num-1 + g_rl_check]:
                break
            switch[num - 1 - g_rl_check] = int(not switch[num - 1 - g_rl_check])
            switch[num - 1 + g_rl_check] = int(not switch[num - 1 + g_rl_check])

for j in range(len(switch)):
    print(int(switch[j]), end=' ')
    if (j+1)%20 == 0:
        print()

