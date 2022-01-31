ga, se = map(int, input().split())
N = int(input())
ga_lst = [0]
se_lst = [0]
for i in range(N):
    ga_se, cut = map(int, input().split())
    if ga_se:
        ga_lst.append(cut)
    else:
        se_lst.append(cut)
ga_lst.append(ga)
ga_lst.sort()
se_lst.append(se)
se_lst.sort()
max_area = 0
for i in range(1, len(ga_lst)):
    for j in range(1, len(se_lst)):
        if (ga_lst[i]-ga_lst[i-1])*(se_lst[j]-se_lst[j-1]) > max_area:
            max_area = (ga_lst[i]-ga_lst[i-1])*(se_lst[j]-se_lst[j-1])
print(max_area)