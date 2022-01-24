from statistics import mean
N = int(input())
clist = []

for i in range(N):
    clist.append(list(map(int, input().split())))

for cclist in clist:
    cnt = 0
    for i in range(1, len(cclist)):
        if cclist[i] > mean(cclist[1:]):
            cnt += 1
    print(f'{cnt/cclist[0]*100:.3f}%')



